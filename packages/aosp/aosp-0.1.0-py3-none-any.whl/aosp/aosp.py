import configparser
import os
import re
import sys
import tempfile
from typing import List, Optional
from os import path as _p

import sh
from yautil import docker_sh
from yautil.pyshutil import compile_shargs

PROFILE_PATH = _p.join(_p.dirname(_p.realpath(__file__)), 'config', 'aosp_profiles.ini')


def android_emulator_done(cmd: sh.RunningCommand, success, exit_code):
    print(f'emulator ended!! success: {success}, exit_code: {exit_code}')
    quit()
    # print(f'error: failed to start Android emulator.', file=sys.stderr)


class AospProductOut:
    aosp: object

    def __init__(self, aosp: object):
        self.aosp = aosp

    @property
    def name(self) -> str:
        return self.aosp.env['ANDROID_PRODUCT_OUT']

    @property
    def dir(self) -> str:
        return self.name

    @property
    def system_dir(self) -> str:
        return _p.join(self.name, self.aosp._cfg['SYSTEM_PATH'])

    @property
    def system_lib_dirs(self) -> List[str]:
        return [_p.join(self.name, path)
                for path in self.aosp._cfg['LD_LIBRARY_PATH'].split(os.pathsep)]

    @property
    def system_bin_dirs(self) -> List[str]:
        return [_p.join(self.name, path)
                for path in self.aosp._cfg['PATH'].split(os.pathsep)]

    @property
    def rc_path(self) -> str:
        return self.aosp._cfg['RC_PATH']

    def find_system_lib(self, basename: str) -> List[str]:
        return [_p.join(dir, basename) for dir in self.system_lib_dirs if _p.isfile(_p.join(dir, basename))]

    def find_system_bin(self, basename: str) -> List[str]:
        return [_p.join(dir, basename) for dir in self.system_bin_dirs if _p.isfile(_p.join(dir, basename))]


class Aosp:
    __path: str
    __build_target: str
    __env = None
    __build_var = None
    __cfg = None
    __out = None
    __canonical_version = None
    __toolchain_abs_prefix = None

    external_paths: list[str]

    @classmethod
    def from_path(cls, path: str, build_target: str = None):
        return cls(path=path, build_target=build_target)

    def __init__(self, path: str, build_target: str):
        self.__path = _p.realpath(path)
        self.__build_target = build_target
        self.external_paths = []

    @property
    def name(self) -> str:
        return self.__path

    @property
    def canonical_version(self) -> str:
        if not self.__canonical_version:
            version_mks = str(sh.find(_p.join(self.__path, 'build'), name='version_defaults.mk',
                                      _long_prefix='-', _long_sep=' ')).strip().split('\n')
            assert len(version_mks) == 1
            version_mk = version_mks[0]

            with open(version_mk, 'r') as f:
                if not (m := re.search(r'^\s*PLATFORM_VERSION.*?(?P<version>\d+(\.\d+)*)$', f.read(), re.M)):
                    raise Exception('failed to get canonical version')
                # print(m.group(0))

            self.__canonical_version = m['version']
        return self.__canonical_version

    @property
    def _cfg(self):
        if not self.__cfg:
            cfgp = configparser.ConfigParser()
            cfgp.read(PROFILE_PATH)
            try:
                self.__cfg = cfgp[self.canonical_version]
            except KeyError:
                raise Exception(f'error: cannot find config for build version \'{self.canonical_version}\''
                                f' from {PROFILE_PATH}. {cfgp.sections()}')
        return self.__cfg

    @property
    def path(self) -> str:
        return self.__path

    @property
    def build_target(self) -> str:
        if not self.__build_target:
            raise Exception('AOSP build target is not configured')
        return self.__build_target

    @build_target.setter
    def build_target(self, value: str):
        self.__build_target = value

    @property
    def env(self) -> dict[str, str]:
        if not self.__env:
            sout = str(self.bash(c='env'))

            env = {}
            for line in filter(None, sout.splitlines()):
                var, val = line.split('=', 1)
                env[var] = val
            self.__env = env
        return self.__env

    @property
    def build_var(self) -> dict:
        if not self.__build_var:
            sout = str(self.bash(c=f'lunch {self.build_target}'))

            build_var = {}
            for line in sout.splitlines():
                if not (m := re.search(r'(?P<var>[^=]+)=(?P<val>.*)', line)):
                    continue
                build_var[m['var']] = m['val']
            self.__build_var = build_var
        return self.__build_var

    @property
    def manifest_merge_branch(self) -> str:

        # 7-bit C1 ANSI sequences
        ansi_escape = re.compile(r'''
            \x1B  # ESC
            (?:   # 7-bit C1 Fe (except CSI)
                [@-Z\\-_]
            |     # or [ for CSI, followed by a control sequence
                \[
                [0-?]*  # Parameter bytes
                [ -/]*  # Intermediate bytes
                [@-~]   # Final byte
            )
        ''', re.VERBOSE)

        repo_info = str(sh.repo.info('x', _cwd=self.path, _ok_code=[0, 1]))

        # remove color codes
        repo_info = ansi_escape.sub('', repo_info)

        if m := re.search(r'Manifest merge branch: refs/heads/(?P<branch>[^\s]+)', repo_info):
            return m['branch']
        return None

    @property
    def out(self) -> AospProductOut:
        if not self.__out:
            self.__out = AospProductOut(self)
        return self.__out

    def __get_toolchain_abs_prefix_from_env(self) -> Optional[str]:
        try:
            toolchain = self.env['ANDROID_TOOLCHAIN']
        except KeyError:
            return

        prefixes = None
        essential_tools = ['gcc', 'ld', 'ar']
        tools = os.listdir(toolchain)

        for et in essential_tools:
            pp = set(t[:-len(et)] for t in filter(lambda t: t.endswith(et), tools))
            if prefixes is None:
                prefixes = pp
            else:
                prefixes.intersection_update(pp)

        if len(prefixes) > 1:
            prefixes = {*filter(lambda p: 'kernel' not in p, prefixes)}

        if len(prefixes) == 1:
            return _p.join(toolchain, prefixes.pop())

        # raise Exception('error: failed to resolve toolchain prefix')

    def __get_toolchain_abs_prefix_from_make(self) -> Optional[str]:
        # https://stackoverflow.com/a/25817631/3836385
        tmpmk = tempfile.NamedTemporaryFile(mode='w')
        with open(_p.join(self.name, 'Makefile'), 'r') as mk:
            tmpmk.write(mk.read())
        tmpmk.writelines(['print-%  : ; @echo $* = $($*)'])
        tmpmk.flush()
        self.external_paths.append(tmpmk.name)

        make_var = 'TARGET_TOOLS_PREFIX'

        try:
            out = str(self.bash(c=f'make --file {tmpmk.name} print-{make_var}'))
            if m := re.search(fr'^{make_var} = (?P<val>.*)$', out, re.M):
                return m.group('val')
        except sh.ErrorReturnCode:
            return

    @property
    def toolchain_abs_prefix(self) -> str:
        if self.__toolchain_abs_prefix is not None:
            pass
        elif (not self.canonical_version.startswith('4.')) \
                and (prefix := self.__get_toolchain_abs_prefix_from_env()) is not None:
            self.__toolchain_abs_prefix = prefix
        elif (prefix := self.__get_toolchain_abs_prefix_from_make()) is not None:
            self.__toolchain_abs_prefix = prefix
        else:
            self.__toolchain_abs_prefix = ''

        return _p.realpath(_p.join(self.name, self.__toolchain_abs_prefix))

    @property
    def toolchain_path(self) -> str:
        return _p.dirname(self.toolchain_abs_prefix)

    @property
    def toolchain_prefix(self) -> str:
        return _p.basename(self.toolchain_abs_prefix)

    @property
    def __docker_build_context(self) -> Optional[str]:
        if ctx := self._cfg.get('DOCKER_BUILD_CONTEXT', fallback=None):
            return _p.join(_p.dirname(__file__), 'docker-build-context', ctx)

        return None

    @property
    def bash(self) -> sh.Command:
        return self.get_bash()

    def get_bash(self, try_docker: bool = True, environ: dict = None, xforwarding: bool = False) -> sh.Command:
        class __Bash:
            __base: sh.Command
            __c_prefix: str

            def __init__(self, base: sh.Command, c_prefix: str = ''):
                self.__base = base
                self.__c_prefix = c_prefix

            def __getattr__(self, name):
                return getattr(self.__base, name)

            def __call__(self, *args, **kwargs):
                if 'c' in kwargs:
                    kwargs['c'] = self.__c_prefix + kwargs['c']

                return self.__base(*args, **kwargs)

        c_prefix = (
            f'cd {_p.realpath(self.__path)}'
            f' && . ./build/envsetup.sh >/dev/null'
            f' && lunch {self.build_target} >/dev/null; '
        )

        if environ is None:
            environ = {}

        if try_docker and (ctx := self.__docker_build_context):
            dsh = docker_sh(
                ctx,
                *[f'-e{k}={v}' for k, v in environ.items()],
                volumes=[f'{_p.realpath(self.__path)}:{_p.realpath(self.__path)}:rw',
                         *map(lambda p: f'{_p.realpath(p)}:{_p.realpath(p)}:rw', self.external_paths)],
                kvm=_p.exists('/dev/kvm'),
                xforwarding=xforwarding,
                # verbose=True,
            )

            return __Bash(dsh.bake('/bin/bash'), c_prefix)

        else:
            env_old = os.environ.copy()
            # while (p := sh.which('python')) and (p2 := sh.which('python2')) and (_p.realpath(p) != _p.realpath(p2)):
            #     # print(f'python: {_p.realpath(p)}, python2: {_p.realpath(p2)}')
            #     env = os.environ['PATH'].split(_p.pathsep)
            #     env.remove(_p.dirname(p))
            #     os.environ['PATH'] = _p.pathsep.join(env)
            env = os.environ
            os.environ = env_old

            env = {**env, **environ}

            return __Bash(sh.bash.bake(_cwd='/', _env=env), c_prefix)

    def make(self, *args, **kwargs) -> sh.RunningCommand:
        a, sha = compile_shargs(*args, **kwargs)
        return self.bash(c=f'make {" ".join(a)}', **sha)

    def emulator(self,
                 command: str = 'emulator',
                 port: int = None,
                 adb_server_port: int = None,
                 writable_system: bool = False,
                 selinux: str = None,
                 system: str = None,
                 ramdisk: str = None,
                 sdcard: str = None,
                 kernel: str = None,
                 fg: bool = True,
                 try_docker: bool = True,
                 **extra_emulator_opts,
                 ) -> Optional[sh.RunningCommand]:

        kwargs = {}
        environ = {}

        if adb_server_port is not None:
            environ['ANDROID_ADB_SERVER_PORT'] = str(adb_server_port)
            # kwargs['_env'] = {**os.environ, 'ANDROID_ADB_SERVER_PORT': str(adb_server_port)}

        if fg:
            kwargs['_fg'] = True
        else:
            kwargs['_bg'] = True
            # kwargs['_bg_exc'] = True
            # kwargs['_tty_in'] = True
            # kwargs['_tty_out'] = True
            # kwargs['_unify_ttys'] = True
            # kwargs['_err_to_out'] = True
            kwargs['_done'] = android_emulator_done

        args, shargs = compile_shargs(**extra_emulator_opts, _long_prefix='-', _long_sep=' ')

        return self.get_bash(try_docker=try_docker, environ=environ, xforwarding=True)(
            c=command
              + (f' -port {port}' if port is not None else '')
              + (f' -writable-system' if writable_system else '')
              + (f' -selinux {selinux}' if selinux is not None else '')
              + (f' -system {system}' if system is not None else '')
              + (f' -ramdisk {ramdisk}' if ramdisk is not None else '')
              + (f' -sdcard {sdcard}' if sdcard is not None else '')
              + (f' -kernel {kernel}' if kernel is not None else '')
              + ' ' + ' '.join(args),
            **kwargs,
        )

    def __hash__(self) -> int:
        return id(self)


def load_aosp(path: str, build_target: str = None) -> Aosp:
    return Aosp.from_path(path=path, build_target=build_target)

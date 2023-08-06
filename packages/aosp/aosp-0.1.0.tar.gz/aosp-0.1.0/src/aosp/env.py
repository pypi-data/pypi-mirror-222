import sh


def get_env(path, target: str = None) -> dict:
    cmd = fr'. ./build/envsetup.sh >/dev/null'
    if target:
        cmd += fr' && lunch {target} >/dev/null'
    cmd += fr' && env'
    sout = str(sh.bash(c=cmd, _cwd=path))

    env = {}
    for line in filter(None, sout.splitlines()):
        var, val = line.split('=', 1)
        env[var] = val

    return env

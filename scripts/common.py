import os

INSTALL_PREFIX = '/usr'


def ensure(program: str, args: list[str]):
    command = " ".join([program, *args])
    print(command)
    if os.system(command) != 0:
        raise Exception("Command failed")


class Builder:
    def __init__(self, name: str, options: list[str] | None=None):
        self.name = name
        self.root = os.getcwd()
        self.destdir = f'{self.root}/build/{self.name}'
        self.options = options or []

    def patch(self):
        os.chdir(f'{self.root}/fcitx5-{self.name}')
        file = f'../patches/{self.name}.patch'
        if os.system('git diff --ignore-submodules --exit-code > /dev/null') == 0 and os.path.isfile(file):
            ensure('git', ['apply', file])
        ensure('sed', [
            '-i',
            f'"s|\\"/usr/include|\\"{self.root}/build/sysroot/usr/include|g"',
            '$(find ../build/sysroot/usr -name "*.cmake")'
        ])
        ensure('sed', [
            '-i',
            f'"s|=/usr/include|={self.root}/build/sysroot/usr/include|g"',
            '$(find ../build/sysroot/usr -name "*.pc")'
        ])

    def configure(self):
        os.environ['PKG_CONFIG_PATH'] = f'{self.root}/build/sysroot/usr/lib/pkgconfig'
        ensure('emcmake', ['cmake',
            '-B', 'build', '-G', 'Ninja',
            f'-DCMAKE_INSTALL_PREFIX={INSTALL_PREFIX}',
            f'-DCMAKE_FIND_ROOT_PATH="{self.root}/build/sysroot/usr;/usr"',
            '-DCMAKE_BUILD_TYPE=Release',
            *self.options
        ])

    def build(self):
        ensure('cmake', ['--build', 'build'])

    def install(self):
        os.environ['DESTDIR'] = self.destdir
        ensure('cmake', ['--install', 'build'])

    def package(self):
        os.chdir(f'{self.destdir}{INSTALL_PREFIX}')
        ensure('tar', ['cjvf', f'{self.destdir}.tar.bz2', '*'])

    def exec(self):
        self.patch()
        self.configure()
        ensure('sed', [
            '-i',
            f'"s|-I/usr|-I{self.root}/build/sysroot/usr|g"',
            'build/build.ninja'
        ])
        ensure('sed', [
            '-i',
            f'"s|-isystem /usr|-isystem {self.root}/build/sysroot/usr|g"',
            'build/build.ninja'
        ])
        self.build()
        self.install()
        self.package()

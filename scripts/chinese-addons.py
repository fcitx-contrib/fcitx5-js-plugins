from common import Builder, ensure

src = 'build/sysroot/usr'
dst = 'build/chinese-addons/usr'
ensure('mkdir', ['-p', f'{dst}/lib'])
ensure('mkdir', ['-p', f'{dst}/share'])
ensure('cp', ['-r', f'{src}/lib/libime', f'{dst}/lib'])
ensure('cp', ['-r', f'{src}/share/libime', f'{dst}/share'])
ensure('cp', ['-r', f'{src}/share/opencc', f'{dst}/share'])

Builder('chinese-addons', [
    '-DENABLE_CLOUDPINYIN=OFF',
    '-DENABLE_TEST=OFF',
    '-DENABLE_GUI=OFF'
]).exec()

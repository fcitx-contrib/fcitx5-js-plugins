from common import Builder, ensure

rime_data_dir = '/usr/share/rime-data'
rime_data_install_dir = f'build/rime{rime_data_dir}'
ensure('mkdir', ['-p', rime_data_install_dir])
ensure('cp', ['fcitx5-rime-data/rime-prelude/*.yaml', rime_data_install_dir])
ensure('cp', ['fcitx5-rime-data/rime-essay/essay.txt', rime_data_install_dir])
ensure('cp', ['fcitx5-rime-data/rime-luna-pinyin/*.yaml', rime_data_install_dir])
ensure('cp', ['fcitx5-rime-data/rime-stroke/*.yaml', rime_data_install_dir])
ensure('cp', ['fcitx5-rime-data/default.yaml', rime_data_install_dir])
ensure('cp', ['-r', 'build/sysroot/usr/share/opencc', rime_data_install_dir])

Builder('rime', [
    f'-DRIME_DATA_DIR={rime_data_dir}'
]).exec()

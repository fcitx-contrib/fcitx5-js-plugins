deps=(
  glog
  json-c
  leveldb
  librime
  libthai
  marisa
  opencc
  yaml-cpp
)

EXTRACT_DIR=build/sysroot/usr
mkdir -p $EXTRACT_DIR

for dep in "${deps[@]}"; do
  file=$dep.tar.bz2
  [[ -f cache/$file ]] || wget -P cache https://github.com/fcitx-contrib/fcitx5-js-prebuilder/releases/download/latest/$file
  tar xjvf cache/$file -C $EXTRACT_DIR
done

file=fcitx5-js-dev.tar.bz2
[[ -f cache/$file ]] || wget -P cache https://github.com/fcitx-contrib/fcitx5-js/releases/download/latest/$file
tar xjvf cache/$file -C $EXTRACT_DIR

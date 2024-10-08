deps=(
  boost
  extra-cmake-modules
  glog
  json-c
  leveldb
  libime
  librime
  libthai
  marisa
  opencc
  yaml-cpp
  zstd
)

EXTRACT_DIR=build/sysroot/usr
mkdir -p $EXTRACT_DIR

# May have wrong absolute path for common deps so should appear first
file=fcitx5-js-dev.tar.bz2
[[ -f cache/$file ]] || wget -P cache https://github.com/fcitx-contrib/fcitx5-js/releases/download/latest/$file
tar xjvf cache/$file -C $EXTRACT_DIR

for dep in "${deps[@]}"; do
  file=$dep.tar.bz2
  [[ -f cache/$file ]] || wget -P cache https://github.com/fcitx-contrib/fcitx5-js-prebuilder/releases/download/latest/$file
  tar xjvf cache/$file -C $EXTRACT_DIR
done

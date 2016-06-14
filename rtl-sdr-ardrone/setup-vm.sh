#!/bin/bash
set -eu

NODE_VERSION="v0.8.15"

echo "-> Installing apt-get packages"

sudo apt-get -y install \
  build-essential \
  curl \
  git \
  cmake \
  libusb-1.0 \
  automake \
  libtool

echo "-> Installing rtl-sdr"

if [ ! -d /home/vagrant/rtl-sdr ]; then
  git clone git://git.osmocom.org/rtl-sdr.git
fi
cd rtl-sdr
# Unfortunately we can't put this into our project dir as vboxfs complains
# about hardlinks in the tar : /
echo "-> Installing code sourcer (arm toolchain)"
if [ ! -d ./armtools ]; then
  cd ~
  tarball="arm-2012.03-57-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2"
  curl -OL http://www.codesourcery.com/public/gnu_toolchain/arm-none-linux-gnueabi/${tarball}
  tar -xf ${tarball}
  mv arm-2012.03 armtools
  rm -rf ${tarball}
fi

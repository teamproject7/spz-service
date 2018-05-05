#!/usr/bin/env bash
set -e

pip install virtualenv
virtualenv -p python3 python3_venv
source python3_venv/bin/activate
pip install --trusted-host pypi.python.org -r requirements.txt


# TODO ~commands in Dockerfile
# ------------- Build & Install openalpr

# Install prerequisites
sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev
sudo apt-get install liblog4cplus-dev libcurl3-dev

# If using the daemon, install beanstalkd
sudo apt-get install beanstalkd

# Clone the latest code from GitHub
git clone https://github.com/openalpr/openalpr.git

# Setup the build directory
cd openalpr/src
mkdir build
cd build

# setup the compile environment
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..

# compile the library
make

# Install the binaries/libraries to your local system (prefix is /usr)
sudo make install


cd openalpr/src/bindings/python && python3 setup.py install

mkdir data
#!/bin/sh
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar xvf Python-3.6.9.tgz
cd Python-3.6.9
./configure --enable-optimizations --enable-shared
make -j8
sudo make altinstall
python3.6

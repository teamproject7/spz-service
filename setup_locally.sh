#!/usr/bin/env bash
set -e

pip install virtualenv
virtualenv -p python3 python3_venv
source python3_venv/bin/activate
pip install --trusted-host pypi.python.org -r requirements.txt
git clone https://github.com/openalpr/openalpr.git && cd openalpr/src/bindings/python && python3 setup.py install
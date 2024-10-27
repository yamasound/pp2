#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 factorial.py ${1} ${2}

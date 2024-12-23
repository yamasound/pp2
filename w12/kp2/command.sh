#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 json_io.py ${1} ${2} ${3} ${4} ${5} ${6} ${7} ${8} ${9} ${10}

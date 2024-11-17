#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 select_copy.py ${1} ${2}

if [ ${#} -eq 2 ]; then
    ls; tree output
fi

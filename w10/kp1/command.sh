#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 google_sheets.py ${1}

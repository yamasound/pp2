#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 drive_browser_by_selenium.py ${1}

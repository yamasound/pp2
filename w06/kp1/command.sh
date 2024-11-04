#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 scrape_by_beautiful_soup.py ${1} ${2} ${3} ${4} ${5}

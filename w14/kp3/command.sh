#!/bin/bash

url='https://www.webscrapingfordatascience.com/postform2/'
google-chrome "${url}" > /dev/null

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 fill_out_form.py ${1}

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 join_pdfs.py
evince output/all.pdf 
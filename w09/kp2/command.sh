#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 swap_rows_and_cols.py
libreoffice --nologo --calc output/swapped_texts.xlsx

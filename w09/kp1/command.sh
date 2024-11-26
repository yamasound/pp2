#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 generate_texts.py
python3 texts_to_xlsx.py
libreoffice --nologo --calc output/texts.xlsx

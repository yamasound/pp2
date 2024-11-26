#!/bin/bash

./clean.sh
mkdir output
cp input/template.xlsx output/documents.xlsx
source ~/venv/py3.10.12/bin/activate
python3 issue_documents.py
libreoffice --nologo --calc output/documents.xlsx

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 extract_phones_or_emails_on_the_clipboard.py

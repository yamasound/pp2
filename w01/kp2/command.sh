#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 make_invitation.py 
libreoffice --nologo --writer output/invitation.docx 

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 create_font_images.py
eog output/font_images.png

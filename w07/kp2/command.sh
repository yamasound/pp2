#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 add_logo_to_images.py
eog output/*

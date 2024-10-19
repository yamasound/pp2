#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 sentence_generator.py input/src.txt

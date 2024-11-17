#!/bin/bash

rm -rf output
rm -rf __pycache__
rm -f *~
python3 generate_data.py
ls; tree output

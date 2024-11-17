#!/bin/bash

rm -rf output
rm -f *~
python3 ../kp2/generate_data.py
ls; tree output

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 gather_images_from_flickr.py ${1} ${2} ${3} ${4} ${5}

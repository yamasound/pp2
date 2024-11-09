#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 create_place_cards.py
eog output/*

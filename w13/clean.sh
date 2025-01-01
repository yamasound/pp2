#!/bin/bash

rm -f *~
rm -rf ~/.streamlit

cd kp1; ./clean.sh; cd ..
cd kp2; ./clean.sh; cd ..
cd kp3; ./clean.sh; cd ..

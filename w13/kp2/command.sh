#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
if [ ${#} == '0' ]; then
    echo '[USAGE] ./command.sh program [method]'
    echo ' - program: worker.py / st_clock.py'
    echo ' - method: threading / th / multiprocessing / mp'
    echo '[SAMPLE] ./command.sh worker.py th'
elif [ ${1} == 'worker.py' ]; then
    python3 worker.py ${1} ${2}
elif [ ${1} == 'st_clock.py' ]; then
    streamlit run st_clock.py ${1} ${2}
fi

#!/bin/bash
#
USAGE='[USAGE] ./command.sh [snapshot_number]'

function save() {
    source ~/venv/py3.10.12/bin/activate
    python3 generational_snapshot.py
}

function restore() {
    i=${1}
    rm -rf output/data
    unzip output/snapshot/${i}.zip
}

if [ ${#} -eq 0 ]; then
    echo 'Saving ...'
    save
elif [ ${#} -eq 1 ]; then
    echo 'Restoring ...'
    restore ${1}
else
    echo ${USAGE}
    exit
fi
ls; tree output
echo 'Finish!'

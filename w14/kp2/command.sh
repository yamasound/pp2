#!/bin/bash

title='platformer'

source ~/venv/py3.10.12/bin/activate

f_build(){
    ./clean.sh
    mkdir -p output/${title}
    cp -r app.py output/${title}/
    cp -r app.pyxres output/${title}/
    cd output
    pyxel package ${title} ${title}/app.py
    cd ..
    rm -r output/${title}/
}

f_play(){
    pyxel play output/${title}.pyxapp
}

f_autopilot(){
    python3 autopilot.py &
}

if [ "${1}" = 'edit' ]; then
    pyxel edit app.pyxres
elif [ "${1}" = 'play' ]; then
    f_build; f_play
elif [ "${1}" = 'autopilot' ]; then
    f_build; f_autopilot; f_play
else
    echo 'USAGE: ./command.sh (play / edit / autopilot)'
    echo 'SAMPLE: ./command.sh play'
fi

#!/bin/bash

f_get_xywh() {
    f_regexp(){
        sep=${1}
        if [[ ${mes} =~ ([0-9]+)${sep}([0-9]+) ]]; then
            echo `echo ${BASH_REMATCH} | sed s/${sep}/\ /g`
        fi
    }
    mes=`xdotool search --onlyvisible --class google-chrome getwindowgeometry`
    echo "`f_regexp ,` `f_regexp x`"
}

url='https://santatracker.google.com/intl/ja/presentbounce.html'
google-chrome "${url}" > /dev/null
xywh=`f_get_xywh`

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 present_bounce.py ${xywh}

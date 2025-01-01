#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
if [ ${#} == '0' ]; then
    echo '[USAGE] ./command.sh weather_data.py'
    echo '        ./command.sh st_weather.py [method]'
    echo ' - method: threading / th / multiprocessing / mp'
    echo '[SAMPLE] ./command.sh weather_data.py'
    echo '         ./command.sh st_weather.py th'
elif [ ${1} == 'weather_data.py' ]; then
    python3 weather_data.py
elif [ ${1} == 'st_weather.py' ]; then
    streamlit run st_weather.py ${1} ${2}
fi

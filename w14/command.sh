#!/bin/bash

sudo /etc/init.d/my_iptables_off.sh
sudo apt update
sudo apt install gnome-screenshot xdotool
sudo /etc/init.d/my_iptables_on.sh

source ~/venv/py3.10.12/bin/activate
pip3 install opencv-python==4.10.0.84 pyxel==2.2.10

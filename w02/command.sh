#!/bin/bash

sudo /etc/init.d/my_iptables_off.sh
sudo apt update
sudo apt install -f xclip
sudo /etc/init.d/my_iptables_on.sh

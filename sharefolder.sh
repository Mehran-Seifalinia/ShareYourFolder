#!/bin/bash

NOCOLOR='\033[0m'
ORANGE='\033[0;33m'

echo -e "Hello, ${ORANGE}$(hostname)${NOCOLOR}\n";
sudo su<<EOF
    python3 Linux/sharefolder_installer.py 
EOF

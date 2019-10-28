#!/bin/bash

# bootstrap up to installing Python3
apt-get update
sudo su -
apt-get install nginx -y
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
cd
mkdir src
cd src
git clone https://github.com/aasquier/SRE_Fall_2019.git

# call Python script for Assignment 2
cd ~/src/SRE_Fall_2019/Automation_Scripts
python3 ./Proj2_Automation_Script.py
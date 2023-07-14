#!/bin/bash

cd

echo
echo "-------------------------------"
echo "-- Installing Python 3.11.4"
echo "--"
echo "-- this will take some time..."
echo "-------------------------------"
echo

pyenv install 3.11.4

echo
echo "-------------------------------"
echo "-- Setting env to Python 3.11.4"
echo "-------------------------------"
echo

pyenv global 3.11.4
pyenv versions

echo
echo "-------------------------------"
echo "-- Updrading PIP"
echo "-------------------------------"
echo

pip install --upgrade pip

echo
echo "-------------------------------"
echo "-- Install pigio & enable"
echo "-------------------------------"
echo

sudo apt install pigpio python-pigpio python3-pigpio -y
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

echo
echo "-------------------------------"
echo "-- Installing PySimpleGUI, pigpio, websockets & PyYAML"
echo "-------------------------------"
echo

pip install pysimplegui pigpio websockets PyYAML

echo
echo "-------------------------------"
echo "-- Rebooting in 5 seconds"
echo "--"
echo "-- Then run install_4"
echo "-------------------------------"
echo

sleep 5

sudo reboot

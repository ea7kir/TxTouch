#!/bin/bash

cd

echo
echo "-------------------------------"
echo "-- Install Pluto UDEV Rules"
echo "-------------------------------"
echo

cd
wget https://raw.githubusercontent.com/analogdevicesinc/plutosdr-fw/master/scripts/53-adi-plutosdr-usb.rules
sudo cp 53-adi-plutosdr-usb.rules /etc/udev/rules.d/

sudo udevadm control --reload-rules

rm 53-adi-plutosdr-usb.rules /etc/udev/rules.d

echo
echo "-------------------------------"
echo "-- Done"
echo "-------------------------------"
echo

echo "Clone TxTouch from within VSCODE"
echo "using: https://github.com/ea7kir/TxTouch.git"
echo
echo "To run TxTouch, type: ./txtouch"

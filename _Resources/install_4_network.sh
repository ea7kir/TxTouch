#!/bin/bash

cd

echo
echo "-------------------------------"
echo "-- Configuring the Network"
echo "-------------------------------"
echo

# #/home/pi/TxTouch/_Resources/Zz.txt
# #original /etc/network/interfaces looks like this
# #interfaces(5) file used by ifup(8) and ifdown(8)
# #Include files from /etc/network/interfaces.d:
# source /etc/network/interfaces.d/*

TXT="
auto eth1
    iface eth1 inet static
        address 192.168.3.10
        netmask 255.255.255.0
"
echo "$TXT" | sudo tee --append /etc/network/interfaces

echo
echo "-------------------------------"
echo "-- Enable port forwarding"
echo "-------------------------------"
echo

sudo sysctl net.ipv4.ip_forward # check if port forwarding is enabled

sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf # change to 1
sudo sysctl -p # confirm port forwarding is active
lsmod | grep nf # check if nftables is running as a kernel module

sudo systemctl enable nftables
sudo systemctl start nftables

echo
echo "-------------------------------"
echo "-- Continue"
echo "-------------------------------"
echo

sudo nft list ruleset # check which rules are active

sudo nft flush ruleset # to start over

sudo nft add table nat

sudo nft 'add chain nat postrouting { type nat hook postrouting priority 100 ; }'

sudo sudo nft add rule nat postrouting masquerade

sudo nft 'add chain nat prerouting { type nat hook prerouting priority -100; }'

echo
echo "-------------------------------"
echo "-- Forward the ENCODER streams to the PLUTO"
echo "-------------------------------"
echo

sudo nft add rule nat prerouting iif eth1 udp dport 7272 dnat to 192.168.2.1

sudo nft add rule nat prerouting iif eth1 udp dport 8282 dnat to 192.168.2.1

echo
echo "-------------------------------"
echo "-- Access the ENCODER from the LAN during debug/development"
echo
echo "   ie. access as: http://txtouch.local:8083"
echo "-------------------------------"
echo

sudo nft add rule nat prerouting iif eth0 tcp dport 8083 dnat to 192.168.3.1:80

echo
echo "-------------------------------"
echo "-- Access the PLUTO from the LAN during debug/development"
echo
echo "   ie. access as: http://txtouch.local:8082"
echo "-------------------------------"
echo

sudo nft add rule nat prerouting iif eth0 tcp dport 8082 dnat to 192.168.2.1:80

echo
echo "-------------------------------"
echo "-- Check the rules"
echo "-------------------------------"
echo

sudo nft list ruleset

echo
echo "-------------------------------"
echo "-- Make the rules persist"
echo "-------------------------------"
echo

sudo cp /etc/nftables.conf /etc/nftables.backup

sudo nft list ruleset | sudo tee /etc/nftables.conf

echo
echo "-------------------------------"
echo "-- NETWORK IS CONFIGURED"
echo "-------------------------------"
echo

echo
echo "-------------------------------"
echo "-- Sleep 5 seconds"
echo "--"
echo "-- Then run install_6"
echo "-------------------------------"
echo

sleep 5


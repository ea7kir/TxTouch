# IP Routing

NOTE: the DDMALL HEV-10 Encoder is set to 192.168.1.251 username/password admin/admin

## Before conguring anything.

### With the Pluto and DDMAL Encoder disconnected...

```
eth0:   192.168.1.37    the Pi local network address
lo:     127.0.0.1       P's loopback address
```

### With the Pluto and DDMAL Encoder connected...

```
eth0:   192.168.1.37    local network address
eth1:   192.168.2.10    for the Pluto on USB 0
eth2:   169.254.14.63   for the HEV-10 on USB 1
lo:     127.0.0.1       loopback address
```

- I can ping pluto.local at 192.168.2.1
- I can ssh root@pluto.local with password analog and access the file system.
    then, PlutoSDR harddisk appears on the desktop
    and mounted as /media/pi/PlutoSDR
- Pluto ifconfig has lo: 127.0.0.1 and usb0: 192.168.2.1
- Pluto can ping 192.160.2.1 and 192.168.2.10
- I can logout and login to the Pluto at will.

However:

- ping 192.168.1.251 gives "From 192.168.1.37 icmp_seq=1 Destination Host Unreachable"

Usefull command 1

```
pi@txtouch:/media/pi $ lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 003: ID 0b95:7720 ASIX Electronics Corp. AX88772
Bus 001 Device 004: ID 0456:b673 Analog Devices, Inc. PlutoSDR (ADALM-PLUTO)
Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

Usefull command 2

```
pi@txtouch:/media/pi $ dmesg | grep usb
[    0.181141] usbcore: registered new interface driver usbfs
[    0.181219] usbcore: registered new interface driver hub
[    0.181296] usbcore: registered new device driver usb
[    0.181700] usb_phy_generic phy: supply vcc not found, using dummy regulator
[    0.181910] usb_phy_generic phy: dummy supplies not allowed for exclusive requests
[    1.414166] usbcore: registered new interface driver r8152
[    1.415302] usbcore: registered new interface driver lan78xx
[    1.416508] usbcore: registered new interface driver smsc95xx
[    1.475666] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
[    1.476751] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.477797] usb usb1: Product: xHCI Host Controller
[    1.478848] usb usb1: Manufacturer: Linux 5.15.84-v8+ xhci-hcd
[    1.479911] usb usb1: SerialNumber: 0000:01:00.0
[    1.484836] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
[    1.485857] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    1.486847] usb usb2: Product: xHCI Host Controller
[    1.487865] usb usb2: Manufacturer: Linux 5.15.84-v8+ xhci-hcd
[    1.488866] usb usb2: SerialNumber: 0000:01:00.0
[    1.496312] usbcore: registered new interface driver uas
[    1.497413] usbcore: registered new interface driver usb-storage
[    1.516131] usbcore: registered new interface driver usbhid
[    1.517096] usbhid: USB HID core driver
[    1.747819] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    1.902500] usb 1-1: New USB device found, idVendor=2109, idProduct=3431, bcdDevice= 4.21
[    1.903731] usb 1-1: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[    1.905032] usb 1-1: Product: USB2.0 Hub
[    2.203832] usb 1-1.2: new high-speed USB device number 3 using xhci_hcd
[    2.317378] usb 1-1.2: New USB device found, idVendor=0b95, idProduct=7720, bcdDevice= 0.01
[    2.318537] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    2.320046] usb 1-1.2: Product: AX88772A
[    2.321343] usb 1-1.2: Manufacturer: ASIX Elec. Corp.
[    2.322444] usb 1-1.2: SerialNumber: 000387
[    2.863895] usb 1-1.1: new high-speed USB device number 4 using xhci_hcd
[    2.974350] usb 1-1.1: New USB device found, idVendor=0456, idProduct=b673, bcdDevice= 4.14
[    2.975575] usb 1-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    2.976706] usb 1-1.1: Product: PlutoSDR (ADALM-PLUTO)
[    2.977844] usb 1-1.1: Manufacturer: Analog Devices Inc.
[    2.978927] usb 1-1.1: SerialNumber: 1044734c960500031e0013003535501798
[    2.992898] usb-storage 1-1.1:1.2: USB Mass Storage device detected
[    2.994952] scsi host0: usb-storage 1-1.1:1.2
[    6.731538] usbcore: registered new interface driver brcmfmac
[    8.328586] usbcore: registered new interface driver cdc_ether
[    8.392559] rndis_host 1-1.1:1.0 eth1: register 'rndis_host' at usb-0000:01:00.0-1.1, RNDIS device, 00:e0:22:6f:28:9a
[    8.392824] usbcore: registered new interface driver rndis_host
[    8.418415] usbcore: registered new interface driver rndis_wlan
[    8.451255] usbcore: registered new interface driver cdc_acm
[    9.193625] Asix Electronics AX88772A usb-001:003:10: attached PHY driver (mii_bus:phy_addr=usb-001:003:10, irq=POLL)
[    9.194646] asix 1-1.2:1.0 eth2: register 'asix' at usb-0000:01:00.0-1.2, ASIX AX88772 USB 2.0 Ethernet, 00:0e:c6:75:b5:c7
[    9.194918] usbcore: registered new interface driver asix
```

Usefull command 3

```
pi@txtouch:/media/pi $ usb-devices

T:  Bus=01 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=480 MxCh= 1
D:  Ver= 2.00 Cls=09(hub  ) Sub=00 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=1d6b ProdID=0002 Rev=05.15
S:  Manufacturer=Linux 5.15.84-v8+ xhci-hcd
S:  Product=xHCI Host Controller
S:  SerialNumber=0000:01:00.0
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub

T:  Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  2 Spd=480 MxCh= 4
D:  Ver= 2.10 Cls=09(hub  ) Sub=00 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=2109 ProdID=3431 Rev=04.21
S:  Product=USB2.0 Hub
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=100mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub

T:  Bus=01 Lev=02 Prnt=02 Port=00 Cnt=01 Dev#=  4 Spd=480 MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=0456 ProdID=b673 Rev=04.14
S:  Manufacturer=Analog Devices Inc.
S:  Product=PlutoSDR (ADALM-PLUTO)
S:  SerialNumber=1044734c960500031e0013003535501798
C:  #Ifs= 6 Cfg#= 1 Atr=80 MxPwr=500mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=02(commc) Sub=02 Prot=ff Driver=rndis_host
I:  If#=0x1 Alt= 0 #EPs= 2 Cls=0a(data ) Sub=00 Prot=00 Driver=rndis_host
I:  If#=0x2 Alt= 0 #EPs= 2 Cls=08(stor.) Sub=06 Prot=50 Driver=usb-storage
I:  If#=0x3 Alt= 0 #EPs= 1 Cls=02(commc) Sub=02 Prot=01 Driver=cdc_acm
I:  If#=0x4 Alt= 0 #EPs= 2 Cls=0a(data ) Sub=00 Prot=00 Driver=cdc_acm
I:  If#=0x5 Alt= 0 #EPs= 6 Cls=02(commc) Sub=00 Prot=00 Driver=(none)

T:  Bus=01 Lev=02 Prnt=02 Port=01 Cnt=02 Dev#=  3 Spd=480 MxCh= 0
D:  Ver= 2.00 Cls=ff(vend.) Sub=ff Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=0b95 ProdID=7720 Rev=00.01
S:  Manufacturer=ASIX Elec. Corp.
S:  Product=AX88772A
S:  SerialNumber=000387
C:  #Ifs= 1 Cfg#= 1 Atr=a0 MxPwr=250mA
I:  If#=0x0 Alt= 0 #EPs= 3 Cls=ff(vend.) Sub=ff Prot=00 Driver=asix

T:  Bus=02 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=5000 MxCh= 4
D:  Ver= 3.00 Cls=09(hub  ) Sub=00 Prot=03 MxPS= 9 #Cfgs=  1
P:  Vendor=1d6b ProdID=0003 Rev=05.15
S:  Manufacturer=Linux 5.15.84-v8+ xhci-hcd
S:  Product=xHCI Host Controller
S:  SerialNumber=0000:01:00.0
C:  #Ifs= 1 Cfg#= 1 Atr=e0 MxPwr=0mA
I:  If#=0x0 Alt= 0 #EPs= 1 Cls=09(hub  ) Sub=00 Prot=00 Driver=hub
```


import subprocess
#import sys

def configure_pluto():
    pass

def shutdown_pluto():
    pass

"""
In the Pluto the file /www/settings.txt contains:

callsign EA7KIR
freq 2409.75
mode DVBS2
mod QPSK
sr 333
fec 34
pilots Off
frame LongFrame
power -2
rolloff 0.25
pcrpts 800
patperiod 200
h265box undefined
remux 1
"""

def setup_pluto(args):
    # stop_pluto()
#########    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
#########    cmd_str = '{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
#########        args.url,
#########        args.frequency,
#########        args.mode,
#########        args.constellation,
#########        args.symbol_rate,
#########        args.fec,
#########        args.gain,
#########        args.calibration_mode,
#########        args.pcr_pts_delay,
#########        args.audio_bit_rate,
#########        args.provider)
#########    # TODO: send to pluto
#########    # start_pluto()
#########    print(f'PLUTO -> {cmd_str}')
    tmp_h265box = 'undefined'
    tmp_remux = '1'
    settings = 'callsign {}\nfreq {}\nmode {}\nmod {}\nsr {}\nfec {}\npilots {}\nframe {}\npower {}\nrolloff {}\npcrpts {}\npatperiod {}\nh265box {}\nremux {}\n\n'.format(
        args.provider,
        args.frequency,
        args.mode,
        args.constellation,
        args.symbol_rate,
        args.fec,
        args.pilots,
        args.frame,
        args.gain,
        args.roll_off,
        args.pcr_pts,
        args.pat_period,
        tmp_h265box,
        tmp_remux)
    #print(settings)
    f = open("/home/pi/settings.txt", "w")
    f.write(settings)
    f.close()
    """
    See: https://wiki.analog.com/university/tools/pluto/drivers/linux

    sudo apt install libiio-utils

    iio_info -n 192.168.2.1 | grep device

    io_readdev -n 192.168.2.1 -s 64 cf-ad9361-lpc | hexdump -x

    AND FOR PASSWORDS:

    wget https://raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/ssh_config -O ~/.ssh/config

    sudo apt install sshpass

    Now I can ssh and scp like this...

    sshpass -panalog ssh root@pluto.local

    sshpass -panalog ssh root@192.168.2.1 # not working

    sshpass -panalog scp /home/pi/settings.txt root@pluto.local:/www/

    sshpass -panalog scp /home/pi/settings.txt root@192.168.2.1:/www/  # not working

    """
    result = subprocess.run(['sshpass', '-panalog', 'scp', '/home/pi/settings.txt', 'root@pluto.local:/www/'])
    if result.returncode != 0:
        print('ERROR updating pluto settings.txt')
    # start_pluto()


import subprocess
import sys

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

ssh root@pluto.local (pwd analog) and updating this file appears to work.

OR:

write to a file and copy to Pluto with scp

scp settings.txt root@pluto.local:/www/

To make this work I need to eliminate the need for ssh paswords

I don't think its possible to copy to /www/ using the mas-storage-device
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
    print(settings)
    # TODO: send this to /home/pi/settings.txt and scp /home/pi/settings.txt root@pluto.local:/www/
    f = open("/home/pi/settings.txt", "w")
    f.write(settings)
    f.close()
    # scp /home/pi/settings.txt root@pluto.local:/www/
    #result = subprocess.run([sys.executable, "-c", "/usr/bin/scp /home/pi/settings.txt root@pluto.local:/www/"])
    # start_pluto()

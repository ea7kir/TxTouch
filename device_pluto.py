# TODO: network access to Pluto

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
    a = f'callsign {args.provider}\n'
    b = f'freq {args.frequency}\n'
    c = f'mode {args.mode}\n'
    d = f'mod {args.constellation}\n'
    e = f'sr {args.symbol_rate}\n'
    f = f'fec {args.fec}\n'
    g = f'pilots {args.pilots}\n'
    h = f'frame {args.frame}\n'
    i = f'power {args.gain}\n'
    j = f'rolloff {args.roll_off}\n'
    k = f'pcrpts {args.pcr_pts}\n'
    l = f'patperiod {args.pat_period}\n'
    m = f'h265box {tmp_h265box}\n'
    n = f'remux {tmp_remux}\n\n'
    txt = a + b + c + d + e + f + g + h + i + j + k + l + m + n
    print(txt)
    # TODO: send to pluto
    # start_pluto()



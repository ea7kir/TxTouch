from device_constants import PLUTO_ADDRESS

# TODO: network access to Pluto

def configure_pluto():
    pass

def shutdown_pluto():
    pass

#class PlutoArgs:
#    frequency = None
#    symbol_rate = None
#    mode = None
#    constellation = None
#    fec = None
#    provider = None
#    service = None
#    gain = None

def setup_pluto(plu):
    print(f'PLUTO frequency: {plu.frequency}, symbol_rate: {plu.symbol_rate}')
    pass

# TODO: rename some of these to match current names

#class PlutoArgs:
#    frequency = None           # '2409.75'
#    mode = None                # 'DBS2'
#    constellation = None       # 'QPSK'
#    rate = None                # '333'
#    fec = None                 # '23'
#    gain = None                # '-10'
#    calibration_mode = None    # 'nocalib'
#    pcr_pts_delay = None       # '800'
#    audio_bit_rate = None      # '32'
#    provider = None            # 'EA7KIR'
#    service = None             # 'Malaga'

#def start_pluto(plu):
#    # stop_pluto()
#    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
#    cmd_str = 'rtmp://{}:{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
#        plu.ip,
#        plu.port,
#        plu.frequency,
#        plu.mode,
#        plu.constellation,
#        plu.symbol_rate,
#        plu.fec,
#        plu.gain,
#        plu.calibration_mode,
#        plu.pcr_pts_delay,
#        plu.audio_bit_rate,
#        plu.provider)
#    # TODO: send to pluto
#    # start_pluto()
#    print(cmd_str)


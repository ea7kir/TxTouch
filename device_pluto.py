from device_constants import PLUTO_ADDRESS

# TODO: network access to Pluto

def configure_pluto():
    pass

def shutdown_pluto():
    pass

class PlutoArgs:
    port = None                     # '8282' or '7272'
    frequency = None                # '2409.75'
    mode = None                     # 'DBS2'
    constellation = None            # 'QPSK'
    symbol_rate = None              # '333'
    fec = None                      # '23' from '2/3'
    gain = None                     # '-10'
    calibration_mode = 'nocalib'    # NOTE: not implemented
    pcr_pts_delay = '800'           # NOTE: not implemented
    audio_bit_rate = '32'           # NOTE: not implemented
    provider = None                 # 'EA7KIR'
    service = None                  # 'Malaga'

def setup_pluto(plu):
    # stop_pluto()
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
    cmd_str = 'rtmp://{}:{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
        PLUTO_ADDRESS,
        plu.port,
        plu.frequency,
        plu.mode,
        plu.constellation,
        plu.symbol_rate,
        plu.fec,
        plu.gain,
        plu.calibration_mode,
        plu.pcr_pts_delay,
        plu.audio_bit_rate,
        plu.provider)
    # TODO: send to pluto
    # start_pluto()
    print(f'\nPLUTO -> {cmd_str}\n')


# TODO: network access to Pluto

def configure_pluto():
    pass

def shutdown_pluto():
    pass

class PlutoArgs:
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
    url = None                      #

def setup_pluto(args):
    # stop_pluto()
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
    cmd_str = '{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
        args.url,
        args.frequency,
        args.mode,
        args.constellation,
        args.symbol_rate,
        args.fec,
        args.gain,
        args.calibration_mode,
        args.pcr_pts_delay,
        args.audio_bit_rate,
        args.provider)
    # TODO: send to pluto
    # start_pluto()
    print(f'PLUTO -> {cmd_str}')


from device_constants import PLUTO_ADDRESS

# TODO: network access to Pluto

def configure_pluto():
    pass

def shutdown_pluto():
    pass

#class TuneArgs:
#    frequency = ''
#    symbol_rate = ''
#    mode = ''
#    constellation = ''
#    fec = ''
#    provider = ''
#    service = ''
#    gain = ''

def setup_pluto(plu):
    print(f'PLUTO frequency: {plu.frequency}, symbol_rate: {plu.symbol_rate}')
    pass

############################################################################ begin pluto data#

#class PlutoData:
#    def __init__(self):
#        # TODO: note these are just example values
#        self.ip:str = '000.000.000.000',
#        self.port:int = 8282,
#        self.frequency:str = '2409.75',
#        self.mode:str = 'DBS2',
#        self.constellation:str = 'QPSK',
#        self.rate:str = '333',
#        self.fec:str = '23',
#        self.gain:str = '-10',
#        self.calibration_mode:str = 'nocalib',
#        self.pcr_pts_delay:str = '800',
#        self.audio_bit_rate:str = '32',
#        self.provider:str = 'EA7KIR',
#        self.service:str = 'Malaga',
#        self.pluto_running: bool = False#

#pluto_data = PlutoData()#

#def start_pluto():
#    stop_pluto()
#    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
#    cmd_str = 'rtmp://{}:{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
#        pluto_data.ip,
#        pluto_data.port,
#        pluto_data.frequency,
#        pluto_data.mode,
#        pluto_data.constellation,
#        pluto_data.symbol_rate,
#        pluto_data.fec,
#        pluto_data.gain,
#        pluto_data.calibration_mode,
#        pluto_data.pcr_pts_delay,
#        pluto_data.audio_bit_rate,
#        pluto_data.provider)
#    # TODO: send to pluto
#    print(cmd_str)
#    pluto_data.pluto_running = True#

############################################################################ end pluto data


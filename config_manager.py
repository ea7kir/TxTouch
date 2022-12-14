# config_manager.py

import yaml

CONFIG_FILE = 'config.yaml'

FACTORY_encoder_ip = '192.168.1.000'
FACTORY_encoder_port = '0000'
FACTORY_pluto_ip = '192.168.2.1'
FACTORY_pluto_port = '7272' # [ ???? | 7272 ]
FACTORY_frequency = '2409.75 / 27'
FACTORY_mode = 'DVBS2'
FACTORY_constellation = 'QPSK'
FACTORY_symbol_rate = '333'
FACTORY_fec = '3/4'
FACTORY_gain = '-10'
FACTORY_calibration_mode = 'nocalib' # [ calib | nocalib ] force a calibration process (high spike) with calib
FACTORY_pcr_pts_delay = '800' # [ 100...2000 ] default 600. If encoding suffers from underflow, increase this
# Audio transcoding bitrate. Audio bitrate from OBS could not go down below 64kbit, this is used to workaround that
FACTORY_audio_bit_rate = '32' # [ 32 | 64 ]
FACTORY_provider = 'PROVIDER'   
FACTORY_service = 'SERVICE'

class ConfigManager():
    def __init__(self):
        self.encoder_ip = FACTORY_encoder_ip
        self.encoder_port = FACTORY_encoder_port
        self.pluto_ip = FACTORY_pluto_ip
        self.pluto_port = FACTORY_pluto_port
        self.frequency = FACTORY_frequency
        self.mode = FACTORY_mode
        self.constellation = FACTORY_constellation
        self.symbol_rate = FACTORY_symbol_rate
        self.fec = FACTORY_fec
        self.gain = FACTORY_gain
        self.calibration_mode = FACTORY_calibration_mode
        self.pcr_pts_delay = FACTORY_pcr_pts_delay
        self.audio_bit_rate = FACTORY_audio_bit_rate
        self.provider = FACTORY_provider   
        self.service = FACTORY_service
        self.read_config()
        
    def read_config(self):
        try:
            with open(CONFIG_FILE) as f:
                data = yaml.load(f, Loader = yaml.FullLoader)
                self.encoder_ip = data['encoder_ip']
                self.encoder_port = data['encoder_port']
                self.pluto_ip = data['pluto_ip']
                self.pluto_port = data['pluto_port']
                self.frequency = data['frequency']
                self.mode = data['mode']
                self.constellation = data['constellation']
                self.symbol_rate = data['symbol_rate']
                self.fec = data['fec']
                self.gain = data['gain']
                self.calibration_mode = data['calibration_mode']
                self.pcr_pts_delay = data['pcr_pts_delay']
                self.audio_bit_rate = data['audio_bit_rate']
                self.provider = data['provider']   
                self.service = data['service']
        except:
            self.write_config()
    
    def write_config(self):
        data = {
            'encoder_ip': self.encoder_ip,
            'encoder_port': self.encoder_port,
            'pluto_ip': self.pluto_ip,
            'pluto_port': self.pluto_port,
            'frequency': self.frequency,
            'mode': self.mode,
            'constellation': self.constellation,
            'symbol_rate': self.symbol_rate,
            'fec': self.fec,
            'gain': self.gain,
            'calibration_mode': self.calibration_mode,
            'pcr_pts_delay': self.pcr_pts_delay,
            'audio_bit_rate': self.audio_bit_rate,
            'provider': self.provider,
            'service': self.service,
        }
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(data, f)
           

config = ConfigManager()

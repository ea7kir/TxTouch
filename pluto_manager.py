# pluto_manager

from config_manager import config

class PlutoManager():
    def __init__(self):
        self.running = False
        self.status_msg: str = ''
        self.status_changed = False
        self.ptt_is_on = False
        
    def send_to_pluto(self, cmd_str):
        pass
        
    # Eg: "rtmp://192.168.1.40:7272/,2409.75,DVBS2,QPSK,333,23,-2,nocalib,800,32,/,EA7KIR,"
    
    def start_ptt(self,
            frequency,
            mode,
            constellation,
            symbol_rate,
            fec,
            gain,
            calibration_mode,
            pcr_pts_delay,
            audio_bit_rate,
            provider,
            service):
        cmd_str = 'rtmp://{}:{}/,{},{},{},{},{},{},{},{},{},/,{}'.format(
            config.pluto_ip,
            config.pluto_port,
            frequency,
            mode,
            constellation,
            symbol_rate,
            fec,
            gain,
            calibration_mode,
            pcr_pts_delay,
            audio_bit_rate,
            provider)
        self.send_to_pluto(cmd_str)
        self.ptt_is_on = True
        self.status_msg = '{}'.format(cmd_str)
        self.status_changed = True
    
    def stop_ptt(self):
        self.ptt_is_on = False
        self.status_msg = ''
        self.status_changed = True
        
    
pluto_manager = PlutoManager()
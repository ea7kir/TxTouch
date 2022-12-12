# pluto_manager

class PlutoManager():
    def __init__(self):
        self.running = False
        self.status_msg: str = ''
        self.status_changed = False
        self.ptt_is_on = False
        
    def start_ptt(self, frequency, symbol_rate):
        self.ptt_is_on = True
        self.status_msg = 'pluto ptt {} {}'.format(frequency, symbol_rate)
        self.status_changed = True
    
    def stop_ptt(self):
        self.ptt_is_on = False
        self.status_msg = ''
        self.status_changed = True
    
pluto_manager = PlutoManager()
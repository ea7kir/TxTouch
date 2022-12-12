# pluto_manager

class PlutoManager():
    def __init__(self):
        self.running = False
        self.status_msg: str = ''
        
    def start_ptt(self, frequency, symbol_rate):
        self.status_msg = 'pluto ptt {} {}'.format(frequency, symbol_rate)
    
    def stop_ptt(self):
        self.status_msg = ''
    
pluto_manager = PlutoManager()
import random # ONLY NEEDED TO SIMULATE DATA VALUES DURING DEVELOPMENT
from time import sleep # ONLY NEEDED TO SIMULATE FETCH TIMES DURING DEVELOPMENT

class RoofData:
    def __init__(self):
        self.preamp_temp:str = ''
        self.pa_temp:str = ''
        self.pa_current:str = ''
        self.fans:str = ''

def process_read_roof_data(send_roof_data):
    roof_data = RoofData()
    IP = '000.000.000.000'
    PORT = 0
    while True:
        sleep(1.0)
        roof_data.preamp_temp = f'{random.randint(30, 39)} °C'
        roof_data.pa_temp:str = f'{random.randint(30, 39)} °C'
        roof_data.pa_current:str = f'{random.randint(6, 7)} Amps'
        roof_data.fans:str = 'OK'
        send_roof_data.send(roof_data)


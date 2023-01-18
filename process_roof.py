import random # ONLY NEEDED TO SIMULATE DATA VALUES DURING DEVELOPMENT
from time import sleep # ONLY NEEDED TO SIMULATE FETCH TIMES DURING DEVELOPMENT

from read_temperature_sensors import read_pa_temperature, read_preamp_temperature
from read_fan_status import read_fan_status
from read_current_sensor import read_pa_current

class RoofData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''
    connected: bool = False


def process_read_roof_data(roof2):
    IP = '000.000.000.000' # roof.local
    PORT = 0 # whatever

    roof_data = RoofData()


    while True:

        if roof2.poll():
            cmd = roof2.recv()
            if cmd == 'STOP':
                # close the connection
                roof_data.connected = False
            else:
                # open the connection
                roof_data.connected = True

        roof_data.connected = True # temporary fix til I implement the connection

        if roof_data.connected:

            roof_data.preamp_temp = read_preamp_temperature()
            roof_data.pa_temp:str = read_pa_temperature()
            roof_data.pa_current:str = read_pa_current()
            roof_data.fans = read_fan_status()
            roof2.send(roof_data)
            sleep(0.5)

        else:

            roof_data.preamp_temp = '-'
            roof_data.pa_temp:str = '-'
            roof_data.pa_current:str = '-'
            roof_data.fans:str = '-'
            roof2.send(roof_data)
            sleep(0.5)
  



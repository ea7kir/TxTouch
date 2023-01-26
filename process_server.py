import random # ONLY NEEDED TO SIMULATE DATA VALUES DURING DEVELOPMENT
from time import sleep # ONLY NEEDED TO SIMULATE FETCH TIMES DURING DEVELOPMENT

from read_temperature_sensors import read_pa_temperature, read_preamp_temperature
from read_fan_status import read_fan_status
from read_current_sensor import read_pa_current

class ServerData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''
    connected: bool = False


def process_read_server_data(roof2):
    IP = '000.000.000.000' # roof.local
    PORT = 0 # whatever

    server_data = ServerData()


    while True:

        if roof2.poll():
            cmd = roof2.recv()
            if cmd == 'STOP':
                # close the connection
                server_data.connected = False
            else:
                # open the connection
                server_data.connected = True

        server_data.connected = True # temporary fix til I implement the connection

        if server_data.connected:

            server_data.preamp_temp = read_preamp_temperature()
            server_data.pa_temp:str = read_pa_temperature()
            server_data.pa_current:str = read_pa_current()
            server_data.fans = read_fan_status()
            roof2.send(server_data)
            sleep(0.5)

        else:

            server_data.preamp_temp = '-'
            server_data.pa_temp:str = '-'
            server_data.pa_current:str = '-'
            server_data.fans:str = '-'
            roof2.send(server_data)
            sleep(0.5)
  



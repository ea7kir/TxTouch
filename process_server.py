from time import sleep # ONLY NEEDED TO SIMULATE FETCH TIMES DURING DEVELOPMENT

SERVER = 'txserver.local'
PORT = 8765

class ServerData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''

def process_read_server_data(pipe):

    server_data = ServerData()

    while True:

        connected = False # temporary fix til I implement the connection

        if connected:

            pass # async client goes here

        else:

            server_data.preamp_temp = '-'
            server_data.pa_temp:str = '-'
            server_data.pa_current:str = '-'
            server_data.fans:str = '-'
            pipe.send(server_data)
            sleep(1)
  



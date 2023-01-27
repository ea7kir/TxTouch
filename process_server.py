from time import sleep # ONLY NEEDED TO SIMULATE FETCH TIMES DURING DEVELOPMENT

SERVER = 'txserver.local'
PORT = 8765

class ServerData:
    preamp_temp = '-'
    pa_temp = '-'
    pa_current = '-'
    fans = '-'

def process_read_server_data(pipe):
    connected = False
    server_data = ServerData()
    while True:
        if connected:
            pass # async client goes here
        else:
            pipe.send(server_data)
            sleep(1)
  



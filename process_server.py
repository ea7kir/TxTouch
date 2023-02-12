import asyncio
import json
from time import sleep

from device_constants import TX_SERVER_ADDRESS, TX_SERVER_PORT

class ServerData:
    preamp_temp = '-'
    pa_temp = '-'
    pa_current = '-'
    fans = '-'

def process_read_server_data(pipe):
    # developed from "TCP echo client using streams"
    # https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-client-using-streams

    async def client():
        try:
            reader, writer = await asyncio.open_connection(TX_SERVER_ADDRESS, TX_SERVER_PORT)
            print(f'Connected to {TX_SERVER_ADDRESS}:{TX_SERVER_PORT}', flush=True)
        except:
            print(f'Failed to connected to {TX_SERVER_ADDRESS}:{TX_SERVER_PORT}. Server unavailable', flush=True)

        server_data = ServerData()
        while True:
            try:
                json_dict_raw = await reader.read(1024)
                json_dict = json_dict_raw.decode()
                data_dict = json.loads(json_dict)
                server_data.preamp_temp = data_dict['preamp_temp']
                server_data.pa_temp = data_dict['pa_temp']
                server_data.pa_current = data_dict['pa_current']
                server_data.fans = data_dict['fans']
                pipe.send(server_data)
                sleep(0)
            except:
                print(f'Connection to {TX_SERVER_ADDRESS}:{TX_SERVER_PORT}. Failed during transfer', flush=True)
                break

        server_data = ServerData()
        pipe.send(server_data)
        while True:
            sleep(1.0) # keep the process running

    asyncio.run(client())

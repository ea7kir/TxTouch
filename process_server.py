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
            connected = True
        except:
            msg = f'Failed to connected to {TX_SERVER_ADDRESS}:{TX_SERVER_PORT}. Server unavailable'
            print(msg, flush=True)
            connected = False#
        server_data = ServerData()
        while connected:
            try:
                # received = str(sock.recv(1024), "utf-8")
                raw_data = await reader.read(128) # normally 72 bytes
                #print(len(raw_data), flush=True)
                server_data = str(raw_data, "utf-8")
                #print(f'>{server_data}<', flush=True)
                pipe.send(server_data)

                #json_dict_raw = await reader.read(128) # normally 100 bytes
                #json_dict = json_dict_raw.decode()
                #data_dict = json.loads(json_dict)
                #server_data.preamp_temp = data_dict['preamp_temp']
                #server_data.pa_temp = data_dict['pa_temp']
                #server_data.pa_current = data_dict['pa_current']
                #server_data.fans = data_dict['fans']
                #pipe.send(server_data)
            except:
                msg = f'Connection to {TX_SERVER_ADDRESS}:{TX_SERVER_PORT}. Failed during transfer'
                print(msg, flush=True)
                connected = False
                break

        server_data = ServerData()
        pipe.send(server_data)
        while True:
            sleep(1.0) # keep the process running

    asyncio.run(client())

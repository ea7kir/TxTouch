import asyncio
import json

SERVER = 'roof.local'
PORT = 8765

class ServerData:
    preamp_temp:str = '-'
    pa_temp: str = '-'
    pa_current: str = '-'
    fans: str = '-'

async def consume(server_data):
    print(f'server_data.preamp_temp : {server_data.preamp_temp}', flush=True)
    print(f'server_data.pa_temp     : {server_data.pa_temp}', flush=True)
    print(f'server_data.pa_current  : {server_data.pa_current}', flush=True)
    print(f'server_data.fans        : {server_data.fans}', flush=True)
    print('-------------------------------------', flush=True)

# developed from "TCP echo server using streams"
# https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-client-using-streams

async def client():
    try:
        reader, writer = await asyncio.open_connection(SERVER, PORT)
        print('Connected to server', flush=True)
    except IOError as e:
        print(f'EXCEPTION 1 {e}', flush=True)
        return
        if e != 'connected':
            print('Server is unavaliable', flush=True)
            print(f'EXCEPTION 1 {e}', flush=True)
            return    

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
            #server_data.connected = data_dict['connected']
            await consume(server_data)
        # TODO: this exception isn't working as I wish, or not at all!
        except IOError as e:
            print(f'EXCEPTION 2 {e}', flush=True)
            break
            if e != 'connected':
                print(f'EXCEPTION 2 {e}', flush=True)
                break

    server_data = ServerData()
    consume(server_data)

asyncio.run(client())

#process_read_server_data(999)

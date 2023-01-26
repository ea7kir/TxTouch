import asyncio
import json

SERVER = 'roof.local'
PORT = 8765

class RoofData:
    preamp_temp:str = '-'
    pa_temp: str = '-'
    pa_current: str = '-'
    fans: str = '-'
    #connected: bool = False

async def consume(roof_data):
    print(f'roof_data.preamp_temp : {roof_data.preamp_temp}', flush=True)
    print(f'roof_data.pa_temp     : {roof_data.pa_temp}', flush=True)
    print(f'roof_data.pa_current  : {roof_data.pa_current}', flush=True)
    print(f'roof_data.fans        : {roof_data.fans}', flush=True)
    #print(f'roof_data.connected   : {roof_data.connected}', flush=True)
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

    roof_data = RoofData()
    while True:
        try:
            json_dict_raw = await reader.read(1024)
            json_dict = json_dict_raw.decode()
            data_dict = json.loads(json_dict)
            roof_data.preamp_temp = data_dict['preamp_temp']
            roof_data.pa_temp = data_dict['pa_temp']
            roof_data.pa_current = data_dict['pa_current']
            roof_data.fans = data_dict['fans']
            #roof_data.connected = data_dict['connected']
            await consume(roof_data)
        except IOError as e:
            print(f'EXCEPTION 2 {e}', flush=True)
            break
            if e != 'connected':
                print(f'EXCEPTION 2 {e}', flush=True)
                break

    roof_data = RoofData()
    consume(roof_data)

asyncio.run(client())

#process_read_roof_data(999)

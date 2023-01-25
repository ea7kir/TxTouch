import asyncio
import json

SERVER = 'roof.local'
PORT = 8765

class RoofData:
    preamp_temp:str = '-'
    pa_temp: str = '-'
    pa_current: str = '-'
    fans: str = '-'
    connected: bool = False

def consume(roof_data):
    print(f'roof_data.preamp_temp : {roof_data.preamp_temp}', flush=True)
    print(f'roof_data.pa_temp     : {roof_data.pa_temp}', flush=True)
    print(f'roof_data.pa_current  : {roof_data.pa_current}', flush=True)
    print(f'roof_data.fans        : {roof_data.fans}', flush=True)
    print(f'roof_data.connected   : {roof_data.connected}', flush=True)
    print('-------------------------------------', flush=True)

# developed from "TCP echo server using streams"
# https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-client-using-streams

async def client():
    try:
        reader, writer = await asyncio.open_connection(SERVER, PORT)
        print('CONNECTED TO SERVER', flush=True)
        roof_data = RoofData()
        while True:
            try:
                data_in = await reader.read(1024)
                data_str = data_in.decode()
                data = json.loads(data_str)
                roof_data.preamp_temp = data['preamp_temp']
                roof_data.pa_temp = data['pa_temp']
                roof_data.pa_current = data['pa_current']
                roof_data.fans = data['fans']
                roof_data.connected = data['connected']
                consume(roof_data)
            except:
                break
        print('Close the connection', flush=True)
        writer.close()
    except:
        print('Server is unavaliable', flush=True)

    roof_data = RoofData()
    consume(roof_data)

asyncio.run(client())

#process_read_roof_data(999)

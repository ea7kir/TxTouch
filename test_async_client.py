import asyncio
import json

SERVER = 'roof.local'
PORT = 8765

class RoofData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''
    connected: bool = False

def consume(roof_data):
    print(f'roof_data.preamp_temp : {roof_data.preamp_temp}', flush=True)
    print(f'roof_data.pa_temp     : {roof_data.pa_temp}', flush=True)
    print(f'roof_data.pa_current  : {roof_data.pa_current}', flush=True)
    print(f'roof_data.fans        : {roof_data.fans}', flush=True)
    print(f'roof_data.connected   : {roof_data.connected}', flush=True)
    print('-------------------------------------', flush=True)

async def client():
    reader, writer = await asyncio.open_connection(SERVER, PORT)
    print('CONNECTED', flush=True)
    roof_data = RoofData()
    while True:
        data_in = await reader.read(1024)
        data_str = data_in.decode()
        data = json.loads(data_str)
        roof_data.preamp_temp = data['preamp_temp']
        roof_data.pa_temp = data['pa_temp']
        roof_data.pa_current = data['pa_current']
        roof_data.fans = data['fans']
        roof_data.connected = data['connected']
        consume(roof_data)

    print('Close the connection', flush=True)
    writer.close()

asyncio.run(client())

#process_read_roof_data(999)

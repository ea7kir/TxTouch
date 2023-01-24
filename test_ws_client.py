import asyncio
import websockets
import pickle

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# can also test $ python -m websockets ws://roof.local:8765/

class RoofData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''
    connected: bool = False

async def consume(roof_data):
    print(f'roof_data.preamp_temp : {roof_data.preamp_temp}')
    print(f'roof_data.pa_temp     : {roof_data.pa_temp}')
    print(f'roof_data.pa_current  : {roof_data.pa_current}')
    print(f'roof_data.fans        : {roof_data.fans}')
    print(f'roof_data.connected   : {roof_data.connected}')
    print('-------------------------------------')

def process_read_roof_data(connection):
    async def handle():
        url = f'ws://{SERVER}:{PORT}/'
        try:
            async with websockets.connect(url) as websocket:
                print('CONNECTED', flush=True)
                roof_data = RoofData()
                while True:
                    recvd_data = await websocket.recv()
                    roof_data = pickle.loads(recvd_data)
                    await consume(roof_data)
        except websockets.exceptions.ConnectionClosedError as e:
            print('EXCEPTION: ConnectionClosedError', flush=True)
            print(e)
            return

    asyncio.run(handle())

process_read_roof_data(999)

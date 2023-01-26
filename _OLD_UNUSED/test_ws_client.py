import asyncio
import websockets
import pickle

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# can also test $ python -m websockets ws://roof.local:8765/

class ServerData:
    preamp_temp:str = ''
    pa_temp: str = ''
    pa_current: str = ''
    fans: str = ''
    connected: bool = False

async def consume(server_data):
    print(f'server_data.preamp_temp : {server_data.preamp_temp}')
    print(f'server_data.pa_temp     : {server_data.pa_temp}')
    print(f'server_data.pa_current  : {server_data.pa_current}')
    print(f'server_data.fans        : {server_data.fans}')
    print(f'server_data.connected   : {server_data.connected}')
    print('-------------------------------------')

def process_read_server_data(connection):
    async def handle():
        url = f'ws://{SERVER}:{PORT}/'
        try:
            async with websockets.connect(url) as websocket:
                print('CONNECTED', flush=True)
                server_data = ServerData()
                while True:
                    recvd_data = await websocket.recv()
                    server_data = pickle.loads(recvd_data)
                    await consume(server_data)
        except websockets.exceptions.ConnectionClosedError as e:
            print('EXCEPTION: ConnectionClosedError', flush=True)
            print(e)
            return

    asyncio.run(handle())

process_read_server_data(999)

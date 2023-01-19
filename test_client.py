import asyncio
import websockets
import pickle

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# can also test $ python -m websockets ws://roof.local:8765/

class RoofData:
    counter = 0
    connected = False

def consumer(roof_data):
    print(roof_data.counter)

def process_read_roof_data(connection):
    async def handle():
        url = f'ws://{SERVER}:{PORT}/'
        try:
            async with websockets.connect(url) as websocket:
                print('connected', flush=True)
                #connected = True
                while True:
                    message = 'PTT'
                    has_message = False
                    if has_message:
                        match message:
                            case 'CLOSE':
                                return
                            case 'PTT':
                                await websocket.send('PTT')
                    else:
                        await websocket.send('ACK')

                    data = await websocket.recv() # TODO: JSON
                    roof_data = pickle.loads(data)
                    consumer(roof_data)
                    await websocket.pong(data=b'')
        except:
            print('not connected', flush=True)
            #connected = False
            #await websocket.close()
            return

    asyncio.run(handle())

process_read_roof_data(999)

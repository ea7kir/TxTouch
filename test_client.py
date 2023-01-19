import asyncio
import websockets
import json

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# can also test $ python -m websockets ws://roof.local:8765/

class RoofData:
    counter = 0
    connected = False
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

#roof_data = RoofData()

d = {"connected": True, "counter": 1}
print(d, d['counter'], d['connected'])
#exit(0)
def process_read_roof_data(connection):
    #roof_data = RoofData()
    async def handle():
        roof_data = RoofData()
        url = f'ws://{SERVER}:{PORT}/'
        try:
            async with websockets.connect(url) as websocket:
                print('connected', flush=True)
                roof_data.connected = True
                # NOT REQUIRED - roof_data = RoofData()
                while True:
                    # if message to send
                    has_message = True
                    if has_message:
                        message = 'PTT'
                        await websocket.send(message)

                    data = await websocket.recv() # TODO: JSON
                    data_dict = json.loads(data)
                    print(data_dict, flush=True)
                    roof_data.counter = data_dict['counter']
                    roof_data.connected = data_dict['connected']
                    print(roof_data.connected, roof_data.counter, flush=True)
        except: 
            print('not connected', flush=True)
            roof_data.connected = False

    asyncio.run(handle())

process_read_roof_data(999)

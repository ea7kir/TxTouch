import asyncio
import websockets

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# The main function that will handle connection and communication 
# with the server

# async def listen():
#     # Connect to the server
#     async with websockets.connect(URL) as ws:
#         # Send a greeting message
#         #await ws.send("Hello Server!")
#         # Stay alive forever, listening to incoming msgs
#         while True:
#             msg = await ws.recv()
#             print(msg)
# 
# # Start the connection
# asyncio.get_event_loop().run_until_complete(listen())
# #asyncio.get_event_loop().run_forever()


# can also test $ python -m websockets ws://roof.local:8765/

class RoofData:
    counter = 0
    connected = False

roof_data = RoofData()

def process_read_roof_data(connection):
    async def handle():
        url = f'ws://{SERVER}:{PORT}/'
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
                
                roof_data.counter = await websocket.recv() # TODO: JSON
                print(roof_data.counter, flush=True)

    asyncio.run(handle())

process_read_roof_data(999)

import asyncio
import websockets

SERVER = 'roof.local'
PORT = 8765
URL = f'ws://{SERVER}:{PORT}/'

# The main function that will handle connection and communication 
# with the server
async def listen():
    # Connect to the server
    async with websockets.connect(URL) as ws:
        # Send a greeting message
        await ws.send("Hello Server!")
        # Stay alive forever, listening to incoming msgs
        while True:
            msg = await ws.recv()
            print(msg)

# Start the connection
#asyncio.get_event_loop().run_until_complete(listen())
asyncio.run(listen)

# can also test $ python -m websockets ws://roof.local:8765/
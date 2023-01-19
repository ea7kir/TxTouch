import asyncio
import websockets

class SpectrumData:
    def __init__(self):
        self.points = [(int(0),int(0))] * 920 # to ensure the last point is (0,0)
        self.beacon_level:int = 0

# Each scan sends a block of 1844 bytes
# This is 922 16-bit samples in low-high format
# The last two 16-bit samples are zero
# Sample zero is at 10490.500MHz
# Each sample represents 10000 / 1024 = 9.765625kHz
# Sample 919 is at 10499.475MHz
# The noise floor value is around 10000
# The peak of the beacon is around 40000

#def process_read_spectrum_data(send_spectrum_data):
#    async def handle():
#        url = 'wss://eshail.batc.org.uk/wb/fft/fft_ea7kirsatcontroller'
#        async with websockets.connect(url) as websocket:
#            spectrum_data = SpectrumData()
#            while True:
#                recvd_data = await websocket.recv()
#                if len(recvd_data) != 1844:
#                    print('rcvd_data != 1844')
#                    continue
#                j = 1
#                for i in range(0, 1836, 2):
#                    uint_16: int = int(recvd_data[i]) + (int(recvd_data[i+1] << 8))
#                    spectrum_data.points[j] = (j, uint_16)
#                    j += 1
#                spectrum_data.points[919] = (919, 0)
#                # calculate the average beacon peak level where beacon center is 103
#                spectrum_data.beacon_level = 0
#                for i in range(93, 113): # should be range(73, 133), but this works better
#                    spectrum_data.beacon_level += spectrum_data.points[i][1]
#                spectrum_data.beacon_level //= 20
#                send_spectrum_data.send(spectrum_data)
#
#    asyncio.get_event_loop().run_until_complete(handle())

def process_read_spectrum_data(send_spectrum_data):
    async def handle():
        url = 'wss://eshail.batc.org.uk/wb/fft/fft_ea7kirsatcontroller'
        async with websockets.connect(url) as websocket:
            spectrum_data = SpectrumData()
            while True:
                recvd_data = await websocket.recv()
                if len(recvd_data) != 1844:
                    print('rcvd_data != 1844')
                    continue
                j = 1
                for i in range(0, 1836, 2):
                    uint_16: int = int(recvd_data[i]) + (int(recvd_data[i+1] << 8))
                    spectrum_data.points[j] = (j, uint_16)
                    j += 1
                spectrum_data.points[919] = (919, 0)
                # calculate the average beacon peak level where beacon center is 103
                spectrum_data.beacon_level = 0
                for i in range(93, 113): # should be range(73, 133), but this works bet
                    spectrum_data.beacon_level += spectrum_data.points[i][1]
                spectrum_data.beacon_level //= 20
                send_spectrum_data.send(spectrum_data)

    asyncio.run(handle())


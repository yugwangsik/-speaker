import asyncio
import struct
import time
from bleak import BleakClient


read_test = ""

async def run(address):
    global read_test
    async with BleakClient(address) as client:
        print('connected')
        services = await client.get_services()

        #while True:
        data = await client.read_gatt_char(read_test)

        #read_data = struct.unpack('c', data)
        #print(type(read_data))
        #print('read_data: ',read_data[0])
        print('read_data: ', data)


    print('disconnect')

def main(_text):
    global read_test
    if _text == "운동":
        address = "E6:F3:C7:D5:FC:84"
        read_test = "00002a24-0000-1000-8000-00805f9b34fb"
    elif _text == "손목":
        address = "D0:33:34:80:76:87"
        read_test = "00002a24-0000-1000-8000-00805f9b34fb"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address))
    print('done')

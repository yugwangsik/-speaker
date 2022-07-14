import asyncio
import struct
import time
from bleak import BleakClient

address = "DF:65:5C:84:A1:44"


async def run(address):
    client = BleakClient(address)
    await client.connect()
    while True:
        time.sleep(3)
        print('connected')


loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')

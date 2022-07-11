import asyncio
from bleak import BleakScanner

device_list = []


async def run():
    global device_list
    devices = await BleakScanner.discover()
    #print(type(devices))
    #print(devices[0])
    for d in devices:
        #for i in range(len(devices)):
        val = str(d)
        if "UART" in val:
                device_list.append(str(d))

    print(device_list)
    for i in device_list:
        print(type(i))
        print(i[0:17])
    #for d in devices:
        #print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

import asyncio
import struct
import time
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import requests

#address = "DF:65:5C:84:A1:44"
address = "CC:AE:7F:D3:7D:08"
read_data = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

result = False


def notify_callback(sender: int, data: bytearray):
    cnt = len(data)
    t = data
    t = t.decode('utf-8')
    t = t.replace(" ", "")
    print('dumbbell value')
    print(t)
    print('===============================================================================================')

    url = "http://localhost:10001/index/check"
    void = {'void':" "}
    ck = requests.post(url, json=void)
    ck = ck.json()
    ck = int(ck["val"])

    if ck:
        if cnt > 60:
            big_data = t
            url = "http://hangyu.pe.kr:9876/auth_m/keyword"
            datas = {'dumbbell':big_data}
            requests.post(url, json=datas)



#async def run(address, uuid, status):
async def run(address):
    global result

    async with BleakClient(address) as client:
        print('connected')
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                #if characteristic.uuid == uuid:
                if characteristic.uuid == read_data:
                    if 'notify' in characteristic.properties:
                        while True:
                            await client.start_notify(characteristic, notify_callback)




    print('disconnect')


loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')

import asyncio
import struct
import time
from bleak import BleakClient
#import sys
#sys.path.append("./flask/views")
import requests
import json


address = "E4:27:42:CA:AA:E5"
#address = "DF:65:5C:84:A1:44"
#address = "CC:AE:7F:D3:7D:08"
read_data = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
num = 0
test_list = []



def notify_callback(sender: int, data: bytearray):
    global test_list, num
    #test_list.append(data)
    #num += 1
    #global num
    num += 1
    #cnt = len(data)
    #change = "B" * 26
    #big_data = struct.unpack(f'{change}', data)
    #print("hand value")
    print(data)
    #print(big_data)
    print(num)
    #print(data)
    #print('===============================================================================================')
#    time.sleep(1)

    #url = "http://localhost:10001/index/check"
    #void = {'void':" "}
    #ck = requests.post(url, json=void)
    #ck = ck.json()
    #ck = int(ck["val"])

#    ck = True
#    if ck:
#        url = "http://hangyu.pe.kr:9876/auth_m/keyword"
#        datas = {'hand':big_data}
#        response = requests.post(url, json=datas)
#        print(response.json())


#    url = "http://hangyu.pe.kr:9876/auth_m/keyword"
#    datas = {'hand':big_data}
#    response = requests.post(url, json=datas)
    #print(response.json())


#async def run(address, uuid, status):
async def run(address):
    global test_list, num
    async with BleakClient(address) as client:
        print('connected')
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                #if characteristic.uuid == uuid:
                if characteristic.uuid == read_data:
                    if 'notify' in characteristic.properties:
                        #while status == True:
                        while True:
                        #while num < 7800:
                        #for i in range(10000):
                            await client.start_notify(characteristic, notify_callback)



    print(len(test_list))
    print('disconnect')

#def main(address, uuid, status):
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(run(address))
#    print('done')

#def main(address, uuid, status):
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')

import asyncio
import struct
import time
import json
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import requests

#address = "D0:33:34:80:76:87"
address1 = "CC:AE:7F:D3:7D:08"
#address = "DE:81:4C:EA:A8:38"
#address = "E3:B8:6C:B9:A2:71"
#address2 = "E4:27:42:CA:AA:E5"
address3 = "DF:65:5C:84:A1:44"
address4 = "C2:6B:78:BB:76:90"
#read_test = "5f78df94-798c-46f5-990a-b3eb6a065c88"
read_test = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
#read_test = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
#read_test = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

def notify_callback(sender: int, data: bytearray):
    cnt = len(data)
    #print(cnt)
    #print(data)

    change = "b" * 26

    big_data = struct.unpack(f'{change}', data)
    print("hand value")
    print(big_data)
    print('===============================================================================================')

    url = "http://hangyu.pe.kr:9876/auth_m/keyword"
    datas = {'hand':big_data}
    response = requests.post(url, json=datas)
    print(response.json())


def notify_callback2(sender: int, data: bytearray):
    cnt = len(data)
    t = data
    t = t.decode('utf-8')
    t = t.replace(" ", "")

    if cnt > 60:
        ##print(type(t))
        print('dumbbell value')
        print(t)
        print('===============================================================================================')
        big_data = t
        url = "http://hangyu.pe.kr:9876/auth_m/keyword"
        datas = {'dumbbell':big_data}
        requests.post(url, json=datas)


def notify_callback3(sender: int, data: bytearray):
    cnt = len(data)
    t = data
    t = t.decode('utf-8')
    t = t.replace(" ", "")

    print('plus value')
    print(t)
    print('===============================================================================================')
    plus_data = t
    url = "http://hangyu.pe.kr:9876/auth_m/keyword"
    datas = {'plus':plus_data}
    requests.post(url, json=datas)


async def main():
    global address1
    global address3
    global address4
    result = await asyncio.gather(run_hand(address3), run_dumbbell(address1), run_plus(address4))


async def run_hand(address):
    async with BleakClient(address, time=5.0) as client:
        print('hand')
        hand_services = await client.get_services()
        for service in hand_services:
            for characteristic in service.characteristics:
                if 'notify' in characteristic.properties:
                    await client.start_notify(characteristic, notify_callback)



async def run_dumbbell(address):
    async with BleakClient(address, time=5.0) as client:
        print("dumbbell")
        dumb_services = await client.get_services()
        for service in dumb_services:
            for characteristic in service.characteristics:
                if 'notify' in characteristic.properties:
                    await client.start_notify(characteristic, notify_callback2)



async def run_plus(address):
    async with BleakClient(address, time=5.0) as client:
        print("dumbbell")
        plus_services = await client.get_services()
        for service in plus_services:
            for characteristic in service.characteristics:
                if 'notify' in characteristic.properties:
                    await client.start_notify(characteristic, notify_callback3)



#    except:
#        client.disconnect()

    print('disconnect')

asyncio.run(main())
#loop = asyncio.get_event_loop()
#loop.run_until_complete(run(address1, address3))
#run(address)
print('done')

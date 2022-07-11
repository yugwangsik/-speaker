import asyncio
import struct
import time
import json
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import requests

#address = "C2:6B:78:BB:76:90"
#address = "CC:AE:7F:D3:7D:08"
#address = "DE:81:4C:EA:A8:38"
#address = "E3:B8:6C:B9:A2:71"
#address2 = "E4:27:42:CA:AA:E5"
#address = "DF:65:5C:84:A1:44"
address = "EE:B1:5D:F7:74:59"
#read_test = "5f78df94-798c-46f5-990a-b3eb6a065c88"
read_RX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
read_TX = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
#read_test = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
#read_test = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

num = 0

def notify_callback(sender: int, data: bytearray):
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

'''
def notify_callback(sender: int, data: bytearray):
    global num
    num += 1
    cnt = len(data)
    #print(cnt)
    #print(data)
    t = data
    t = t.decode('utf-8')
    print(t)

    #change = "b" * 26

    #big_data = struct.unpack(f'{change}', data)
    #print("hand value")
    #print(big_data)
    #print('===============================================================================================')

    url = "http://hangyu.pe.kr:9876/auth_m/keyword"
    big_data = t
    datas = {'data':big_data}
    requests.post(url, json=datas)



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

'''

async def main():
    global address1
    global address3
    result = await asyncio.gather(run_hand(address3), run_dumbbell(address1))



async def run(address):
#    try:
    async with BleakClient(address) as client:
        print('hand')
        nordic_services = await client.get_services()
        for service in nordic_services:
            for characteristic in service.characteristics:
                if 'write' in characteristic.properties:
                    await client.write_gatt_char(read_RX, bytes(b'1'))
                    #await client.write_gatt_char(read_RX, bytes(b'+'))
                    print("+++")

#                    for i in range(10):
#                if 'notify' in characteristic.properties:
#                    await client.start_notify(characteristic, notify_callback)
#                            read = await client.read_gatt_char(read_TX)
#                            print('read: ', read)
#
#                    if 'write' in characteristic.properties:
#                        await client.write_gatt_char(read_RX, bytes(b'-'))
#                        print("---")
#
#                    for i in range(10):
#                        if 'notify' in characteristic.properties:
#                            #await client.start_notify(characteristic, notify_callback)
#                            read = await client.read_gatt_char(read_TX)
#                            print('read: ', read)
#
#                    if 'write' in characteristic.properties:
#                        await client.write_gatt_char(read_RX, bytes(b'2'))

#    except:
#        client.disconnect()
#        print('disconnect')



#asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
#run(address)
print('done')
print(num)

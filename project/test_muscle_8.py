import asyncio
import struct
import time
from bleak import BleakClient, BleakScanner
import sys
sys.path.append("./flask/views")
import requests


#address = "E4:27:42:CA:AA:E5"
#address = "C2:6B:78:BB:76:90"
#address = "CC:AE:7F:D3:7D:08"
address = "FD:B1:28:A8:41:3B"
read_data = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
read_RX = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

device_list = []
#address = ""

value1 = 0


def notify_callback(sender: int, data: bytearray):
    global address
    cnt = len(data)
    t = data
    t = t.decode('utf-8')
    t = t.replace(" ", "")

    print('plus value')
    print(address)
    print(t)
    print('===============================================================================================')
    plus_data = t
    url = "http://34.64.199.227:9876/muscle/push"
    datas = {'plus':plus_data,
             'address':address + " 8번"}
    requests.post(url, json=datas)


#async def run(address, uuid, status):
async def run(address):
    global value1
    async with BleakClient(address) as client:
        print('connected')
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                if 'notify' in characteristic.properties:
                    await client.write_gatt_char(read_RX, bytes(b'1'))

                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))
                    await client.write_gatt_char(read_RX, bytes(b'+'))

                    #for i in range(1,4):
                        #await client.write_gatt_char(read_RX, bytes(b'+'))
                    while True:
#                        for i in range(1, 8):
#                            await client.write_gatt_char(read_RX, bytes(b'+'))
#                        url = "http://hangyu.pe.kr:9876/auth_m/send_mod"
#                        void = {'void':" "}
#                        mod = requests.post(url, json=void)
#                        mod1 = mod.json()
#                        mod = mod1["data"]
#                        value = mod1["value"]
#                        #if mod == "+" or mod == "-":
#                            #sign = mod
#                        #stat = mod.decode('utf-8')
#                        #print(mod)


#                        if mod == "1":
#                            await client.write_gatt_char(read_RX, bytes(b'1'))
#                        elif mod == "2":
#                            await client.write_gatt_char(read_RX, bytes(b'2'))
#                        elif mod == "+" and value != value1:
#                        #elif mod == "+":
#                            await client.write_gatt_char(read_RX, bytes(b'+'))
#                        elif mod == "-" and value != value1:
#                        #elif mod == "-":
#                            await client.write_gatt_char(read_RX, bytes(b'-'))

                        await client.start_notify(characteristic, notify_callback)
                        #value1 = value
                        #print(f'value = {value} | value1 = {value1}')
                #if 'write' in characteristic.properties:
                    #await client.write_gatt_char(read_RX, bytes(b'1'))
                    #await client.write_gatt_char(read_RX, bytes(b'+'))
                    #print("+++")
                    #num = 1
                #if num == 1:
                    #if 'notify' in characteristic.properties:
                        #while True:
                            #await client.start_notify(characteristic, notify_callback)
                #if characteristic.uuid == uuid:
                #if characteristic.uuid == read_data:
                    #if 'notify' in characteristic.properties:
                        #while status == True:
                        #while True:
                            #await client.start_notify(characteristic, notify_callback)




    print('disconnect')


'''
async def device():
    global device_list, address
    devices = await BleakScanner.discover()
    for d in devices:
        val = str(d)
        if "UART" in val:
            device_list.append(str(d))

    print(device_list)
    for i in device_list:
        print(i[0:17])
        address = i[0:17]
'''

loop = asyncio.get_event_loop()
#loop.run_until_complete(device())
loop.run_until_complete(run(address))
print('done')

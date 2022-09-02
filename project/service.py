import asyncio
from bleak import BleakClient

#address = "E6:F3:C7:D5:FC:84"
#address = "D0:33:34:80:76:87"
#address = "CC:AE:7F:D3:7D:08"
#address = "E3:B8:6C:B9:A2:71"
#address = "E4:27:42:CA:AA:E5"
#address = "DE:81:4C:EA:A8:38"
address = "FB:6B:CA:43:D7:C6"
#address = "C2:6B:78:BB:76:90"

async def run(address):
    #async with BleakClient(address) as client:
    client = BleakClient(address)
    await client.connect()
    print('connected')
    services = await client.get_services()
    for service in services:
        print(service)

        print('\tuuid:', service.uuid)
        print('\tcharacteristic list:')

        for characteristic in service.characteristics:
            print('\t\t', characteristic)

            print('\t\tuuid:', characteristic.uuid)
            print('\t\tdescription :', characteristic.description)
            print('\t\tproperties :', characteristic.properties)

    await client.disconnect()
    print('disconnect')

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
print('done')

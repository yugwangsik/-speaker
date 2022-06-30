import os
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import read_data
#import a_test_data_push
#import b_test_data_push
import asyncio
from multiprocessing import Process
import Text
import requests
import subprocess, time


def Order(_text):
    print("order_list.py: ", _text)

    if "그만" in _text:
        print("kill!")
        val = "0"
        url = "http://localhost:10001/index/change"
        datas = {'val':val}
        requests.post(url, json=datas)
        #subprocess.run(['python3 kill.py'], shell=True)
    else:
        if "운동" in _text:
            print("open!")
            #subprocess.run(['killall chromium-browser'])
            #subprocess.run(['python3 /home/pi/project/url/close.py'], shell=True)
            #subprocess.run(['python3 /home/pi/project/url/new.py'], shell=True)
            print("111111")
            #time.sleep(1)
            #Text.start()
            subprocess.run(['python3 /home/pi/project/url/go.py'], shell=True)
            Text.start()
            #exercise_status = True
            #url = "http://hangyu.pe.kr:9876/auth_m/open"
            #datas = {'word':_text}
            #requests.post(url, json=datas)
            #while exercise_status == True:
                #exercise_status = Proceeding()

        elif "스캔" in _text:
            print('scan!')
            val = "1"
            url = "http://localhost:10001/index/sign"
            datas = {'val':val}
            requests.post(url, json=datas)
            #scan_status = True
            #dumbbel_address = "CC:AE:7F:D3:7D:08"
            #hand_address = "DF:65:5C:84:A1:44"
            #muscle_address = "C2:6B:78:BB:76:90"
            #uuid = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
            #os.system('bash sensing.sh')
            #subprocess.Popen(['python3 dumbbell_data_push.py'], shell=True)
            #subprocess.Popen(['python3 hand_data_push.py'], shell=True)
            Text.bell()



def Proceeding():
    val = 3
    url = "http://hangyu.pe.kr:9876/auth_m/exercise"
    datas = {'val':val}
    response = requests.post(url, json=datas)
    print('=======')
    print(response)
    print(response.json())
    print('=======')
    word = response.json()
    print(word)
    print(type(word))
    return False
    print(word["data"])
'''
    if "fail" in word:
        Text.fail()
        stat = True
        return stat

    elif "success" in word:
        Text.success()
        stat = False
        return stat

    elif cnt <= 10:
        Text.count(cnt)
        stat = True
        return stat
'''

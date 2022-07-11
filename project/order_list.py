import os
from bleak import BleakClient
import sys
sys.path.append("./flask/views")
import read_data
import asyncio
from multiprocessing import Process
import Text, multi_turn
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

    else:
        if "운동" in _text:
            print("open!")
            subprocess.run(['python3 /home/pi/speaker_project/project/url/go.py'], shell=True)
            Text.start()
            #time.sleep(0.5)

            bol = True
            multi_turn.main(bol)
            print("aaaaa")
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
            Text.bell()


    if "다운" in _text:
        print("1")
        data = True
        url = "http://localhost:10001/index/update"
        datas = {'data':data}
        requests.post(url, json=datas)



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

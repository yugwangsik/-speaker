# _*_ coding: utf-8 _*_
import argparse
import locale
import logging
from bleak import BleakClient
from google.assistant.library.event import EventType
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts
import Text, order_list
import re
import requests,subprocess



def get_hints(language_code):
    if language_code.startswith('ko_'):
        return None

    return None


def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


def main(_bol):
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', 'ko_KR')
    hints = get_hints('ko_KR')
    client = CloudSpeechClient()
    with Board() as board:
        while _bol:
            print("동작 선택 대기중...")
            text = client.recognize(language_code='ko_KR', hint_phrases=hints)

            if text is None:
                _bol = False
            else:
                if "1" in text:
                    subprocess.run(['python3 /home/pi/speaker_project/project/url/choice.py'], shell=True)
                    choice = 1
                    url = "http://hangyu.pe.kr:9876/auth_m/select"
                    datas = {'choice':choice}
                    requests.post(url, json=datas)
                    print("선택 번호: " + text)

                elif "이" in text:
                    subprocess.run(['python3 /home/pi/speaker_project/project/url/choice.py'], shell=True)
                    choice = 2
                    url = "http://hangyu.pe.kr:9876/auth_m/select"
                    datas = {'choice':choice}
                    requests.post(url, json=datas)
                    print("선택 번호: " + text)

                elif "3" in text:
                    subprocess.run(['python3 /home/pi/speaker_project/project/url/choice.py'], shell=True)
                    choice = 3
                    url = "http://hangyu.pe.kr:9876/auth_m/select"
                    datas = {'choice':choice}
                    requests.post(url, json=datas)
                    print("선택 번호: " + text)

                elif "4" in text:
                    subprocess.run(['python3 /home/pi/speaker_project/project/url/choice.py'], shell=True)
                    choice = 4
                    url = "http://hangyu.pe.kr:9876/auth_m/select"
                    datas = {'choice':choice}
                    requests.post(url, json=datas)
                    print("선택 번호: " + text)

            print(choice)

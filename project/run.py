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
import requests

def callDB(user_say):
    return None


def get_hints(language_code):
    if language_code.startswith('ko_'):
        return None

    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def Trigger(client, hints):
    keyword = '유리'
    say_text = client.recognize(language_code='ko_KR', hint_phrases=hints)
    print(say_text)
    try:
        #if say_text in keyword:
        if keyword in say_text:
            Text.play()
            return True
        else:
            Text.replay()
            return False
    except Exception as e:
        return False


def main():
    address = '/home/pi/cloud_speech.json'
    #logging.basicConfig(level=logging.DEBUG)
    #print("대기중")
    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', 'ko_KR')
    hints = get_hints('ko_KR')
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            print("대기중...")
            stat = Trigger(client, hints)
            if stat:
                if hints:
                    logging.info('Say something, e.g. %s.' % ','.join(hints))
                    print(" ")
                else:
                    logging.info('Say someting.')

                text = client.recognize(language_code='ko_KR', hint_phrases=hints)
                if text is None:
                    continue
                else:
                    if '안녕' in text:
                        aiy.voice.tts.say('goodbye')
                        break
                    else:
                        if text is None:
                            logging.info('You said nothing.')
                            continue
                        elif text is not None:
                            print("run.py: ", text)
                            order_list.Order(text)

                        print("작업 끝")


if __name__ == '__main__':
    main()

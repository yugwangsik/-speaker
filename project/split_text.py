# _*_ coding: utf-8 _*_
import argparse
import locale
import logging

from google.assistant.library.event import EventType
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts

from konlpy.tag import Komoran
#import database
#import Text

import re

def callDB(user_say):
    return None


def get_hints(language_code):
    if language_code.startswith('ko_'):
        return None

    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    address = '/home/pi/cloud_speech.json'
    logging.basicConfig(level=logging.DEBUG)
    #a = locale_language()
    #print(a)
    trigger = 'keti'
    komoran = Komoran()

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', 'ko_KR')
    hints = get_hints('ko_KR')
    #print(hints)
    client = CloudSpeechClient()
    #print(client)
    with Board() as board:
        while True:
            if hints:
                logging.info('Say something, e.g. %s.' % ','.join(hints))
            else:
                logging.info('Say someting.')

            text = client.recognize(language_code='ko_KR', hint_phrases=hints)
            #text = text.lower()

            if text is None:
                logging.info('You said nothing.')
                continue
            elif text is not None:
                #speech = database.myDB(text)
                #print(text)
                #test = text.split(' ')
                #for t in test:
                #    print(t)
                #Text.tts(speech)
                print(text)
                str_split = komoran.nouns(text)
                num_split = re.sub(r'[^0-9]', '', text)
                i = 0
                '''
                for st in str_split:
                    print(st[i])
                    i = i + 1
                '''   
                #print(str_split[0])
                print(str_split)
                print(num_split)
            
            logging.info('Your said: "%s"' % text)
            #text = text.lower()
            if '안녕' in text:
                aiy.voice.tts.say('goodbye')
                break


if __name__ == '__main__':
    main()

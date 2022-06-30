from google.cloud import texttospeech
import pygame
import time

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/start.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    time.sleep(0.2)
    bell()
    return None



def replay():
    pygame.mixer.music.load("/home/pi/project/replay.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    time.sleep(0.2)
    bell()
    return None


def start():
    pygame.mixer.music.load("/home/pi/project/start.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    time.sleep(0.2)
    #bell()
    return None



def bell():
    pygame.mixer.music.load("/home/pi/project/bell.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue
    return None


def fail():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/fail.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue
    return None


def success():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/posture/dumbbell.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue
    return None


def count(cnt):
    str = "count" + cnt + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/count/" + str)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue
    return None


def tts(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
            language_code = 'ko-KR', 
            ssml_gender = texttospeech.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.AudioConfig(
            audio_encoding = texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config})

    with open('answer.mp3', 'wb') as out:
        out.write(response.audio_content)

    play()

    return None


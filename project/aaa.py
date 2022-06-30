from google.cloud import texttospeech
import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/success.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    return None


def bell():
    pygame.mixer.music.load("/home/pi/project/Blop Sound.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    return None


def count(cnt):
    str = "count" + cnt + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/project/" + str)
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

    with open('start.wav', 'wb') as out:
        out.write(response.audio_content)

    play()

    return None

aa = "운동 동작을 선택해주세요."
tts(aa)

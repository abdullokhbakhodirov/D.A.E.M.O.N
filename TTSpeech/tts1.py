import pygame
import os
import subprocess
import time
import pyautogui


def text_to_speech_en(example_text):
    voice = "en-US-ChristopherNeural"
    command = f'edge-tts --voice "{voice}" --text "{example_text}" --write-media "test.mp3"'
    try: 
        subprocess.run(command, shell=True, check=True)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
    except:
        subprocess.run(command, shell=True, check=True)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def text_to_speech_uz(example_text):
    voice = "uz-UZ-SardorNeural"
    command = f'edge-tts --voice "{voice}" --text "{example_text}" --write-media "test.mp3"'
    os.system(command)
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def text_to_speech_ru(example_text):
    voice = "ru-RU-DmitryNeural"
    command = f'edge-tts --voice "{voice}" --text "{example_text}" --write-media "test.mp3"'
    os.system(command)
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


'''Name: uz-UZ-MadinaNeural
Gender: Female

Name: uz-UZ-SardorNeural
Gender: Male'''

'''Name: ru-RU-DmitryNeural
Gender: Male

Name: ru-RU-SvetlanaNeural
Gender: Female'''

'''Name: en-GB-LibbyNeural
Gender: Female

Name: en-GB-MaisieNeural
Gender: Female

Name: en-GB-RyanNeural
Gender: Male

Name: en-GB-SoniaNeural
Gender: Female'''

'''Name: en-US-AnaNeural
Gender: Female

Name: en-US-AriaNeural
Gender: Female

Name: en-US-ChristopherNeural
Gender: Male

Name: en-US-EricNeural
Gender: Male

Name: en-US-GuyNeural
Gender: Male

Name: en-US-JennyNeural
Gender: Female

Name: en-US-MichelleNeural
Gender: Female

Name: en-US-RogerNeural
Gender: Male'''

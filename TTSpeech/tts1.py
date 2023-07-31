import pygame
import edge_tts

async def text_to_speech_en(example_text):
    voice = "en-US-ChristopherNeural"
    try:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
    except:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
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


async def text_to_speech_uz(example_text):
    voice = "uz-UZ-SardorNeural"
    try:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
    except:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
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


async def text_to_speech_ru(example_text):
    voice = "ru-RU-DmitryNeural"
    try:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
    except:
        communicate = edge_tts.Communicate(example_text, voice)
        await communicate.save('test.mp3')
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

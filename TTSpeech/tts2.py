import torch
import pygame
import os


def text_to_speech_en(example_text):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'v3_en.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/en/v3_en.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    sample_rate = 48000
    speaker='en_0'

    audio_paths = model.save_wav(text=example_text,
                                speaker=speaker,
                                sample_rate=sample_rate)
    pygame.mixer.init()
    pygame.mixer.music.load("test.wav")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    os.remove("test.wav")


def text_to_speech_uz(example_text):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'v3_uz.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/uz/v3_uz.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    sample_rate = 48000
    speaker='dilnavoz'

    audio_paths = model.save_wav(text=example_text,
                                speaker=speaker,
                                sample_rate=sample_rate)
    pygame.mixer.init()
    pygame.mixer.music.load("test.wav")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    os.remove("test.wav")


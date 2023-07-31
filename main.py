from Chatbot import mainy as chat, unique_code as code, pgadmin
from command_procesing import command as cmp
from Image_Desciption import img_descripte as img
from News import en_news as en, uz_news as uz
from SpeechTT import stt 
from TTSpeech import tts1 as tts
from wake_word_detection import wwd 
from Weather import weather_get as weather
import asyncio


wwd.wake_word()
uni_code = code.get_unique_code_from_file()
username = pgadmin.get_username(uni_code)
if not uni_code:

    asyncio.run(tts.text_to_speech_en("You are new in our program so can I ask you some questions to register you"))
    question = stt.main_speech_to_text()
    prob = cmp.comparing(['Yes', 'Yes certainly', 'Yes you can', 'Ok', "Ok ask"], question)
    for i in prob:
        if i >= 70:
            codee = code.write_unique_code_to_file()
            asyncio.run(tts.text_to_speech_en("What is your name?"))
            username = stt.main_speech_to_text()
            asyncio.run(tts.text_to_speech_en("Can you create a password and spell it"))
            password = stt.main_speech_to_text()
            asyncio.run(tts.text_to_speech_en("What is your email? Please write it in the console"))
            email = input("Write your email here >>> ")
            pgadmin.add_user(codee, username, password, qanda="{}", email=email)
            break


asyncio.run(tts.text_to_speech_en(f"Hello Abdullokh, how can I help you"))
flag = True
while flag:
    wwd.wake_word()
    question: str = stt.main_speech_to_text()
    words = ['image', 'picture', 'news', 'reports', 'report', 'images', 'pictures', 'music', 'musics', 'player', 'song', 'songs', "weather"]
    sen = question.split()
    fl = True
    for i in sen:
        if i in words:
            f = cmp.comparing(["wants to listen music", "wants to open music player", "open music player", "wants to know what is the latest news", "wants to know news from yesterday", "wants to know what is the description of the image", "wants to know what's the weather right now", "wants to know what is the weather for tomorrow", "wants to know what was the weather yesterday", "wants to know what was the weather in previous days"], question)
            count = 0
            for j in f:
                if j >= 70 and count in [0, 1, 2]:
                    # listen music
                    fl = False
                    break
                elif j >= 70 and count in [3, 4]:
                    a_news = en.get_news_en()
                    for i in a_news:
                        print(f"{i} === {a_news[i]}")
                    asyncio.run(tts.text_to_speech_en("I have printed all news from BBC.com"))
                    fl = False
                    break
                elif j >= 70 and count in [5]:
                    des = img.img_descripte()
                    asyncio.run(tts.text_to_speech_en(f"Descriptions of this image like this: {des[0]}, {des[1]}"))
                    fl = False
                    break
                elif j >= 70 and count in [6, 7, 8]:
                    temp = weather.get_location()
                    asyncio.run(tts.text_to_speech_en(f"In the current time the temperature in {temp[1]} is {temp[0]}"))
                    fl = False
                    break
                else:
                    count += 1
        elif not fl:
            break
    if fl:
        answer = chat.chatgpt(question)
        asyncio.run(tts.text_to_speech_en(answer))

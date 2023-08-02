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
h = True
if not uni_code:
    asyncio.run(tts.text_to_speech_en("You are new in our program so can I ask you some questions to register you"))
    while True:
        question = stt.main_speech_to_text()
        prob = cmp.comparing(question)
        if prob == 'yes':
            codee = code.write_unique_code_to_file()
            asyncio.run(tts.text_to_speech_en("What is your name?"))
            username = stt.main_speech_to_text()
            asyncio.run(tts.text_to_speech_en("Can you create a password and spell it"))
            password = stt.main_speech_to_text()
            asyncio.run(tts.text_to_speech_en("What is your email? Please write it in the console"))
            email = input("Write your email here >>> ")
            pgadmin.add_user(codee, username, password, qanda="{}", email=email)
            h = True
            break
        elif h:
            asyncio.run(tts.text_to_speech_en("Sorry if you will not register, you can't use me. I will ask you one last time, can I ask you some questions to register you?"))
            h = False
            continue
        else:
            asyncio.run(tts.text_to_speech_en("Sorry but you can't use this program"))
            break
try: 
    username = pgadmin.get_username(uni_code)
except: 
    username = pgadmin.get_username(codee)
if not h:
    import sys
    sys.exit()


asyncio.run(tts.text_to_speech_en(f"Hello {username}, how can I help you"))
flag = True
while flag:
    wwd.wake_word()
    question: str = stt.main_speech_to_text()
    words = ['image', 'picture', 'news', 'reports', 'report', 'images', 'pictures', 'music', 'musics', 'player', 'song', 'songs', "weather"]
    sen = question.split()
    fl = False
    for i in sen:
        if i in words:
            f = cmp.comparing(question)
            if f == 'weather':
                temp = weather.get_degree()
                asyncio.run(tts.text_to_speech_en(f"Temperature in {temp[1]} is {temp[0]}"))
                fl = True
                break
            elif f == 'news':
                new_en = (en.get_news_en())[1]
                new_uz = (uz.get_news_uz())[1]
                city = weather.get_location()

                if city[1] == "O'zbekiston":
                    for i in new_uz:
                        print(f"{i} ==== {new_uz[i]}")
                    asyncio.run(tts.text_to_speech_en("I have printed news in your country. Do you want to know about general news too?"))
                    question: str = stt.main_speech_to_text()
                    f = cmp.comparing(question)
                    if f == 'yes':
                        for i in new_en:
                            print(f"{i} ==== {new_en[i]}")
                        asyncio.run(tts.text_to_speech_en("I have printed last general news from BBC"))
                    else:
                        asyncio.run(tts.text_to_speech_en("Ok ask everything you want"))
                else:
                    for i in new_en:
                        print(f"{i} ==== {new_en[i]}")
                    asyncio.run(tts.text_to_speech_en("I have printed last news from BBC"))
                fl = True
                break
                    

            elif f == 'music':
                ...
            elif f == 'player':
                ...
            elif f == 'img':
                ...
    if not fl:
        answer = chat.gpt_turbo(question, uni_code)
        asyncio.run(tts.text_to_speech_en(answer))

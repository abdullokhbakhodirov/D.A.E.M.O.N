from Chatbot import mainy as chat, unique_code as code, pgadmin
from command_procesing import command as cmp
from Image_Desciption import img_descripte as img
from News import en_news as en, uz_news as uz
from SpeechTT import stt 
from TTSpeech import tts1 as tts
from wake_word_detection import wwd 


wwd.wake_word()
uni_code = code.get_unique_code_from_file()
username = pgadmin.get_username(uni_code)
if not uni_code:

    tts.text_to_speech_en("You are new in our program so can I ask you some questions to register you")
    question = stt.main_speech_to_text()
    prob = cmp.comparing(['Yes', 'Yes certainly', 'Yes you can', 'Ok', "Ok ask"], question)
    for i in prob:
        if i >= 70:
            codee = code.write_unique_code_to_file()
            tts.text_to_speech_en("What is your name?")
            username = stt.main_speech_to_text()
            tts.text_to_speech_en("Can you create a password and spell it")
            password = stt.main_speech_to_text()
            tts.text_to_speech_en("What is your email? Please write it in the console")
            email = input("Write your email here >>> ")
            pgadmin.add_user(codee, username, password, qanda="{}", email=email)
            break


tts.text_to_speech_en(f"Hello {username}, how can I help you")
wwd.wake_word()
question = stt.main_speech_to_text()
flag = True
while flag:
    answer = chat.chatgpt(question)
    tts.text_to_speech_en(answer)
    wwd.wake_word()    
    question = stt.main_speech_to_text()

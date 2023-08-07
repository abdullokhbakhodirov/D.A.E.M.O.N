from tkinter import *
import customtkinter as tk
from PIL import Image
from Chatbot.mainy import chatgpt
from SpeechTT.stt import main_speech_to_text
from TTSpeech.tts1 import text_to_speech_en
import threading
from Chatbot.unique_code import get_unique_code_from_file
from login_window import login_windows



if not get_unique_code_from_file():
    login_windows()


tk.set_appearance_mode("dark")
window = tk.CTk()
window.geometry("410x670+500+10")
window.title("D.A.E.M.O.N")
window.resizable(False, False)

# ========================================================================================================================
global txt, ans, flag
txt = 0
ans = 1
flag = False
def send_message(master, textbox, btn1, btn2):
    text = textbox.get("0.0", "end")
    textbox.delete("0.0", "end") 
    if len(text) <= 1:
        None
    else:
        btn1.configure(state="disabled")
        btn2.configure(state='disabled')
        frame_creator(master, text, btn1, btn2)


def get_chatgpt_response_in_thread(master, text, btn1, btn2):
    sen = chatgpt(text)
    master.after(0, answer_to, master, sen, btn1, btn2)


def record_speech(master, lbl_, btn1, btn2):
    text = main_speech_to_text()
    master.after(0, main_frain, master, text, lbl_, btn1, btn2)


def main_frain(master, text, lbl_, btn1, btn2):
    global txt
    lbl_.configure(state="normal")  
    lbl_.delete("0.0",tk.END)
    lbl_.insert("0.0", text)
    lbl_.configure(state="disabled")
    lbl_.get('0.0', tk.END).split('\n')
    a = count_lines(lbl_)
    height1 = a * 18
    lbl_.configure(height=height1)
    txt += 2
    master.update()
    thread = threading.Thread(target=lambda:get_chatgpt_response_in_thread(master, text, btn1, btn2))
    thread.start()


def record_audio(master, btn1, btn2):
    btn1.configure(state='disabled')
    btn2.configure(state='disabled')
    global txt, flag
    lbl_ = tk.CTkTextbox(master, width=410, bg_color='gray', activate_scrollbars=False, height=20, corner_radius=0)
    lbl_.grid(row=txt, column=0)
    lbl_.insert("0.0", "Speak now ...")
    lbl_.configure(state="disabled")
    master.update()
    thread = threading.Thread(target=lambda:record_speech(master, lbl_, btn1, btn2))
    thread.start()


def count_lines(textbox):
    content = textbox.get('0.0', tk.END)
    lines = content.split('\n')
    num_lines = len(lines)
    return num_lines


def frame_creator(master, text, btn1, btn2):
    global txt
    lbl_ = tk.CTkTextbox(master, width=410, bg_color='gray', activate_scrollbars=False, height=100, corner_radius=0)
    lbl_.grid(row=txt, column=0)
    lbl_.insert("0.0", text)
    lbl_.configure(state="disabled")
    lbl_.get('0.0', tk.END).split('\n')
    a = count_lines(lbl_)
    height1 = a * 18
    lbl_.configure(height=height1)
    txt += 2
    master.update()
    thread = threading.Thread(target=lambda:get_chatgpt_response_in_thread(master, text, btn1, btn2))
    thread.start()


def answer_to(master, text, btn1, btn2):
    global ans
    lbl_1 = tk.CTkTextbox(master, fg_color='#38393f', activate_scrollbars=False, height=0, width=410, corner_radius=0)
    lbl_1.grid(row=ans, column=0)
    lbl_1.insert("0.0", text)
    lbl_1.configure(state="disabled")
    lbl_1.get('1.0', tk.END).split('\n')
    a = count_lines(lbl_1)
    height1 = a * 40
    lbl_1.configure(height=height1)
    ans += 2
    btn1.configure(state='normal')
    btn2.configure(state='normal')

# ========================================================================================================================


textbox = tk.CTkTextbox(window, width=300, height=45, border_width=2, corner_radius=10)
textbox.place(x=2, y=620)

image_path = "D:/Created Programs/Daemon/resourses/btn_micro.png"
img = tk.CTkImage(Image.open(image_path))
btn_record = tk.CTkButton(window, image=img, width=0, text="", height=45, border_width=2, corner_radius=10, command=lambda:record_audio(main_frame, btn_send, btn_record))
btn_record.place(x=358, y=620)

image_path2 = "D:/Created Programs/Daemon/resourses/btn_send.png"
img2 = tk.CTkImage(Image.open(image_path2))
btn_send = tk.CTkButton(window, image=img2, text="", width=0, height=45, border_width=2, corner_radius=10, command=lambda:send_message(main_frame, textbox, btn_send, btn_record))
btn_send.place(x=308, y=620)

frame = tk.CTkFrame(master=window, width=410, height=60, corner_radius=0)
frame.place(x=0, y=0)

image_path3 = "D:/Created Programs/Daemon/resourses/profile.png"
img3 = tk.CTkImage((Image.open(image_path3)), size=(50,50))
lbl_pro = tk.CTkLabel(master=frame, text="", image=img3, corner_radius=10)
lbl_pro.place(x=5, y=5)

main_frame = tk.CTkScrollableFrame(master=window, width=410, height=558, corner_radius=0, fg_color='#242424')
main_frame.place(x=0, y=60)

window.mainloop()

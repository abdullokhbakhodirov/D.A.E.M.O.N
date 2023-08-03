from tkinter import *
import customtkinter as tk
from PIL import Image
from Chatbot.mainy import chatgpt


tk.set_appearance_mode("dark")
window = tk.CTk()
window.geometry("410x670+500+10")
window.title("D.A.E.M.O.N")
# window.resizable(False, False)


# ========================================================================================================================
global txt, ans
txt = 0
ans = 1
def send_message(master, textbox):
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    textbox.delete("0.0", "end")  # delete all text
    # textbox.configure(state="disabled")
    frame_creator(master, text)


def record_audio():
    ...


def get_number_of_rows(text_box):
    num_rows = text_box.index(END).split('.')[0]
    return int(num_rows)


def frame_creator(master, text):
    global txt
    t = add_line_breaks(text, 410)
    lines = t.split('\n')
    num_rows = len(lines)
    he = num_rows*7
    lbl_ = tk.CTkLabel(master,text=t, width=410, height=he, bg_color='gray', corner_radius=0)
    lbl_.grid(row=txt, column=0)
    txt += 2
    master.update()
    answer_to(master, text)


def add_line_breaks(sentence, line_width):
    words = sentence.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= line_width:  # +1 for space between words
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    # Append the last line
    lines.append(current_line.strip())

    return "\n".join(lines)


def answer_to(master, text):
    global ans
    sen = chatgpt(text)
    t1 = add_line_breaks(sen, 410)
    lines = t1.split('\n')
    num_rows = len(lines)
    he = num_rows*7
    lbl_1 = tk.CTkLabel(master, text=t1, bg_color='darkgrey', width=410, height=he, corner_radius=0)
    lbl_1.grid(row=ans, column=0)
    ans += 2

# ========================================================================================================================


textbox = tk.CTkTextbox(window, width=300, height=45, border_width=2, corner_radius=10)
textbox.place(x=2, y=620)

image_path = "D:/Created Programs/Daemon/resourses/btn_micro.png"
img = tk.CTkImage(Image.open(image_path))
btn_record = tk.CTkButton(window, image=img, width=0, text="", height=45, border_width=2, corner_radius=10, command=lambda:record_audio())
btn_record.place(x=358, y=620)

image_path2 = "D:/Created Programs/Daemon/resourses/btn_send.png"
img2 = tk.CTkImage(Image.open(image_path2))
btn_send = tk.CTkButton(window, image=img2, text="", width=0, height=45, border_width=2, corner_radius=10, command=lambda:send_message(main_frame, textbox))
btn_send.place(x=308, y=620)

frame = tk.CTkFrame(master=window, width=410, height=60, corner_radius=0)
frame.place(x=0, y=0)

image_path3 = "D:/Created Programs/Daemon/resourses/profile.png"
img3 = tk.CTkImage((Image.open(image_path3)), size=(50,50))
lbl_pro = tk.CTkLabel(master=frame, text="", image=img3, corner_radius=10)
lbl_pro.place(x=5, y=7)

main_frame = tk.CTkScrollableFrame(master=window, width=410, height=558, corner_radius=0, fg_color='#242424')
main_frame.place(x=0, y=60)

window.mainloop()

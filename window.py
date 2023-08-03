from tkinter import *
import customtkinter as tk
from PIL import Image


tk.set_appearance_mode("dark")
window = tk.CTk()
window.geometry("410x670+500+10")
window.title("D.A.E.M.O.N")
window.resizable(False, False)


# ========================================================================================================================

def send_message():
    ...


def record_audio():
    ...

# ========================================================================================================================


textbox = tk.CTkTextbox(window, width=300, height=45, border_width=2, corner_radius=10)
textbox.place(x=2, y=620)

image_path = "D:/Created Programs/Daemon/resourses/btn_micro.png"
img = tk.CTkImage(Image.open(image_path))
btn_record = tk.CTkButton(window, image=img, width=0, text="", height=45, border_width=2, corner_radius=10, command=lambda:None)
btn_record.place(x=358, y=620)

image_path2 = "D:/Created Programs/Daemon/resourses/btn_send.png"
img2 = tk.CTkImage(Image.open(image_path2))
btn_send = tk.CTkButton(window, image=img2, text="", width=0, height=45, border_width=2, corner_radius=10, command=lambda:None)
btn_send.place(x=308, y=620)

frame = tk.CTkFrame(master=window, width=410, height=50, corner_radius=0)
frame.place(x=0, y=0)

image_path3 = "D:/Created Programs/Daemon/resourses/profile.png"
img3 = tk.CTkImage((Image.open(image_path3)))
lbl_pro = tk.CTkLabel(frame, text="", image=img3, font=('helvetica', 30), width=0, height=45, corner_radius=10)
lbl_pro.place(x=10, y=10)

window.mainloop()

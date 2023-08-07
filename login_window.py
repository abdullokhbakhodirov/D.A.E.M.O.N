import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image
from tkinter import Button


def login_windows():

    def show():
        show_btn.configure(text="Hide", command=lambda:hide())
        user_pass.configure(show="")
    
    def hide():
        show_btn.configure(text="Show", command=lambda:show())
        user_pass.configure(show="*")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("420x500+400+100")
    app.title("Login")

    frame = ctk.CTkFrame(master=app, width=320, height=370)
    frame.place(x=50, y=90)

    image_path2 = "D:/Created Programs/Daemon/resourses/profile.png"
    img2 = ctk.CTkImage(Image.open(image_path2), size=(70,70))
    lbl_profile = ctk.CTkLabel(app, text="", image=img2)
    lbl_profile.place(x=180, y=10)

    lbl_login = ctk.CTkLabel(frame, text="LOGIN", font=("Helvetica", 20))
    lbl_login.place(x=130, y=25)

    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username", width=280)
    user_entry.place(x=20, y=80)

    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*", width=230)
    user_pass.place(x=20, y=150)

    show_btn = ctk.CTkButton(master=frame, text="Show", command=lambda:show(), width=15)
    show_btn.place(x=260, y=150)

    button = ctk.CTkButton(master=frame,text='Login',command=lambda:None)
    button.place(x=95, y=260)

    checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
    checkbox.place(x=100, y=210)

    forgot_btn = Button(frame, font=('helvetica', 10), text="Forgot Password", command=lambda:None, bg="#2b2b2b", fg='white', border=0, cursor='hand2', activebackground='#2b2b2b')
    forgot_btn.place(x=25, y=310)

    regis_btn = Button(frame, font=("helvetica", 10), text="Create Account", command=lambda:None, bg="#2b2b2b", fg="white", border=0, cursor='hand2', activebackground='#2b2b2b')
    regis_btn.place(x=200, y=310)

    app.mainloop()
login_windows()
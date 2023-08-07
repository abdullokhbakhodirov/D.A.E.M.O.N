import customtkinter as tk
from tkinter import *


def login_windows():
    tk.set_appearance_mode("dark")
    window = tk.CTk()
    window.geometry("410x570+500+10")
    window.title("D.A.E.M.O.N")
    window.resizable(False, False)

    tk.CTkLabel(window, image="D:/Created Programs/Daemon/resourses/bg.png").pack()

    window.mainloop()
login_windows()
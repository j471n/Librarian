from tkinter import *
from os import getenv
from dotenv import load_dotenv
import webbrowser
from PIL import ImageTk, Image  #PIL -> Pillow

load_dotenv()

def profile1():
    webbrowser.open(getenv('PROFILE_1_URL'))

def profile2():
    webbrowser.open(getenv('PROFILE_2_URL'))


def aboutUS():
    root = Toplevel()
    root.title("About US")
    root.iconbitmap('img/about-icon.ico')
    root.geometry("740x495")

    color = '#BEFFE4'
    root.config(bg=color)

    bg, bg1, button = Image.open("img/profile/1.png"), Image.open("img/profile/2.png"), Image.open('img/profile/insta.png')
    bg, bg1, button = bg.resize((350, 470), Image.ANTIALIAS), bg1.resize(
        (350, 470), Image.ANTIALIAS), button.resize((170, 35), Image.ANTIALIAS)
    img, img1 , buttonIMG= ImageTk.PhotoImage(bg), ImageTk.PhotoImage(bg1) , ImageTk.PhotoImage(button)

    Label(root, image=img, border=0, bg=color).grid(row=0, column=0, padx=10, pady=10)
    Label(root, image=img1, bg=color).grid(row=0, column=2, padx=5, pady=10)

    button1 = Button(root, text='',image=buttonIMG, bg='white', border=0, command=profile1).place(relx=0.13, rely=0.79)
    button2 = Button(root, text='',image=buttonIMG, bg='white',border=0, command=profile2).place(relx=0.625, rely=0.79)

    root.resizable(0,0)

    root.mainloop()

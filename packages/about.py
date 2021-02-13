from tkinter import *
from os import getenv
from dotenv import load_dotenv
import webbrowser
from PIL import ImageTk, Image
from dotenv import *

env = find_dotenv('env/.env')
load_dotenv(env)

# Opening Profile1 URL in web browser
def profile1():
    webbrowser.open(getenv('PROFILE_1_URL'))

# Opening Profile2 URL in web browser
def profile2():
    webbrowser.open(getenv('PROFILE_2_URL'))


def aboutUS():

    # Initializing the About Window
    root = Toplevel()
    root.title("About US")
    root.iconbitmap('img/about-icon.ico')
    root.geometry("740x495")

    # Changing the Background color of the window
    color = '#BEFFE4'
    root.config(bg=color)

    # Importing Images
    bg, bg1, button = Image.open("img/profile/1.png"), Image.open("img/profile/2.png"), Image.open('img/profile/insta.png')
    bg, bg1, button = bg.resize((350, 470), Image.ANTIALIAS), bg1.resize( (350, 470), Image.ANTIALIAS), button.resize((170, 35), Image.ANTIALIAS)

    # Making Images as Object
    img, img1 , buttonIMG= ImageTk.PhotoImage(bg), ImageTk.PhotoImage(bg1) , ImageTk.PhotoImage(button)

    # Putting Images in the Window
    Label(root, image=img, border=0, bg=color).grid(row=0, column=0, padx=10, pady=10)
    Label(root, image=img1, bg=color).grid(row=0, column=2, padx=5, pady=10)

    # Making Instagram Buttons
    button1 = Button(root, text='',image=buttonIMG, bg='white', border=0, command=profile1).place(relx=0.13, rely=0.79)
    button2 = Button(root, text='',image=buttonIMG, bg='white',border=0, command=profile2).place(relx=0.625, rely=0.79)

    # Restricting Resizing
    root.resizable(0,0)

    root.mainloop()

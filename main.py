# Importing Files

from tkinter import *
from PIL import ImageTk, Image
import pymysql
from addBook import *
from viewsBook import *
from deletebook import *
from issueBook import *
from returnBook import *
from os import getenv, set_inheritable
from dotenv import load_dotenv
from feedback import feedBack
from about import aboutUS
from search import Search

# Loading ENV
load_dotenv()

# Initializing Root
root = Tk()
root.title("Librarian")
root.iconbitmap('img/logo.ico')
root.minsize(width=400, height=400)
root.geometry("600x500")


# Adding a background image

bg = Image.open("img/background/librarian.jpg")
bg = bg.resize((600, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(bg)
Label(root, image=img).pack()

# Heading Frame for Heading
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1,
                     text="Welcome to Librarian",
                     bg='black',
                     fg='white',
                     font=('Great Vibes', 28))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Function to put the Buttons on the Screen
def putButtons(set, X_Axis, Y_Axis, sign, width, height):
    
    for _img, fun in set.items():

        btn = Button(root,
                    text="",
                    bg='black',
                    fg='white',
                    image=_img,
                    border=0.5,
                    font=('Gill Sans MT', 12),
                    anchor=CENTER,
                    command=fun)
        btn.place(relx=X_Axis, rely=Y_Axis, relwidth=width, relheight=height)

        if sign == "+":
            Y_Axis += 0.1
        elif sign == "-":
            Y_Axis -= 0.1


# Creating a photoimage object to use image
img1 = PhotoImage(file="img/buttons/add.png")
img2 = PhotoImage(file="img/buttons/del.png")
img3 = PhotoImage(file="img/buttons/view.png")
img4 = PhotoImage(file="img/buttons/issue.png")
img5 = PhotoImage(file="img/buttons/return.png")
img6 = PhotoImage(file="img/buttons/f-icon.png")
img7 = PhotoImage(file="img/buttons/info-icon.png")
img8 = PhotoImage(file="img/buttons/search.png")

# Initializing the buttons and placing them
buttons = {
    img1: addBook,
    img2: delete,
    img3: View,
    img4: issueBook,
    img5: returnBook
}

putButtons(buttons, 0.28, 0.35, "+", 0.45, 0.1)

sideButtons = {

    img6 : feedBack,
    img7 : aboutUS,
    img8 : Search

}

putButtons(sideButtons, 0.03, 0.87, "-", 0.1, 0.1)

Label(root, text='v1.0.0',font=('Gill Sans MT', 12), padx=5).place(relx=0.91, rely=0.94)

# Restric t resizing
root.resizable(0,0)
root.mainloop()

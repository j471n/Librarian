from tkinter import font
from PIL import ImageTk, Image  #PIL -> Pillow
import pymysql
from addBook import *
from viewsBook import *
from deletebook import *
from issueBook import *
from returnBook import *
from os import getenv
from dotenv import load_dotenv
from feedback import feedBack
from about import aboutUS

load_dotenv()
# Function form viewsBook.py to connect DB


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


headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1,
                     text="Welcome to Librarian",
                     bg='black',
                     fg='white',
                     font=('Great Vibes', 28))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# Creating a photoimage object to use image
img1 = PhotoImage(file="img/buttons/add.png")
img2 = PhotoImage(file="img/buttons/del.png")
img3 = PhotoImage(file="img/buttons/view.png")
img4 = PhotoImage(file="img/buttons/issue.png")
img5 = PhotoImage(file="img/buttons/return.png")
img6 = PhotoImage(file="img/buttons/f-icon.png")
img7 = PhotoImage(file="img/buttons/info-icon.png")

# Resizing image to fit on button

btn1 = Button(root,text="", bg='black', fg='white', image=img1, border=0.5, compound=LEFT, padx=40, font=('Gill Sans MT', 12), anchor=CENTER, command=addBook)
btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="",bg='black', fg='white', image=img2, border=0.5,compound=LEFT, padx=25, font=('Gill Sans MT', 12),anchor=CENTER, command=delete)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="",bg='black', fg='white', image=img3, border=0.5,compound=LEFT, padx=25, font=('Gill Sans MT', 12), anchor=CENTER,command=View)
btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="",bg='black', fg='white', image=img4, border=0.5,compound=LEFT, padx=40, font=('Gill Sans MT', 12), anchor=CENTER,command=issueBook)
btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="",bg='black', fg='white', image=img5, border=0.5,compound=LEFT, padx=25, font=('Gill Sans MT', 12),anchor=CENTER, command=returnBook)
btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)

btn6 = Button(root, text="", bg='black', border = 0.8, image=img6, compound=LEFT, padx=25, font=('Gill Sans MT', 12), anchor=CENTER, command=feedBack)
btn6.place(relx=0.03, rely=0.87, relwidth=0.1, relheight=0.1)

btn7 = Button(root, text="", bg='black', border = 0.8, image=img7, compound=LEFT, padx=25, font=('Gill Sans MT', 12), anchor=CENTER, command=aboutUS)
btn7.place(relx=0.03, rely=0.77, relwidth=0.1, relheight=0.1)


Label(root, text='v1.0.0',font=('Gill Sans MT', 12), padx=5).place(relx=0.91, rely=0.94)


root.resizable(0,0)
root.mainloop()

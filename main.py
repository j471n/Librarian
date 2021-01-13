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

load_dotenv()
# Function form viewsBook.py to connect DB
connectDB()


root = Tk()
root.title("Librarian")
root.iconbitmap('img/logo.ico')
root.minsize(width=400, height=400)
root.geometry("600x500")


# 1.4

# same = True
# n = 0.25

# Adding a background image
background_image = Image.open("img/librarian.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(100, 250, image=img)
Canvas1.config(bg="white", width=imageSizeWidth, height=imageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)



headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1,
                     text="Welcome to Librarian",
                     bg='black',
                     fg='white',
                     font=('Great Vibes', 28))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


# Creating a photoimage object to use image
img1 = PhotoImage(file="img/buttons/add2-32.png")
img2 = PhotoImage(file="img/buttons/del-32.png")
img3 = PhotoImage(file="img/buttons/info-32.png")
img4 = PhotoImage(file="img/buttons/issue2-32.png")
img5 = PhotoImage(file="img/buttons/return-32.png")
# addB = img1.subsample(3, 3)

# Resizing image to fit on button

btn1 = Button(root,text="Add Book", bg='black', fg='white', image=img1, compound=LEFT, padx=25, font=('Gill Sans MT', 12), command=addBook)
btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Book",bg='black', fg='white', image=img2, compound=LEFT, padx=25, font=('Gill Sans MT', 12), command=delete)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Details",bg='black', fg='white', image=img3, compound=LEFT, padx=25, font=('Gill Sans MT', 12), command=View)
btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Issue Book",bg='black', fg='white', image=img4, compound=LEFT, padx=25, font=('Gill Sans MT', 12), command=issueBook)
btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Return Book",bg='black', fg='white', image=img5, compound=LEFT, padx=25, font=('Gill Sans MT', 12), command=returnBook)
btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)
root.resizable(0,0)
root.mainloop()

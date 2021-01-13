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
photo = PhotoImage(file ='img/logo.png')
root.iconphoto(False, photo)
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


btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
root.resizable(0,0)
root.mainloop()

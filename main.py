# Importing Files

from tkinter import *
from PIL import ImageTk, Image
from packages.addBook import *
from packages.viewsBook import *
from packages.deletebook import *
from packages.issueBook import *
from packages.returnBook import *
from os import getenv
from dotenv import load_dotenv
from packages.feedback import feedBack
from packages.about import aboutUS
from packages.search import Search
from packages.shelvesUpdation import UpdateShelves

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


# Creating a photoimage object to use image
img1 = PhotoImage(file="img/buttons/add.png")
img2 = PhotoImage(file="img/buttons/del.png")
img3 = PhotoImage(file="img/buttons/view.png")
img4 = PhotoImage(file="img/buttons/issue.png")
img5 = PhotoImage(file="img/buttons/return.png")
img6 = PhotoImage(file="img/buttons/f-icon.png")
img7 = PhotoImage(file="img/buttons/info-icon.png")
img8 = PhotoImage(file="img/buttons/search.png")
img9 = PhotoImage(file="img/buttons/updateBtn.png")

# Initializing the buttons and placing them
buttons = {
    img1: addBook,
    img2: delete,
    img3: View,
    img4: issueBook,
    img5: returnBook
}

# from modules.func
Function.putButtons(root, buttons, 0.28, 0.35, "+", 0.45, 0.1, bd=0.5, direction=VERTICAL)

sideButtons = {

    img6 : feedBack,
    img7 : aboutUS,
    img8 : Search,
    img9 : UpdateShelves

}

# from modules.func
Function.putButtons(root, sideButtons, 0.03, 0.87, "-", 0.1, 0.1, bd=0.5, direction=VERTICAL)

Label(root, text='v1.0.0',font=('Gill Sans MT', 12), padx=5).place(relx=0.91, rely=0.94)

# Restrict resizing
root.resizable(0,0)
root.mainloop()

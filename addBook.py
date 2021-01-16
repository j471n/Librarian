from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# Adding book to Database
def bookRegister():

    book_id = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    publication = bookInfo4.get()
    status = bookInfo5.get()
    status = status.lower()

    insertBooks = "INSERT INTO " + bookTable + " VALUES ('" + book_id + "','" + title + "','" + author + "','" + publication + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")
        print(messagebox.ERROR)
    print("Book ID : ",book_id)
    print("Book Title : ", title)
    print("Book Author : ",author)
    print("Publication : ", publication)
    print("Status : ", status)
    root.destroy()


def addBook():

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4,bookInfo5, Canvas1, con, cur, bookTable, root

    root = Toplevel()
    root.title("Add Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap('img/logo.ico')

    con = pymysql.connect(host="localhost", user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
    cur = con.cursor()  #cur -> cursor

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/addBook.jpg")
    bg = bg.resize((600, 500), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    bookTable = "books"  # Book Table

    # A container
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Add Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Label Frame
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.35, rely=0.2, relwidth=0.52, relheight=0.08)

    # Title
    lb2 = Label(labelFrame,
                text="Title : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.35, rely=0.35, relwidth=0.52, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame,
                text="Author : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.35, rely=0.50, relwidth=0.52, relheight=0.08)

    # Book Publication
    lb4 = Label(labelFrame,
                text="Publication : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.35, rely=0.65, relwidth=0.52, relheight=0.08)

    # Book Status

    lb5 = Label(labelFrame,
                text="Status(Avail/issued) : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb5.place(relx=0.05, rely=0.80, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.35, rely=0.80, relwidth=0.52, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root,
                       text="Submit",
                       bg='#d1ccc0',
                       fg='black',
                       command=bookRegister,
                       font=('Gill Sans MT', 12))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Cancel Button
    cancelBtn = Button(root,
                       text="Cancel",
                       bg='#f7f1e3',
                       fg='black',
                       command=root.destroy,
                       font=('Gill Sans MT', 12))
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()
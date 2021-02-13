from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from os import getenv
from dotenv import load_dotenv
import re

load_dotenv()

# Connecting the Database
con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()  
# Adding book to Database
def bookRegister(event=None):

    book_id = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    publication = bookInfo4.get()
    status = bookInfo5.lower()
    pos = bookInfo6.get()

    # Checking that Every field should contain values
    if status != "available" or book_id == "" or author == "" or title == "" or publication == "":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return

    # Checking that Position of the Bok Should inclue -, _, and Digits
    if not any(re.findall(r'-|_|/|\d', pos, re.IGNORECASE)) or not re.sub('[^\d.,]' , '', pos):
        root.destroy()
        messagebox.showerror("Failed", "Location Field should include '-' or '_' and Numbers (0-9)")
        return

    # SQL Queries
    insertBooks = f"INSERT INTO {bookTable} (book_id, title, author, publication, status, phylocation) VALUES ('{book_id}', '{title}', '{author}', '{publication}','{status}', '{pos}');"
    insertPosition = f"INSERT INTO {posTable} (bid, location) VALUES ('{book_id}', '{pos}');"
    verify = f"SELECT bid, location FROM {posTable};"

    # Executing Queries and checking that bookID and Location is Already in the DB or not
    try:
        cur.execute(verify)
        con.commit()

        for row in cur:
            if book_id == row[0]:
                print("Book Id Already Exist")
                root.destroy()
                messagebox.showwarning("Warning", f"Book id ({book_id}) Already Exist.")
                return

            if pos == row[1]:
                print("Location is Already Reserved")

                cur.execute(f"SELECT title FROM books WHERE phyLocation =  '{pos}';")
                con.commit()
                bTitle = [val for val in cur]

                root.destroy()
                messagebox.showwarning("Warning", f"Position ({pos}) Already Reserved by - {bTitle[0][0]}")
                return

        cur.execute(insertBooks)
        cur.execute(insertPosition)
        con.commit()

        messagebox.showinfo('Success', f"Book Added Successfully. It should be at {pos} in Physical Library")
    except:
        messagebox.showerror("Error", "Can't Add Data Into Database")


    con.close()
    print("Book ID : ",book_id)
    print("Book Title : ", title)
    print("Book Author : ",author)
    print("Publication : ", publication)
    print("Status : ", status)
    print("Position : ", pos)
    root.destroy()



def addBook():

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4,bookInfo5, bookInfo6, con, cur, bookTable, posTable, root

    # Initializing the Window
    root = Toplevel()
    root.title("Add Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap('img/logo.ico')

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/addBook.jpg")
    bg = bg.resize((600, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    # Tables Name
    bookTable = getenv('BOOK_TABLE')
    posTable = getenv('POSITION_TABLE')

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
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

    # Book ID
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb1.place(relx=0.1, rely=0.14, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.35, rely=0.15, relwidth=0.52, relheight=0.08)

    # Title
    lb2 = Label(labelFrame,
                text="Title : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb2.place(relx=0.1, rely=0.29, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.35, rely=0.3, relwidth=0.52, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame,
                text="Author : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb3.place(relx=0.1, rely=0.44, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.35, rely=0.45, relwidth=0.52, relheight=0.08)

    # Book Publication
    lb4 = Label(labelFrame,
                text="Publication : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb4.place(relx=0.1, rely=0.59, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.35, rely=0.60, relwidth=0.52, relheight=0.08)

    # Book Status
    bookInfo5 = 'Available'

    # Position of the Book
    lb6 = Label(labelFrame,
                text="Location : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 12))
    lb6.place(relx=0.1, rely=0.74, relheight=0.08)

    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.35, rely=0.75, relwidth=0.52, relheight=0.08)

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

    root.bind('<Return>', bookRegister)
    root.resizable(0, 0)
    root.mainloop()
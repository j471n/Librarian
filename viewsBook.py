from tkinter import *
import PIL
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv
from tkinter import ttk
import modules.func as Function

load_dotenv()

# Function to connect if database does not exist
def connectDB():
    try:
        global con, cur
        # Connecting to the Database
        con = pymysql.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
        cur = con.cursor()  #cur -> cursor
        print("Database Connected, Already Existed.")

    except:

        # SQL
        q1 = f"CREATE DATABASE {getenv('DB_NAME')};"
        q2 = f"use {getenv('DB_NAME')};"
        q3 = 'CREATE TABLE books (book_id VARCHAR(200) PRIMARY KEY, title VARCHAR(50), author VARCHAR(30),publication VARCHAR(100), status VARCHAR(30), phyLocation VARCHAR(50), issued_date VARCHAR(15), issued_to VARCHAR(25));'
        q4 = "CREATE TABLE position (bid VARCHAR(200) PRIMARY KEY, location VARCHAR(50));"
        con = pymysql.connect(host = getenv('HOST'), user = getenv('USER'), password = getenv('DB_PASS'))
        cur = con.cursor()

        cur.execute(q1)
        con.commit()
        cur.execute(q2)
        con.commit()
        cur.execute(q3)
        con.commit()
        cur.execute(q4)
        con.commit()

        # Connecting to the Database
        con = pymysql.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
        cur = con.cursor()
        print("Database Connected, New Created")


connectDB()
# Enter Table Names here
bookTable = getenv('BOOK_TABLE')


def View():


    root = Toplevel()
    root.title("View Details")
    root.minsize(width=400, height=400)
    root.geometry("1000x700")
    root.iconbitmap('img/logo.ico')
    #Adding Image to Add Book
    global img
    bg = PIL.Image.open("img/background/viewsBook.jpg")
    bg = bg.resize((1000, 700), PIL.Image.ANTIALIAS)
    img = PIL.ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    # Heading Frame - Container
    headingFrame1 = Frame(root, bg="#FFBB00", bd=4)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)
    # Heading Frame - Label
    headingLabel = Label(headingFrame1,
                         text="View Books",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Select All books from the Library
    getBooks = f"SELECT * FROM {bookTable} ORDER BY status;"
    
    # Creating the Treeview and Scrolling
    Function.createTable(dir=root, height=0.6,width=1, marginX=0., marginY=0.25, query=getBooks, scroll="yes", sMarginX=0.988, sMarginY=0.285, sheight=0.56, swidth=0.012)

    # Total Books Query
    length = f"SELECT COUNT(*), (SELECT COUNT(*) FROM books WHERE status = 'available') AS Avail FROM books;"
    cur.execute(length)
    con.commit()
    Books = [value for value in cur]

    # Label to Print Total Books
    Label(root, text=f"Total Books : {Books[0][0]}\nAvailable : {Books[0][1]}\nIssued : {Books[0][0]-Books[0][1]}",font=('Gill Sans MT', 12), padx=5, anchor=E).place(relx=0.88, rely=0.89)

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Gill Sans MT', 12), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv
from tkinter import ttk

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
    bg = Image.open("img/background/viewsBook.jpg")
    bg = bg.resize((1000, 700), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg)
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



    # TREEVIEW in View Window
    detail_tree = ttk.Treeview(root)
    detail_tree.pack()

    # ScrollBar Adding to Treeview
    tree_scroll = Scrollbar(root, orient="vertical", command=detail_tree.yview)
    tree_scroll.place(relx=0.988, rely=0.285, relheight=0.56, relwidth=0.012)
    detail_tree.configure(yscrollcommand=tree_scroll.set)

    detail_tree['columns'] = ("BID", "Title", "Author", "Publication", "Status", "P-Location", "Issued Date", "Issued To")

    #Heading List
    detail_tree.heading("#0", text="")
    detail_tree.heading("BID", text="BID", anchor=CENTER)
    detail_tree.heading("Title", text="Title", anchor=CENTER)
    detail_tree.heading("Author", text="Author", anchor=CENTER)
    detail_tree.heading("Publication", text="Publication", anchor=CENTER)
    detail_tree.heading("Status", text="Status", anchor=CENTER)
    detail_tree.heading("P-Location", text="P-Location", anchor=CENTER)
    detail_tree.heading("Issued Date", text="Issued Date", anchor=CENTER)
    detail_tree.heading("Issued To", text="Issued To", anchor=CENTER)
    # Colums List
    detail_tree.column('#0', width=0, stretch=NO)
    detail_tree.column('BID', width=10, anchor=CENTER)
    detail_tree.column('Title', width=20, anchor=CENTER)
    detail_tree.column('Author', width=10, anchor=CENTER)
    detail_tree.column('Publication', width=20, anchor=CENTER)
    detail_tree.column('Status', width=10, anchor=CENTER)
    detail_tree.column('P-Location', width=10, anchor=CENTER)
    detail_tree.column('Issued Date', width=10, anchor=CENTER)
    detail_tree.column('Issued To', width=10, anchor=CENTER)

    # Styling Treeview
    style = ttk.Style()
    style.configure("Treeview",
                    background='#d3d3d3',
                    foreground="black",
                    rowheight=30,
                    font=('Arial', 9))

    style.map("Treeview",
              background=[('selected', 'green'), ('active', '#D3D3D3')])

    #Fetching data from database
    getBooks = f"SELECT * FROM {bookTable} ORDER BY status;"
    count = 0
    try:
        cur.execute(getBooks)
        con.commit()

        # Adding Data to the Treeview Table
        for data in cur:
            data = list(data)
            # print(data)

            # Checking if the column is None then change the value to -
            for i in range(len(data)):
                if data[i] == None:
                    data[i] = '-'

            # Inserting in the Treeview
            detail_tree.insert(parent='', index=END, iid=count, text="",
                    values=(
                        data[0],
                        data[1].capitalize(),
                        data[2].capitalize(),
                        data[3].capitalize(),
                        data[4].capitalize(),
                        data[5],
                        data[6],
                        data[7].capitalize()
                    )
            )
            count += 1

        detail_tree.place(relx=0, rely=0.25, relwidth=1, relheight=0.6)
    except:
        messagebox.showinfo("Failed to fetch files from database")


    # Total Books Query
    length = f"SELECT COUNT(*), (SELECT COUNT(*) FROM books WHERE status = 'available') AS Avail FROM books;"
    cur.execute(length)
    con.commit()
    Books = [value for value in cur]

    # Label to Print Total Books
    Label(root, text=f"Total Books : {Books[0][0]}\nAvailable Book : {Books[0][1]}\nIssued Books : {Books[0][0]-Books[0][1]}",font=('Gill Sans MT', 12), padx=5, anchor=E).place(relx=0.86, rely=0.89)

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Gill Sans MT', 12), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()
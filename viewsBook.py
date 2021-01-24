from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv
from tkinter import ttk

load_dotenv()

def connectDB():
    try:
        global con, cur
        con = pymysql.connect(host="localhost",
                            user=getenv('USER'),
                            password=getenv('DB_PASS'),
                            database=getenv('DB_NAME'))
        cur = con.cursor()  #cur -> cursor
        print("Database Connected, Already Existed.")

    except:
        q1 = f"CREATE DATABASE {getenv('DB_NAME')};"
        q2 = f"use {getenv('DB_NAME')};"
        q3 = 'CREATE TABLE books (book_id VARCHAR(200) PRIMARY KEY, title VARCHAR(50), author VARCHAR(30),publication VARCHAR(100), status VARCHAR(30), issued_date VARCHAR(15), issued_to VARCHAR(25));'
        q4 = "CREATE TABLE books_issued (bid VARCHAR(200) PRIMARY KEY, issuedto VARCHAR(50),issued_date VARCHAR(15));"
        con = pymysql.connect(host="localhost", user='root', password='root')
        cur = con.cursor()

        cur.execute(q1)
        con.commit()
        cur.execute(q2)
        con.commit()
        cur.execute(q3)
        con.commit()
        cur.execute(q4)
        con.commit()

        con = pymysql.connect(host="localhost",
                              user='root',
                              password='root',
                              database=getenv('DB_NAME'))
        cur = con.cursor()
        print("Database Connected, New Created")


connectDB()
# Enter Table Names here
bookTable = "books"



# def GetBooks(labelFrame, i , y):

#     Label(labelFrame, fg='black', bg='white', width=10, pady=2, text=i[0], font=('Gill Sans MT', 10)).grid(row=y, column=0)
#     Label(labelFrame, bg='black', fg='white', width=20, pady=2, text=i[1], font=('Gill Sans MT', 10)).grid(row=y, column=1)
#     Label(labelFrame, fg='black', bg='white', width=20, pady=2, text=i[2], font=('Gill Sans MT', 10)).grid(row=y, column=2)
#     Label(labelFrame, bg='black', fg='white', width=20, pady=2, text=i[3], font=('Gill Sans MT', 10)).grid(row=y, column=3)
#     Label(labelFrame, fg='black', bg='white', width=12, pady=2, text=i[4], font=('Gill Sans MT', 10)).grid(row=y, column=4)

def View():

    root = Toplevel()
    root.title("View Details")
    root.minsize(width=400, height=400)
    root.geometry("900x500")
    root.iconbitmap('img/logo.ico')

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/viewsBook.jpg")
    bg = bg.resize((900, 500), Image.ANTIALIAS)
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
    tree_scroll.place(relx=0.985, rely=0.3, relheight=0.54, relwidth=0.015)
    detail_tree.configure(yscrollcommand=tree_scroll.set)

    detail_tree['columns'] = ("BID", "Title", "Author", "Publication", "Status", "Issued Date", "Issued To")

    #Heading List
    detail_tree.heading("#0", text="")
    detail_tree.heading("BID", text="BID", anchor=CENTER)
    detail_tree.heading("Title", text="Title", anchor=CENTER)
    detail_tree.heading("Author", text="Author", anchor=CENTER)
    detail_tree.heading("Publication", text="Publication", anchor=CENTER)
    detail_tree.heading("Status", text="Status", anchor=CENTER)
    detail_tree.heading("Issued Date", text="Issued Date", anchor=CENTER)
    detail_tree.heading("Issued To", text="Issued To", anchor=CENTER)
    # Colums List
    detail_tree.column('#0', width=0, stretch=NO)
    detail_tree.column('BID', width=10, anchor=CENTER)
    detail_tree.column('Title', width=20, anchor=CENTER)
    detail_tree.column('Author', width=10, anchor=CENTER)
    detail_tree.column('Publication', width=20, anchor=CENTER)
    detail_tree.column('Status', width=10, anchor=CENTER)
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
    getBooks = "SELECT * FROM " + bookTable + ";"
    count = 0
    try:
        cur.execute(getBooks)
        con.commit()

        # Adding Data to the Treeview Table
        for data in cur:
            data = list(data)
            print(data)

            # Checking if the column is None then change the value to -
            for i in range(len(data)):
                if data[i] == None:
                    data[i] = '-'


            detail_tree.insert(parent='', index=END, iid=count, text="",
                    values=(
                        data[0],
                        data[1].capitalize(),
                        data[2].capitalize(),
                        data[3].capitalize(),
                        data[4].capitalize(),
                        data[5],
                        data[6].capitalize()
                    )
            )
            count += 1

        detail_tree.place(relx=0, rely=0.25, relwidth=1, relheight=0.6)
    except:
        messagebox.showinfo("Failed to fetch files from database")


    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('Gill Sans MT', 12), command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()
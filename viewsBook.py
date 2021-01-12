from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv

load_dotenv()

con = pymysql.connect(host="localhost",
                      user=getenv('USER'),
                      password=getenv('DB_PASS'),
                      database=getenv('DB_NAME'))
cur = con.cursor()  #cur -> cursor

# Enter Table Names here
bookTable = "books"



def GetBooks(labelFrame, i , y):

    Label(labelFrame, fg='black', bg='white', width=10, pady=2, text=i[0]).grid(row=y, column=0)
    Label(labelFrame, bg='black', fg='white', width=20, pady=2, text=i[1]).grid(row=y, column=1)
    Label(labelFrame, fg='black', bg='white', width=20, pady=2, text=i[2]).grid(row=y, column=2)
    Label(labelFrame, bg='black', fg='white', width=20, pady=2, text=i[3]).grid(row=y, column=3)
    Label(labelFrame, fg='black', bg='white', width=12, pady=2, text=i[4]).grid(row=y, column=4)

def View():

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Canvas1 Properties
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

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

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0, rely=0.25, relwidth=1, relheight=0.6)

    Label(labelFrame, bg='black', fg='white',width=10, pady=5, text="BID").grid(row=0, column=0)
    Label(labelFrame, fg='black', bg='white',width=20, pady=5, text="Title").grid(row=0, column=1)
    Label(labelFrame, bg='black', fg='white',width=20, pady=5, text="Author").grid(row=0, column=2)
    Label(labelFrame, fg='black', bg='white',width=20, pady=5, text="Publication").grid(row=0, column=3)
    Label(labelFrame, bg='black', fg='white',width=12, pady=5, text="Status").grid(row=0, column=4)


    getBooks = "SELECT * FROM " + bookTable + ";"
    y = 2
    try:
        cur.execute(getBooks)
        s = con.commit()
        print(s)

        for i in cur:
            GetBooks(labelFrame, i, y)
            y += 1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()
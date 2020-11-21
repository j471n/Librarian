from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


# Database Name and Password
mypass = "root"
mydatabase = "db"

# Connecting the MySql server
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"


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
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    # Heading Frame - Label
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame,
          text="%-10s%-25s%-30s%-30s%-5s" % ('BID', 'Title', 'Author', 'Publication', 'Status'),
          bg='black',
          fg='white').place(relx=0.07, rely=0.1)


    # lINE LABEL
    Label(
        labelFrame,
        text=
        "________________________________________________________________________________",
        bg='black',
        fg='white').place(relx=0.05, rely=0.16)
    getBooks = "SELECT * FROM " + bookTable + ";"
    try:
        cur.execute(getBooks)
        s = con.commit()
        print(s)

        for i in cur:
            Label(labelFrame,
                  text="%-10s%-25s%-30s%-30s%-5s" % (i[0], i[1], i[2], i[3], i[4]),
                  bg='black',
                  fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # Quit Button
    quitBtn = Button(root,
                     text="Quit",
                     bg='#f7f1e3',
                     fg='black',
                     command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
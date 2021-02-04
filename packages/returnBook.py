from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from os import getenv
from dotenv import load_dotenv
import modules.func as Function

load_dotenv()

# Connecting to the DB
con = pymysql.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
cur = con.cursor()  #cur -> cursor

# Enter Table Names here
bookTable = getenv('BOOK_TABLE')
posTable = getenv('POSITION_TABLE')

# Getting values and checking that values are correct Printing where to put the book
def returnn(event=None):

    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status, check, title, pos

    bid = bookInfo1.get()

    if bid == "":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return

    # Checking bookID is correct or not
    if Function.bookIdChecker(bid) == 1: 
        root.destroy()
        return

    try:
        getLocation = f"SELECT location FROM {posTable} WHERE bid = '{bid}';"
        cur.execute(getLocation)
        con.commit()
        for i in cur:
            pos = i[0]

        print(pos)
    except:
        root.destroy()
        messagebox.showerror("Error", "Book ID is Invalid. (Can't Fetch from the Database)")
        return


    # SQL
    updateStatus = f"UPDATE {bookTable} SET status = 'available', phyLocation = '{pos}', issued_date = NULL, issued_to = NULL WHERE book_id = '{bid}';"
    checkAvail = f"SELECT status, title FROM {bookTable} WHERE book_id = '{bid}';"

    # Executing query and checking isBook issued or not
    try:
        cur.execute(checkAvail)
        con.commit()
        for field in cur:
            global s
            check = field[0]
            title = field[1]
            print(check)

        if check == 'issued':
            cur.execute(updateStatus)
            con.commit()
            root.destroy()
            messagebox.showinfo('Success', f"Book Name - {title}\nBook Successfully Returned. Put the Book at '{pos}'")
            return

        elif check == 'available':
            root.destroy()
            messagebox.showwarning('Warning', "The Book has not been Issued Yet.")
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again.")
    root.destroy()


def returnBook():

    global bookInfo1, SubmitBtn, cancelBtn, Canvas1, con, cur, root, labelFrame, lb1

    # Initializing the window
    root = Toplevel()
    root.title("Return Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap('img/logo.ico')

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/returnBook.jpg")
    bg = bg.resize((600, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    # Heading Frame and Label
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Return Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Content Frame
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.4)

    # Book ID to Delete
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb1.place(relx=0.1, rely=0.114)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4, rely=0.15, relwidth=0.5)

    # Feedback
    lb2 = Label(labelFrame,
                text="Feedback :\n(optional)  ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb2.place(relx=0.1, rely=0.314)

    bookInfo2 = Text(labelFrame,
                     height=5,
                     padx=10,
                     pady=10,
                     font=('Gill Sans MT', 10))
    bookInfo2.place(relx=0.4, rely=0.3, relwidth=0.5)

    #Submit Button
    SubmitBtn = Button(root,
                       text="Return",
                       bg='#d1ccc0',
                       fg='black',
                       font=('Gill Sans MT', 12),
                       command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Cancel Button
    cancelBtn = Button(root,
                     text="Cancel",
                     bg='#f7f1e3',
                     fg='black',
                     font=('Gill Sans MT', 12),
                     command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.bind('<Return>', returnn)
    root.resizable(0, 0)
    root.mainloop()
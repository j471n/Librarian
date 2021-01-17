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
issueTable = "books_issued"
bookTable = "books"

allBid = []  #To store all the Book ID’s


def returnn(event):

    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status, check

    bid = bookInfo1.get()

    if bid=="":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return

    extractBid = "SELECT bid FROM " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "SELECT status FROM " + bookTable + " WHERE book_id = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    # SQL Query
    issueSql = "DELETE FROM " + issueTable + " WHERE bid = '" + bid + "'"
    updateStatus = "UPDATE " + bookTable + " SET status = 'avail' WHERE book_id = '" + bid + "'"

    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            root.destroy()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            root.destroy()
            messagebox.showinfo('Message', "Please check the book ID")
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()




def returnBook():

    global bookInfo1, SubmitBtn, cancelBtn, Canvas1, con, cur, root, labelFrame, lb1

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

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Return Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID to Delete
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb1.place(relx=0.1, rely=0.364)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4, rely=0.4, relwidth=0.5)

    #Submit Button
    SubmitBtn = Button(root,
                       text="Return",
                       bg='#d1ccc0',
                       fg='black',
                       font=('Gill Sans MT', 12),
                       command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

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
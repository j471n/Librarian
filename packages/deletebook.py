from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from os import getenv
from dotenv import load_dotenv
import modules.func as Function

load_dotenv()

# Connecting to the Database
con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()  #cur -> cursor

# Table Name and Minimum Length
bookTable = getenv('BOOK_TABLE')
posTable = getenv('POSITION_TABLE')
MIN_LENGTH = 15

# To Check the Length of the Reason
def checkWords(self):
    global counter, length, reason

    reason = bookInfo2.get('1.0', END).strip()
    length = len(list(reason.split(" "))) - 1
    if length <= MIN_LENGTH:
        counter.config(text=MIN_LENGTH-length)

# Get the Fields value and  Checking that Every thing has a value and Check reason is of enough length
def deleteBook(event=None):

    bid = bookInfo1.get()
    print("Reason : ", reason)
    print("bid : ", bid)

    if bid == "":
        root.destroy()
        messagebox.showerror("Failed", "Book ID is Mandatory")
        return
    elif length < MIN_LENGTH:
        root.destroy()
        messagebox.showerror('Failed', f"Length of the Reason Field must be {MIN_LENGTH}")
        return

    # Checking bookID is correct or not
    if Function.bookIdChecker(bid) == 1:
        root.destroy()
        return

    # SQL
    deleteSql = f"DELETE FROM {bookTable} WHERE book_id = '{bid}';"
    deletePosition = f"DELETE FROM {posTable} WHERE bid = '{bid}';"
    book_details = f"SELECT title, status, issued_to FROM {bookTable} WHERE book_id = '{bid}';"
    global BookName, BookStatus, issuedTO

    # Executing the Queries
    try:
        cur.execute(book_details)
        con.commit()
        for data in cur:
            BookName = data[0].capitalize()
            BookStatus = data[1]
            issuedTO = data[2].capitalize()

        if BookStatus == "issued":
            answer = messagebox.askyesno("Confirm", f"The Book ({BookName}) is already issued to - {issuedTO}.\nDo you really want to delete the Book?")
            if answer == False:
                root.destroy()
                messagebox.showinfo("Failed", "You've chosen not to delete the Book")
                return


        if BookName != "":
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deletePosition)
            con.commit()

            root.destroy()
            messagebox.showinfo('Success', f"Book Name - {BookName}\nBook Record Deleted Successfully")
        else:
            print("Something went wrong")

    except:
        messagebox.showinfo('Failed', "You've Entered the Wrong Book ID.")

    root.destroy()
    return


def delete():

    global bookInfo1, bookInfo2, Canvas1, con, cur, root, counter

    #Initializing the Window
    root = Toplevel()
    root.title("Delete Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap('img/logo.ico')

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/deleteBook.jpg")
    bg = bg.resize((800, 750), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    # Heading Frame and Label
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Delete Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Content/Label Frame
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb1.place(relx=0.1, rely=0.1)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.125, relwidth=0.52)

    # Reason Should be 15 length
    lb2 = Label(labelFrame,
                text="Reason : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb2.place(relx=0.1, rely=0.325)

    bookInfo2 = Text(labelFrame,
                     height=5,
                     padx=10,
                     pady=10,
                     font=('Gill Sans MT', 12))
    bookInfo2.place(relx=0.3, rely=0.3, relwidth=0.52)

    # Counter Label
    counter = Label(labelFrame,
                    text=MIN_LENGTH,
                    bg='black',
                    fg='white',
                    font=('Gill Sans MT', 12))
    counter.place(relx=0.15, rely=0.425)

    #Submit Button
    SubmitBtn = Button(root,
                       text="Submit",
                       bg='#d1ccc0',
                       fg='black',
                       font=('Gill Sans MT', 12),
                       command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Cancel Button
    cancelBtn = Button(root,
                     text="Cancel",
                     bg='#f7f1e3',
                     fg='black',
                     font=('Gill Sans MT', 12),
                     command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # Running SendEmail on Enter
    root.bind_all("<KeyPress>", checkWords)
    root.resizable(0, 0)
    root.mainloop()
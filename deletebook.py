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
issueTable = "books_issued"



def deleteBook(event=None):

    bid = bookInfo1.get()
    reason = bookInfo2.get()

    if bid == "" or reason == "":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return  

    deleteSql = "DELETE FROM " + bookTable + " WHERE book_id = '" + bid + "'"
    book_name = "SELECT title FROM " + bookTable + " WHERE book_id = '" + bid + "'"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(book_name)
        con.commit()

        messagebox.showinfo('Success', "Book Record Deleted Successfully")

    except:
        messagebox.showinfo('Failed', "You've Entered the Wrong Book ID.")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():

    global bookInfo1, bookInfo2, Canvas1, con, cur, root

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

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Delete Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb1.place(relx=0.05, rely=0.3)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.325, relwidth=0.52)

    lb2 = Label(labelFrame,
                text="Reason : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb2.place(relx=0.05, rely=0.6)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.625, relwidth=0.52)
    # print("Reason : ", bookInfo2.get())

    #Submit Button
    SubmitBtn = Button(root,
                       text="Submit",
                       bg='#d1ccc0',
                       fg='black',
                       font=('Gill Sans MT', 12),
                       command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    cancelBtn = Button(root,
                     text="Cancel",
                     bg='#f7f1e3',
                     fg='black',
                     font=('Gill Sans MT', 12),
                     command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # Running SendEmail on Enter
    root.bind('<Return>', deleteBook)
    root.resizable(0, 0)
    root.mainloop()
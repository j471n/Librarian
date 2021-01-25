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
MIN_LENGTH = 15

# To Check the Length of the Reason
def checkWords(self):
    global counter, lenght

    reason = bookInfo2.get('1.0', END).strip()
    lenght = len(list(reason.split(" "))) - 1
    if lenght <= MIN_LENGTH:
        counter.config(text=MIN_LENGTH-lenght)


def deleteBook(event=None):

    bid = bookInfo1.get()
    reason = bookInfo2.get('1.0', END)
    print("Reason : ", reason)

    if bid == "":
        root.destroy()
        messagebox.showerror("Failed", "Book ID is Mandatory")
        return
    elif lenght < MIN_LENGTH:
        root.destroy()
        messagebox.showerror('Failed', f"Lenght of the Reason Field must be {MIN_LENGTH}")
        return

    deleteSql = f"DELETE FROM {bookTable} WHERE book_id = {bid};"
    book_name = f"SELECT title FROM {bookTable} WHERE book_id = {bid};"

    global BookName

    try:
        cur.execute(book_name)
        con.commit()
        for name in cur:
            BookName = name[0]
        cur.execute(deleteSql)
        con.commit()

        messagebox.showinfo('Success', f"Book Name - {BookName}\nBook Record Deleted Successfully")

    except:
        messagebox.showinfo('Failed', "You've Entered the Wrong Book ID.")

    root.destroy()


def delete():

    global bookInfo1, bookInfo2, Canvas1, con, cur, root, counter

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
    lb1.place(relx=0.1, rely=0.1)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.125, relwidth=0.52)

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

    cancelBtn = Button(root,
                     text="Cancel",
                     bg='#f7f1e3',
                     fg='black',
                     font=('Gill Sans MT', 12),
                     command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # Running SendEmail on Enter
    root.bind_all("<KeyPress>", checkWords)
    # root.bind('<Return>', deleteBook)
    root.resizable(0, 0)
    root.mainloop()
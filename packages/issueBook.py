from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import messagebox
from os import getenv
import pymysql
from datetime import date
from dotenv import load_dotenv
import modules.func as Function

load_dotenv()

# Connecting to DB
con = pymysql.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
cur = con.cursor()  #cur -> cursor

# Enter Table Names here
bookTable = getenv('BOOK_TABLE')

# Getting values and checking that every field should have value
def issue(event=None):

    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, cancelBtn, root, Canvas1, status, check, Date,location, issuedName

    bid = inf1.get()
    issueto = inf2.get()
    issueDate = date.today().strftime("%b %d, %Y")

    if bid == "" or issueto == "":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return

    # Checking bookID is correct or not
    if Function.bookIdChecker(bid) == 1: 
        root.destroy()
        return


    # SQL
    updateStatus = f"UPDATE {bookTable} SET status = 'issued', phyLocation = NULL, issued_date = '{issueDate}', issued_to = '{issueto}' WHERE book_id = '{bid}';"
    issueDateAndName = f"SELECT issued_date, issued_to FROM {bookTable} WHERE book_id = '{bid}';"
    getBookDetails = f"SELECT title, phyLocation FROM {bookTable} WHERE book_id = '{bid}';"
    checkAvail = f"SELECT status FROM {bookTable} WHERE book_id = '{bid}';"

    # Executing Queries and checking for book status if already issued and fetching the details of the student
    try:
        cur.execute(checkAvail)
        con.commit()
        for field in cur:
            global s
            check = field[0]
            print(check)

        if check == 'issued':
            cur.execute(issueDateAndName)
            con.commit()

            # Fetching the Issue Date and the Student name
            for i in cur:
                Date = i[0]
                issuedName = i[1]
            root.destroy()
            messagebox.showinfo('Message', "Already Issued on " + str(Date) + " to " +  str(issuedName).capitalize())
            return
        elif check == 'available':
            cur.execute(getBookDetails)
            con.commit()

            bName = ""

            # Fetching the Bookname and the Location in Physical
            for i in cur:
                bName = i[0].capitalize()
                location = i[1]

            cur.execute(updateStatus)
            con.commit()
            root.destroy()
            messagebox.showinfo('Success', f"The Book '{bName}' is at '{location}'.\nSuccessfully Issued on " + str(issueDate) + " to " + str(issueto).capitalize())
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again.")
    root.destroy()




def issueBook():

    global issueBtn, labelFrame, lb1, inf1, inf2,inf3, cancelBtn, root, Canvas1, status

    # Initializing the window
    root = Toplevel()
    root.title("Issue Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    root.iconbitmap('img/logo.ico')

    #Adding Image to Add Book
    global img
    bg = Image.open("img/background/issueBook.jpg")
    bg = bg.resize((600, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bg)
    Label(root, image=img).pack()

    # Heading frame and Lable
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Issue Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Content Frame
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame,
                text="Book ID : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb1.place(relx=0.1, rely=0.25)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.4, rely=0.3, relwidth=0.5)

    # Issued To Student name
    lb2 = Label(labelFrame,
                text="Issued To : ",
                bg='black',
                fg='white',
                font=('Gill Sans MT', 14))
    lb2.place(relx=0.1, rely=0.51)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.4, rely=0.55, relwidth=0.5)

    #Issue Button
    issueBtn = Button(root,
                      text="Issue",
                      bg='#d1ccc0',
                      fg='black',
                      font=('Gill Sans MT', 12),
                      command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Cancel Button
    cancelBtn = Button(root,
                       text="Cancel",
                       bg='#aaa69d',
                       fg='black',
                       font=('Gill Sans MT', 12),
                       command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    # Running SendEmail on Enter
    root.bind('<Return>', issue)
    root.resizable(0, 0)
    root.mainloop()

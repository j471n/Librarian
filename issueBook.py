from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from os import getenv
import pymysql
from datetime import date
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

allBid = []  #To store all the Book ID’s



def issue():

    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, cancelBtn, root, Canvas1, status, check, Date, issuedName

    bid = inf1.get()
    issueto = inf2.get()
    issueDate = date.today().strftime("%b %d, %Y")

    extractBid = "SELECT book_id FROM " + bookTable
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

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "INSERT INTO " + issueTable + " VALUES ('" + bid + "','" + issueto + "','" + issueDate + "')"
    updateStatus = "UPDATE " + bookTable + " SET status = 'issued' WHERE book_id = '" + bid + "'"
    issueDateAndName = "SELECT issued_date, issuedto FROM " + issueTable + " WHERE bid = '" + bid + "'"

    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            root.destroy()
            messagebox.showinfo('Success', "Book Issued Successfully on " + str(issueDate) + " to " + str(issueto).capitalize())
        else:
            allBid.clear()
            cur.execute(issueDateAndName)
            con.commit()

            for i in cur:
                Date = i[0]
                issuedName = i[1]

            root.destroy()
            messagebox.showinfo('Message', "Already Issued on " + str(Date) + " to " +  str(issuedName).capitalize())
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again.")
    allBid.clear()




def issueBook():

    global issueBtn, labelFrame, lb1, inf1, inf2,inf3, cancelBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1,
                         text="Issue Book",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    #Issue Button
    issueBtn = Button(root,
                      text="Issue",
                      bg='#d1ccc0',
                      fg='black',
                      command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Cancel Button
    cancelBtn = Button(root,
                     text="Cancel",
                     bg='#aaa69d',
                     fg='black',
                     command=root.destroy)
    cancelBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.resizable(0, 0)
    root.mainloop()

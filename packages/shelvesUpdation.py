from tkinter import *
import sqlite3
from os import getenv
from dotenv import *
import tkinter.ttk as TTK
from tkinter import messagebox
# import func as Function
import modules.func as Function

env = find_dotenv('env/.env')
load_dotenv(env)

# Connecting to DB
con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()

# Book Table
bookTable = getenv('BOOK_TABLE')
posTable = getenv('POSITION_TABLE')


def update():

    # Checking Bid should have value
    print(bid, pos)
    if bid == "" or pos == "":
        root.destroy()
        messagebox.showerror("Failed", "All Fields are Required.")
        return

    # Position verificaion
    Function.positionVerification(div=root, position=pos)

    # SQL Queries
    query1 = f"UPDATE {bookTable} SET phyLocation = '{pos}' WHERE book_id = '{bid}';"
    query2 = f"UPDATE {posTable} SET location = '{pos}' WHERE bid = '{bid}';"

    check0 = f"SELECT location FROM {posTable};"
    check1 = f"SELECT status FROM {bookTable} WHERE book_id = '{bid}';"

    try:
        cur.execute(check0)
        con.commit()

        for row in cur:
            if pos == row[0]:
                print("Location is Already Reserved")
                root.destroy()
                messagebox.showwarning("Warning", f"Position ({pos}) Already Reserved.")
                return


        cur.execute(check1)
        con.commit()

        status = [val[0] for val in cur]

        if status[0] == 'available':
            cur.execute(query1)
            con.commit()

        cur.execute(query2)
        con.commit()

        root.destroy()
        messagebox.showinfo("Success", "Book Position Updated Successfully")
    except:
        messagebox.showerror("Failed", "Book ID is Incorrect")


# Changing the Button state on the basis of fields
def verify(self):

    global bid, pos
    bid = BidEntry.get()
    pos = positionEntry.get()
    try:
        if BidEntry.get() == "" or positionEntry.get() == "":
            updateButton.config(state=DISABLED)
        else:
            updateButton.config(state=NORMAL)
    except:
        print("Something Went wrong. Refresh Window.")


def UpdateShelves():
    global updateButton, root, positionEntry, BidEntry

    # Initializing the Search Window
    root = Toplevel()
    root.title("Update Location")
    root.iconbitmap('img/Updation.ico')
    root.geometry("250x250")

    # Title Lable
    Label(root, text="Update Book Location", font=('Gill Sans MT', 14), anchor=CENTER).place(rely=0.08, relwidth=1)

    # BID Lable and Entry
    Label(root, text="Enter Book ID", font=('Gill Sans MT', 11)).place(relx=0.05, rely=0.3)
    BidEntry = TTK.Entry(root)
    BidEntry.place(relx=0.53, relwidth=0.4, rely=0.3, relheight=0.12)

    # Position Label and Entry
    Label(root, text="Updated Location", font=('Gill Sans MT', 11)).place(relx=0.05, rely=0.5)
    positionEntry = TTK.Entry(root)
    positionEntry.place(relx=0.53, relwidth=0.4, rely=0.5, relheight=0.12)

    # Update Button
    updateButton = Button(root,
                          text='Update',
                          bd=0.5,
                          cursor='hand2',
                          state=DISABLED,
                          font=('Gill Sans MT', 12),
                          padx=25,
                          pady=5,
                          command=update)
    updateButton.place(relx=0.3, rely=0.75, relheight=0.15, relwidth=0.4)


    # Running Verify event on any key press
    root.bind_all("<KeyPress>", verify)

    # Running SendEmail on Enter
    root.bind('<Return>', update)
    root.resizable(0,0)
    root.mainloop()

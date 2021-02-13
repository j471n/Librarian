from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from os import getenv
from dotenv import*
import re
from .database import *


env = find_dotenv('env/.env')
load_dotenv(env)


# Connecting to DB
con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()

# Book Table
bookTable = getenv('BOOK_TABLE')
# root = Tk()

def createTable(dir,height=0.5, width=1, marginX=0.1, marginY=0.1, loopThrough=cur, query="", scroll="NO", sheight=0.6, swidth=0.01, sMarginX=0.9, sMarginY=0.2):
    detail_tree = ttk.Treeview(dir)
    # detail_tree.pack()

    # ScrollBar Adding to Treeview
    if scroll !="NO":
        tree_scroll = Scrollbar(dir, orient="vertical", command=detail_tree.yview)
        tree_scroll.place(relx=sMarginX, rely=sMarginY, relheight=sheight, relwidth=swidth)
        # tree_scroll.place(relx=0.988, rely=0.285, relheight=0.56, relwidth=0.012)
        detail_tree.configure(yscrollcommand=tree_scroll.set)

    detail_tree['columns'] = ("BID", "Title", "Author", "Publication", "Status", "P-Location", "Issued Date", "Issued To")

    #Heading List
    detail_tree.heading("#0", text="")
    detail_tree.heading("BID", text="BID", anchor=CENTER)
    detail_tree.heading("Title", text="Title", anchor=CENTER)
    detail_tree.heading("Author", text="Author", anchor=CENTER)
    detail_tree.heading("Publication", text="Publication", anchor=CENTER)
    detail_tree.heading("Status", text="Status", anchor=CENTER)
    detail_tree.heading("P-Location", text="P-Location", anchor=CENTER)
    detail_tree.heading("Issued Date", text="Issued Date", anchor=CENTER)
    detail_tree.heading("Issued To", text="Issued To", anchor=CENTER)
    # Colums List
    detail_tree.column('#0', width=0, stretch=NO)
    detail_tree.column('BID', width=10, anchor=CENTER)
    detail_tree.column('Title', width=20, anchor=CENTER)
    detail_tree.column('Author', width=10, anchor=CENTER)
    detail_tree.column('Publication', width=20, anchor=CENTER)
    detail_tree.column('Status', width=10, anchor=CENTER)
    detail_tree.column('P-Location', width=10, anchor=CENTER)
    detail_tree.column('Issued Date', width=10, anchor=CENTER)
    detail_tree.column('Issued To', width=10, anchor=CENTER)

    # Styling Treeview
    style = ttk.Style()
    style.configure("Treeview",
                    background='#d3d3d3',
                    foreground="black",
                    rowheight=30,
                    font=('Arial', 9))

    style.map("Treeview",
              background=[('selected', 'green'), ('active', '#D3D3D3')])

    # Fetching data from database
    count = 0
    try:

        if query != "":
            cur.execute(query)
            con.commit()

        # Adding Data to the Treeview Table
        for data in loopThrough:
            data = list(data)
            # print(data)

            # Checking if the column is None then change the value to -
            for i in range(len(data)):
                if data[i] == None:
                    data[i] = '-'

            # Inserting in the Treeview
            detail_tree.insert(parent='', index=END, iid=count, text="",
                    values=(
                        data[0],
                        data[1].capitalize(),
                        data[2].capitalize(),
                        data[3].capitalize(),
                        data[4].capitalize(),
                        data[5],
                        data[6],
                        data[7].capitalize()
                    )
            )
            count += 1

        detail_tree.place(relx=marginX, rely=marginY, relwidth=width, relheight=height)
    except:
        messagebox.showinfo("Failed to fetch files from database")

# To Verify Position
def positionVerification(div, position):
    # Checking that Position of the Bok Should inclue -, _, and Digits
    if not any(re.findall(r'-|_|/|\d', position, re.IGNORECASE)) or not re.sub(
            '[^\d.,]', '', position):
        div.destroy()
        messagebox.showerror(
            "Failed",
            "Location Field should include '-' or '_' and Numbers (0-9)")
        return


# Function to put the Buttons on the window
def putButtons(window, set, X_Axis, Y_Axis, sign, width, height, bd=0, direction=VERTICAL):

    for _img, fun in set.items():

        btn = Button(
            window,
            text="",
            image=_img,
            border=bd,
            # font=('Gill Sans MT', 12),
            cursor='hand2',
            anchor=CENTER,
            command=fun)
        btn.place(relx=X_Axis, rely=Y_Axis, relwidth=width, relheight=height)

        if direction == VERTICAL:
            if sign == "+":
                Y_Axis += 0.1

            elif sign == "-":
                Y_Axis -= 0.1

        elif direction == HORIZONTAL:
            if sign == "+":
                X_Axis += 0.1
            elif sign == "-":
                X_Axis -= 0.1


# Checking BookID is correct or not Implemented in DeleteBook, IssuedBook, Return Book
def bookIdChecker(bid):
    checklist = []

    c = f"SELECT book_id FROM {bookTable};"
    cur.execute(c)
    con.commit()

    for i in cur:
        checklist.append(i)

    t = (bid, )

    if t not in checklist:
        messagebox.showinfo('Failed', "You've Entered the Wrong Book ID.")
        return 1
from tkinter import *
import pymysql
from os import getenv
from dotenv import load_dotenv
import tkinter.ttk as TTK
from datetime import datetime
from .issueBook import issueBook
import modules.func as Function

load_dotenv()

# Connecting to DB
con = pymysql.connect(host=getenv('HOST'), user=getenv('USER'), password=getenv('DB_PASS'), database=getenv('DB_NAME'))
cur = con.cursor()

# Book Table
bookTable = getenv('BOOK_TABLE')

# Search Result List
result = []

# Verify that search Field is empty or not
def verify(self):
    try:
        if searchField.get() == "":
            searchButton.config(state=DISABLED)
        else:
            searchButton.config(state=NORMAL)
    except:
        print("Something Went wrong. Refresh Window.")

# Search Query Execution and Returning the Result
def executingQuery(query):
    cur.execute(query)
    con.commit()

    for row in cur:
        result.append(row)

    print(result)
    return result


# Search Via BOOK ID
def searchByBookID():
    bid = searchField.get()
    query1 = f"SELECT * FROM {bookTable} WHERE book_id = '{bid}' ORDER BY status;"
    return executingQuery(query1)

# Search Via Author
def searchByAuthor():
    author = searchField.get()
    query1 = f"SELECT * FROM {bookTable} WHERE author LIKE '%{author.lower()}%' ORDER BY status;"
    return executingQuery(query1)

# Search Via Title
def searchByTitle():
    title = searchField.get()
    query1 = f"SELECT * FROM {bookTable} WHERE title LIKE '%{title.lower()}%' ORDER BY status;"
    return executingQuery(query1)

# Get the Key from teh Value
def GetKey(val):
    for key, value in radioButton.items():
        if val == value:
            return key

# Issue Button click on the Result Page
def issueFromSearch():
    app.destroy()
    issueBook()


# Result Page when the Search Button is Clicked
def OnClick():

    # Process Start Time
    start_time = datetime.now()

    global selectedOption, resultedList, result_tree, tree_scroll, app

    selectedOption = var.get()

    # Checking which option is selected
    if selectedOption == "1":
        resultedList = searchByBookID()
    if selectedOption == "2":
        resultedList = searchByAuthor()
    if selectedOption == "3":
        resultedList =  searchByTitle()

    print(resultedList)

    # Initializing the Result Window
    app = Toplevel()
    app.title("Results")
    app.geometry("1000x400")
    app.iconbitmap('img/resultIcon.ico')

    # Calculating the total time taken by the Search
    duration = str(datetime.now() - start_time)
    print('Duration: {}'.format(datetime.now() - start_time))

    # Display the Result Bar
    resultText = f"{len(resultedList)} results found in {duration[5:10]} of {GetKey(selectedOption)} - {searchField.get()}"
    resultLabel = Label(app, text=resultText, font = ('Gill Sans MT', 13))
    resultLabel.grid(row=0, column=0, pady=10, ipadx=10)

    # Creating Tree View and Looping through the Result
    Function.createTable(dir=app, height=0.6, width=0.98, marginX=0.01, marginY=0.15, loopThrough=resultedList)

    # Clear the Resulted List
    result.clear()

    # Issue Button
    issueBtn = Button(app,
                     text="Issue",
                     bg='white',
                     fg='black',
                     bd=0.5,
                     command=issueFromSearch)
    issueBtn.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.1)

    # Quit Button
    quitBtn = Button(app,
                     text="Quit",
                     bg='white',
                     fg='black',
                     bd=0.5,
                     command=app.destroy)
    quitBtn.place(relx=0.6, rely=0.8,relwidth=0.2, relheight=0.1)
    root.destroy()
    app.resizable(0,0)
    app.mainloop()


def Search():
    global var, label, radioButton, searchField, searchButton, root

    # Initializing the Search Window
    root = Toplevel()
    root.title("Search")
    root.iconbitmap('img/searchIcon.ico')
    root.geometry("250x250")

    # Choose Lable
    chooseLabel = TTK.Label(root, text="Search by -")
    chooseLabel.grid(row=0, column=0, columnspan=2, padx=20, pady=10, ipadx=30)

    # Radio Buttons
    var = StringVar(root, "1")

    # Radio Button Set
    radioButton = {
        "Book ID" : "1",
        "Author" : "2",
        "Title": "3"
    }

    col = 0

    # Puttin the Radio Button on the Window
    for (text, value) in radioButton.items():

        Rbutton = TTK.Radiobutton(root, text = text, variable = var, value = value)
        Rbutton.grid(row=1, column=col, columnspan=2, padx=20,ipadx=30)
        col += 1

    # Search Field
    searchField  = TTK.Entry(root)
    searchField.place(relx=0.04, rely=0.3, relwidth=0.9, relheight=0.1)

    # Search Button
    searchButton = Button(root, text='Search', bd=0.5, cursor='hand2',state=DISABLED,font=('Gill Sans MT', 14), command=OnClick)
    searchButton.place(relx=0.3, rely=0.45, relheight=0.15, relwidth=0.4)


    # Running SendEmail on Enter
    root.bind('<Return>', OnClick)
    root.bind_all("<KeyPress>", verify)

    root.resizable(0,0)
    root.mainloop()

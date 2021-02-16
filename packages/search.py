from tkinter import *
import sqlite3
from os import getenv
from dotenv import *
import tkinter.ttk as TTK
from datetime import datetime
import modules.func as Function
from PIL import *
from tkinter import messagebox


# importing every file
from .addBook import addBook
from .deletebook import delete
from .viewsBook import View
from .issueBook import issueBook
from .returnBook import returnBook
from .shelvesUpdation import UpdateShelves
from .feedback import feedBack

env = find_dotenv('env/.env')
load_dotenv(env)

# Connecting to DB
con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()

# Book Table
bookTable = getenv('BOOK_TABLE')
studentsTable = getenv('STUDENT_TABLE')

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
    try:
        cur.execute(query)
        con.commit()

        for row in cur:
            result.append(row)

        return result

    except:
        print("Something went Wrong")
        root.destroy()
        messagebox.showerror("Failed", "Something went wrong try again.")
        return


# Search Via BOOK ID
def searchByBookID():
    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id  WHERE book_id = '{inputField}' ORDER BY status;"
    return executingQuery(query1)

# Search Via Author
def searchByAuthor():
    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id WHERE author LIKE '%{inputField.lower()}%' ORDER BY status;"
    return executingQuery(query1)

# Search Via Title
def searchByTitle():
    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id WHERE title LIKE '%{inputField.lower()}%' ORDER BY status;"
    return executingQuery(query1)


# Search By Position
def searchByPosition():
    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id WHERE phyLocation LIKE '%{inputField.lower()}%' ORDER BY status;"
    return executingQuery(query1)

# Search By Date
def searchByDate():

    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id WHERE issued_date LIKE '%{inputField.lower()}%' ORDER BY status;"
    return executingQuery(query1)

# Search By Student Name
def searchByStudent():

    query1 = f"SELECT *, {studentsTable}.student_name as name FROM {bookTable} LEFT JOIN students ON {bookTable}.issued_to = {studentsTable}.student_id WHERE issued_to = {inputField} ORDER BY status;"
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
def OnClick(e=None):

    # Process Start Time
    start_time = datetime.now()

    global selectedOption, resultedList, result_tree, tree_scroll, app, inputField

    selectedOption = var.get()

    inputField = searchField.get()


    # Checking which option is selected
    if selectedOption == "1":
        resultedList = searchByBookID()
    if selectedOption == "2":
        resultedList = searchByAuthor()
    if selectedOption == "3":
        resultedList =  searchByTitle()
    if selectedOption == "4":
        resultedList =  searchByPosition()
    if selectedOption == "5":
        resultedList = searchByDate()
    if selectedOption == "6":
        try:
            inputField =  int(inputField)
        except:
            messagebox.showerror("Error", "StudentID must be Integer")
            return
        resultedList = searchByStudent()

    # print(resultedList)

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

    img1 = PhotoImage(file='img/buttons/searchButtons/add.png')
    img2 = PhotoImage(file='img/buttons/searchButtons/del.png')
    img3 = PhotoImage(file='img/buttons/searchButtons/info.png')
    img4 = PhotoImage(file='img/buttons/searchButtons/issue.png')
    img5 = PhotoImage(file='img/buttons/searchButtons/return.png')
    img6 = PhotoImage(file="img/buttons/f-icon.png")
    img7 = PhotoImage(file="img/buttons/updateBtn.png")
    img8 = PhotoImage(file='img/buttons/searchButtons/quit.png')


    buttonsOnSearch = {

        img1 : addBook,
        img2 : delete,
        img3 : View,
        img4 : issueBook,
        img5 : returnBook,
        img6 : feedBack,
        img7 : UpdateShelves,
        img8 : app.destroy

    }

    # from modules.func
    Function.putButtons(app, buttonsOnSearch, 0.145, 0.8, "+", 0.08, 0.15, direction=HORIZONTAL)

    root.destroy()
    app.resizable(0,0)
    app.mainloop()


def Search():
    global var, label, radioButton, searchField, searchButton, root

    # Initializing the Search Window
    root = Toplevel()
    root.title("Search")
    root.iconbitmap('img/searchIcon.ico')
    root.geometry("650x250")

    # Choose Lable
    chooseLabel = TTK.Label(root, text="Search by -", font=('Gill Sans MT', 12))
    chooseLabel.grid(row=0, column=0, columnspan=1, padx=20, pady=10)

    # Radio Buttons
    var = StringVar(root, "1")

    # Radio Button Set
    radioButton = {
        "Book ID" : "1",
        "Author" : "2",
        "Title": "3",
        "Position" : "4",
        "Date" : "5",
        "Student ID" : "6"
    }

    col = 0

    # Puttin the Radio Button on the Window
    for (text, value) in radioButton.items():

        Rbutton = TTK.Radiobutton(root, text = text, variable = var, value = value)
        Rbutton.grid(row=1, column=col, columnspan=1, padx=20)
        col += 1

    # Search Field
    searchField  = TTK.Entry(root)
    searchField.place(relx=0.04, rely=0.35, relwidth=0.9, relheight=0.1)

    # Search Button
    searchButton = Button(root, text='Search', bd=0.5, cursor='hand2',state=DISABLED,font=('Gill Sans MT', 14), command=OnClick)
    searchButton.place(relx=0.3, rely=0.5, relheight=0.15, relwidth=0.4)


    # Running SendEmail on Enter
    root.bind('<Return>', OnClick)
    root.bind_all("<KeyPress>", verify)

    root.resizable(0,0)
    root.mainloop()

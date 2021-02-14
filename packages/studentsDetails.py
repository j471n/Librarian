from calendar import month
from os.path import relpath
from tkinter import *
import sqlite3
from dotenv import *
from os import getenv
import tkinter.ttk as TTK
import modules.func as Function
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename

env = find_dotenv('env/.env')
load_dotenv(env)
# Connecting to DB

con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()  #cur -> cursor

studentsTable = getenv('STUDENT_TABLE')
bookTable = getenv('BOOK_TABLE')
posTable = getenv('POSITION_TABLE')


def OpenFile():
    global path
    path = askopenfilename(filetypes=[("JPEG Files",
                                       '*.jpg'), ("PNG Files", '*.png')])
    print(path)


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def addStudentSubmit():
    nameValue = studentNameEntry.get()
    dobValue = studentDobEntry.get_date()
    addressValue = studentAddressEntry.get()
    courseValue = studentCourseEntry.get()
    branchValue = studentBranchEntry.get()
    contactValue = studentContactEntry.get()
    gradYearValue = studentGraduationYearEntry.get()

    print("socond path", path)
    profileImage = convertToBinaryData(path)

    print(nameValue, dobValue, addressValue, courseValue, branchValue,
          contactValue, gradYearValue)

    insertQuery = f"INSERT INTO {studentsTable} (student_name, dob, course, branch, address, contact, img, g_year) VALUES (?,?,?,?,?,?,?,?);"
    values = (nameValue, dobValue, courseValue, branchValue, addressValue,
              contactValue, profileImage, gradYearValue)

    con.execute(insertQuery, values)
    con.commit()
    print("Inserted Successfully.")


# To Adding Student in the Database
def addStudent():
    # root.destroy()

    global addAPP, studentAddressEntry, studentDobEntry, studentNameEntry, studentContactEntry, studentBranchEntry, studentCourseEntry, studentGraduationYearEntry, entry

    addAPP = Toplevel()
    addAPP.title("Add Student")
    addAPP.minsize(width=400, height=400)
    addAPP.geometry("600x500")
    addAPP.iconbitmap('img/logo.ico')
    addAPP.config(bg='white')

    # A container
    headingFrame1 = Frame(addAPP, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Add Student",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # StudentName Label and Entry
    studentNameLabel = Label(addAPP,
                             text="Name : ",
                             bg='white',
                             fg='black',
                             font=('Gill Sans MT', 12))
    studentNameLabel.place(relx=0.15, rely=0.25)
    studentNameEntry = TTK.Entry(addAPP)
    studentNameEntry.place(relx=0.4, rely=0.26, relwidth=0.45)

    # Student DOB

    studentDobLabel = Label(addAPP,
                            text="Date of Birth : ",
                            bg='white',
                            fg='black',
                            font=('Gill Sans MT', 12))
    studentDobLabel.place(relx=0.15, rely=0.305)

    studentDobEntry = DateEntry(addAPP,
                                width=12,
                                background='red',
                                foreground='white',
                                borderwidth=2)
    studentDobEntry.place(relx=0.4, rely=0.32)

    # Student Coruse

    studentCourseLabel = Label(addAPP,
                               text="Course : ",
                               bg='white',
                               fg='black',
                               font=('Gill Sans MT', 12))
    studentCourseLabel.place(relx=0.15, rely=0.365)
    studentCourseEntry = TTK.Entry(addAPP)
    studentCourseEntry.place(relx=0.4, rely=0.38, relwidth=0.45)

    # Student Branch

    studentBranchLabel = Label(addAPP,
                               text="Branch : ",
                               bg='white',
                               fg='black',
                               font=('Gill Sans MT', 12))
    studentBranchLabel.place(relx=0.15, rely=0.425)
    studentBranchEntry = TTK.Entry(addAPP)
    studentBranchEntry.place(relx=0.4, rely=0.44, relwidth=0.45)

    # Student Address

    studentAddressLabel = Label(addAPP,
                                text="Address : ",
                                bg='white',
                                fg='black',
                                font=('Gill Sans MT', 12))
    studentAddressLabel.place(relx=0.15, rely=0.49)
    studentAddressEntry = TTK.Entry(addAPP)
    studentAddressEntry.place(relx=0.4, rely=0.5, relwidth=0.45)

    # Student Contact

    studentContactLabel = Label(addAPP,
                                text="Contact : ",
                                bg='white',
                                fg='black',
                                font=('Gill Sans MT', 12))
    studentContactLabel.place(relx=0.15, rely=0.545)
    studentContactEntry = TTK.Entry(addAPP)
    studentContactEntry.place(relx=0.4, rely=0.56, relwidth=0.45)
    # Student Graduation Year

    studentGraduationYearLabel = Label(addAPP,
                                       text="Graduation : ",
                                       bg='white',
                                       fg='black',
                                       font=('Gill Sans MT', 12))
    studentGraduationYearLabel.place(relx=0.15, rely=0.605)
    studentGraduationYearEntry = TTK.Entry(addAPP)
    studentGraduationYearEntry.place(relx=0.4, rely=0.62, relwidth=0.45)

    # Student Image

    studentImageLabel = Label(addAPP,
                              text="Image : ",
                              bg='white',
                              fg='black',
                              font=('Gill Sans MT', 12))
    studentImageLabel.place(relx=0.15, rely=0.67)

    StudentImageEntry = TTK.Button(addAPP,
                                   text='Choose',
                                   cursor='hand2',
                                   command=OpenFile)
    StudentImageEntry.place(relx=0.4, rely=0.68)

    # Button Images
    _img1 = PhotoImage(file="img/buttons/submit.png")
    _img2 = PhotoImage(file="img/buttons/cancel.png")

    # Submit Button
    SubmitBtn = Button(addAPP,
                       bg='white',
                       image=_img1,
                       bd=0,
                       cursor='hand2',
                       command=addStudentSubmit,
                       font=('Gill Sans MT', 12))
    SubmitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.1)

    # Cancel Button
    cancelBtn = Button(addAPP,
                       bg='white',
                       image=_img2,
                       command=addAPP.destroy,
                       bd=0,
                       cursor='hand2',
                       font=('Gill Sans MT', 12))
    cancelBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.1)

    addAPP.mainloop()


# addStudent()
# return


def delStudent():
    pass


def updateData():
    pass


def viewData():
    pass


def SearchData():
    pass


def studentPortalWindow():

    global root

    root = Toplevel()
    root.title("Student Portal")
    root.geometry("600x350")
    root.iconbitmap('img/studentportal.ico')
    customColor = '#5dffb8'
    root.config(bg=customColor)

    # Heading Frame for Heading
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.2)
    headingLabel = Label(headingFrame1,
                         text="Student Portal",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 28))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    addimg = PhotoImage(file='img/buttons/studentsButtons/addbtn.png')
    delimg = PhotoImage(file='img/buttons/studentsButtons/delbtn.png')
    udtimg = PhotoImage(file='img/buttons/studentsButtons/udtbtn.png')
    viewimg = PhotoImage(file='img/buttons/studentsButtons/viewbtn.png')
    exitimg = PhotoImage(file='img/buttons/studentsButtons/exitbtn.png')

    leftbuttons = {
        addimg: addStudent,
        udtimg: updateData,
    }

    rightbuttons = {
        delimg: delStudent,
        viewimg: viewData,
    }

    bottomButtons = {exitimg: root.destroy}

    # from modules.func
    Function.putButtons(root,
                        leftbuttons,
                        -0.05,
                        0.35,
                        "+",
                        0.45,
                        0.17,
                        bgcolor=customColor,
                        bd=0,
                        direction=VERTICAL)
    Function.putButtons(root,
                        rightbuttons,
                        0.6,
                        0.35,
                        "+",
                        0.45,
                        0.17,
                        bgcolor=customColor,
                        bd=0,
                        direction=VERTICAL)
    Function.putButtons(root,
                        bottomButtons,
                        0.37,
                        0.75,
                        "+",
                        0.26,
                        0.17,
                        bgcolor=customColor,
                        bd=0,
                        direction=VERTICAL)
    root.resizable(0, 0)

    root.mainloop()


# studentPortalWindow()
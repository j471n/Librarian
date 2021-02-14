from tkinter import *
import sqlite3
from dotenv import *
from os import getenv, pardir
import tkinter.ttk as TTK
import modules.func as Function
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

env = find_dotenv('env/.env')
load_dotenv(env)
# Connecting to DB

con = sqlite3.connect(getenv('DATABASE'))
cur = con.cursor()  #cur -> cursor

studentsTable = getenv('STUDENT_TABLE')
bookTable = getenv('BOOK_TABLE')
posTable = getenv('POSITION_TABLE')


def OpenFile():
    global path, RemoveButton
    path = askopenfilename(filetypes=[("JPEG Files", '*.jpg'), ("PNG Files", '*.png')])
    StudentImageEntry.config(text="Choosed")
    RemoveButton = TTK.Button(addAPP,text='x', cursor='hand2', command=RemoveFile)
    RemoveButton.place(relx=0.53, rely=0.68, relwidth=0.05)

# To remove the File
def RemoveFile():
    path = ""
    RemoveButton.destroy()
    StudentImageEntry.config(text="Choose")


def addStudentSubmit():
    global profileImage

    nameValue = studentNameEntry.get()
    dobValue = studentDobEntry.get_date()
    addressValue = studentAddressEntry.get()
    courseValue = studentCourseEntry.get()
    branchValue = studentBranchEntry.get()
    contactValue = studentContactEntry.get()
    gradYearValue = studentGraduationYearEntry.get()
    genderValue = var.get()

    answer = messagebox.askyesno("Confirm", f"Do you want to add \"{nameValue.capitalize()}\" as Student?")
    if answer == False:
        addAPP.destroy()
        return

    try:
        int(contactValue)
    except:
        messagebox.showwarning("Warning", "Contact No. Must be correct.\nDon't put space and '-' between numbers")
        studentContactEntry.delete(0, END)
        print('Not correct')
        return

    # return
    if len(gradYearValue) == 4:
        try:
            gradYearValue = int(gradYearValue)
        except:
            print("Not Interger")
            messagebox.showwarning("Warning", "Year must be Integer")
            studentGraduationYearEntry.delete(0, END)

    else:
        messagebox.showerror("Failed", "Enter the Correct Year")
        studentGraduationYearEntry.delete(0, END)
        return

    try:
        profileImage = Function.reduceImage(path)
    except(NameError):
        if genderValue == 'M':
            print("Using Male Unknown Image")
            path = "img/profile/male.jpg"
        elif genderValue == 'F':
            print("Using FeMale Unknown Image")
            path = "img/profile/female.jpg"

        profileImage = Function.reduceImage(path)


    insertQuery = f"INSERT INTO {studentsTable} (student_name, dob, course, branch, address, contact, img, g_year, gender) VALUES (?,?,?,?,?,?,?,?,?);"
    values = (nameValue, dobValue, courseValue, branchValue, addressValue,
              contactValue, profileImage, gradYearValue, genderValue)

    try:
        con.execute(insertQuery, values)
        con.commit()
        print("Inserted Successfully.")
        messagebox.showinfo("Success", f"Student \"{nameValue.capitalize()}\ added successfully")
    except:
        messagebox.showerror("Failed", 'Something Went Wrong')
    addAPP.destroy()


# To Adding Student in the Database
def addStudent():
    root.destroy()

    global addAPP, studentAddressEntry, studentDobEntry, studentNameEntry, studentContactEntry, studentBranchEntry, studentCourseEntry, studentGraduationYearEntry, entry, var, StudentImageEntry

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

    # Gender Lable
    genderLabel = Label(addAPP,
                            text="Gender : ",
                            bg='white',
                            fg='black',
                            font=('Gill Sans MT', 12))
    genderLabel.place(relx=0.6, rely=0.305)

    var = StringVar()
    monthchoosen = TTK.Combobox(addAPP, width = 27, textvariable = var, state="readonly")
    monthchoosen.place(relx=0.75, rely=0.32, relwidth=0.1)
    # Adding combobox drop down list
    monthchoosen['values'] = ('M', 'F')
    monthchoosen.current(0)
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

def delSubmitButton():

    studentID = toDeleteIDEntry.get()

    try:
        studentID = int(studentID)
        print("correctID")
    except:
        print("Incorrect ID")
        toDeleteIDEntry.delete(0, END)
        return

    cur.execute(f"SELECT student_name FROM {studentsTable} WHERE student_id = {studentID};")
    con.commit()
    studentName = ""

    for i in cur:
        studentName = i[0]
        print(studentName)

    if len(studentName) == 0:
        messagebox.showerror("Failed", "Student Does not Exist")
        toDeleteIDEntry.delete(0, END)
        return

    answer = messagebox.askyesno("Confirm", f"Do you want to delete the records of \"{studentName.capitalize()}\"?")
    if answer == False:
        delAPP.destroy()
        return


    deleteStudentQuery = f"DELETE FROM {studentsTable} WHERE student_id = {studentID};"

    try:
        cur.execute(deleteStudentQuery)
        con.commit()
        messagebox.showinfo("Success", f"{studentName.capitalize()} records deleted Successfully")
    except:
        messagebox.showerror("Failed", "Something went wrong")
        return

    delAPP.destroy()


def delStudent():
    root.destroy()

    global delAPP, toDeleteIDEntry

    delAPP = Toplevel()
    delAPP.title("Add Student")
    delAPP.geometry("300x250")
    delAPP.iconbitmap('img/logo.ico')
    delAPP.config(bg='white')

    # A container
    headingFrame1 = Frame(delAPP, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.23)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Delete Student",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 22))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # StudentName Label and Entry
    toDeleteIDLabel = Label(delAPP,
                             text="Student ID : ",
                             bg='white',
                             fg='black',
                             font=('Gill Sans MT', 12))
    toDeleteIDLabel.place(relx=0.13, rely=0.45)
    toDeleteIDEntry = TTK.Entry(delAPP)
    toDeleteIDEntry.place(relx=0.42, rely=0.475, relwidth=0.45)

    _img1 = PhotoImage(file="img/buttons/submit.png")

    delSubmitBtn = Button(delAPP,
                       bg='white',
                       image=_img1,
                       bd=0,
                       cursor='hand2',
                       command=delSubmitButton,
                       font=('Gill Sans MT', 12))
    delSubmitBtn.place(relx=0.325, rely=0.7, relwidth=0.35, relheight=0.15)


    delAPP.mainloop()
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
    Function.putButtons(root, leftbuttons, -0.05, 0.35, "+", 0.45,0.17,bgcolor=customColor, bd=0, direction=VERTICAL)
    Function.putButtons(root, rightbuttons, 0.6, 0.35, "+", 0.45, 0.17, bgcolor=customColor, bd=0, direction=VERTICAL)
    Function.putButtons(root, bottomButtons, 0.37, 0.75, "+", 0.26, 0.17, bgcolor=customColor, bd=0, direction=VERTICAL)
    root.resizable(0, 0)

    root.mainloop()


# studentPortalWindow()
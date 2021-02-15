from tkinter import *
import sqlite3
from dotenv import *
from os import getenv
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


# -----------------------------------------Add Student Section---------------------------------
def OpenFile():
    global path, RemoveButton
    path = askopenfilename(filetypes=[("JPEG Files", '*.jpg'), ("PNG Files", '*.png')])
    StudentImageEntry.config(text="Choosed")
    RemoveButton = TTK.Button(addAPP,text='x', cursor='hand2', command=RemoveFile)
    RemoveButton.place(relx=0.53, rely=0.68, relwidth=0.05)

# To remove the File
def RemoveFile():
    global path
    path = ""
    RemoveButton.destroy()
    StudentImageEntry.config(text="Choose")


def addStudentSubmit():

    global path, profileImage
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
        # global profileImage
        profileImage = Function.reduceImageByHeight(path)
    except(NameError):
        if StudentImageEntry['text'] == 'Choose':
            if genderValue == 'M':
                print("Using Male Unknown Image")
                path = "img/profile/male.jpg"
            elif genderValue == 'F':
                print("Using FeMale Unknown Image")
                path = "img/profile/female.jpg"

            profileImage = Function.reduceImageByHeight(path)


    insertQuery = f"INSERT INTO {studentsTable} (student_name, dob, course, branch, address, contact, img, g_year, gender) VALUES (?,?,?,?,?,?,?,?,?);"
    values = (nameValue, dobValue, courseValue, branchValue, addressValue,
              contactValue, profileImage, gradYearValue, genderValue)

    try:
        con.execute(insertQuery, values)
        con.commit()
        print("Inserted Successfully.")
        messagebox.showinfo("Success", f"Student \"{nameValue.capitalize()}\" added successfully")
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

    addAPP.resizable(0,0)
    addAPP.mainloop()

# ----------------------------- Delete Student Section-----------------------------------------

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

    delAPP.resizable(0,0)
    delAPP.mainloop()


def updateData():
    pass


def viewData():
    pass


# ------------------------------------------Search Student Section --------------------------------------------


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def resultPage(dict):

    searchAPP.destroy()

    global resultAPP

    resultAPP = Toplevel()
    resultAPP.title("Search Result")
    resultAPP.geometry("500x500")
    resultAPP.iconbitmap('img/logo.ico')
    resultAPP.config(bg='white')


    # A container
    headingFrame1 = Frame(resultAPP, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=0.125)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Search Result",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 22))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # StudentID Label

    try:
        idLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"ID\t-  {dict['id']}")
        idLabel.place(relx=0.1, rely=0.2)
    except:
        resultAPP.destroy()
        messagebox.showerror("Failed", f"You've entered the wrong StudentID")
        return
    # Student Name Label
    nameLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Name\t-  {dict['name']}")
    nameLabel.place(relx=0.1, rely=0.25)

    # studen DOB
    dobLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"DOB\t-  {dict['dob']}")
    dobLabel.place(relx=0.1, rely=0.3)

    # Student Gender

    if dict['gender'] == 'M':
        dict['gender'] = 'Male'
    else:
        dict['gender'] = 'Female'

    genLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Gender\t-  {dict['gender']}")
    genLabel.place(relx=0.1, rely=0.35)

    # Student Course

    cLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Course\t-  {dict['course']}")
    cLabel.place(relx=0.1, rely=0.4)

    # Student Branch

    bLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Branch\t-  {dict['branch']}")
    bLabel.place(relx=0.1, rely=0.45)


    # Student Contact

    conLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Contact\t-  {dict['contact']}")
    conLabel.place(relx=0.1, rely=0.5)

    # Student Graduation Year

    yearLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"G. Year\t-  {dict['g_year']}")
    yearLabel.place(relx=0.1, rely=0.55)

    # Student Fine


    finLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Fine\t-  {dict['fine']} Rs.")
    finLabel.place(relx=0.1, rely=0.6)

    # Student Address

    genLabel = Label(resultAPP, bg='white',font=('Gill Sans MT', 12), text=f"Address\t-  {dict['add']}", wraplength=475)
    genLabel.place(relx=0.1, rely=0.65)

    # Student Image
    global resultProfileImg

    try:
        resultProfileImg = ImageTk.PhotoImage(Image.open(f"img/studentsDB/{dict['id']}.png"))
        print('old')
    except:
        print('new')
        filepath = "img/studentsDB/" + str(dict['id']) + ".png"
        writeTofile(dict['img'], filepath)
        resultProfileImg = ImageTk.PhotoImage(Image.open(f"img/studentsDB/{dict['id']}.png"))

    studentImg = Label(resultAPP, image=resultProfileImg, bg='black')
    studentImg.place(relx=0.55, rely=0.2)


    # QUIT BUTTON
    quitImg = PhotoImage(file='img/buttons/studentsButtons/quit.png')
    quitBtn = Button(resultAPP,cursor='hand2', image=quitImg, bd=0, bg='white', command=resultAPP.destroy)
    quitBtn.place(relx=0.39, rely=0.8, relheight=0.1, relwidth=0.22)

    resultAPP.resizable(0,0)
    resultAPP.mainloop()




def Searching():
    studentID = toDeleteIDEntry.get()

    try:
        studentID = int(studentID)
        print("correctID")
    except:
        print("Incorrect ID")
        searchAPP.destroy()
        messagebox.showerror("Failed", "StudentID should be Integer")
        return

    global studentdat
    studentData = {}
    cur.execute(f"SELECT * FROM {studentsTable} WHERE student_id = {studentID};")
    con.commit()

    for data in cur:

        try:
            studentData.update({'id' : data[0]})
            studentData.update({'name': data[1].title()})
            studentData.update({'dob' : data[2]})
            studentData.update({'course' : data[3].upper()})
            studentData.update({'branch' : data[4].upper()})
            studentData.update({'add': data[5].title()})
            studentData.update({'contact' : data[6]})
            studentData.update({'img' : data[7]})
            studentData.update({'g_year' : data[8]})
            studentData.update({'gender' : data[9]})
            studentData.update({'fine' : data[10]})

        except:
            searchAPP.destroy()
            messagebox.showerror("Failed", f"You've entered the wrong StudentID")
            return

    resultPage(studentData)




def SearchData():
    root.destroy()

    global searchAPP, toDeleteIDEntry

    searchAPP = Toplevel()
    searchAPP.title("Search Student")
    searchAPP.geometry("300x250")
    searchAPP.iconbitmap('img/logo.ico')
    searchAPP.config(bg='white')

    # A container
    headingFrame1 = Frame(searchAPP, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.23)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Search Student",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 22))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # StudentName Label and Entry
    toDeleteIDLabel = Label(searchAPP,
                            text="Student ID : ",
                            bg='white',
                            fg='black',
                            font=('Gill Sans MT', 12))
    toDeleteIDLabel.place(relx=0.13, rely=0.45)
    toDeleteIDEntry = TTK.Entry(searchAPP)
    toDeleteIDEntry.place(relx=0.42, rely=0.475, relwidth=0.45)

    _img1 = PhotoImage(file="img/buttons/submit.png")

    searchSubmitBtn = Button(searchAPP,
                             bg='white',
                             image=_img1,
                             bd=0,
                             cursor='hand2',
                             command=Searching,
                             font=('Gill Sans MT', 12))
    searchSubmitBtn.place(relx=0.325, rely=0.7, relwidth=0.35, relheight=0.15)

    searchAPP.resizable(0,0)
    searchAPP.mainloop()

#----------------------------------View Student List -------------------------------



def viewData():
    root.destroy()

    viewAPP = Toplevel()
    viewAPP.title('View Student Database')
    viewAPP.geometry("800x400")
    viewAPP.iconbitmap('img/logo.ico')
    viewAPP.config(bg='white')

    # A container
    headingFrame1 = Frame(viewAPP, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.03, relwidth=0.5, relheight=0.125)

    # Container Label
    headingLabel = Label(headingFrame1,
                         text="Student Database",
                         bg='black',
                         fg='white',
                         font=('Great Vibes', 22))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    # Table
    studentTree = TTK.Treeview(viewAPP)

    # ScrollBar Adding to Treeview
    tree_scroll = Scrollbar(viewAPP, orient="vertical", command=studentTree.yview)
    tree_scroll.place(relx=0.98, rely=0.2, relheight=0.6, relwidth=0.02)
    studentTree.configure(yscrollcommand=tree_scroll.set)

    studentTree['columns'] = ("SID", "Name", "DOB", "Gender", "Course", "Branch", "Contact", "Fine")

    #Heading List
    studentTree.heading("#0", text="")
    studentTree.heading("SID", text="SID", anchor=CENTER)
    studentTree.heading("Name", text="Name", anchor=CENTER)
    studentTree.heading("DOB", text="DOB", anchor=CENTER)
    studentTree.heading("Gender", text="Gender", anchor=CENTER)
    studentTree.heading("Course", text="Course", anchor=CENTER)
    studentTree.heading("Branch", text="Branch", anchor=CENTER)
    studentTree.heading("Contact", text="Contact", anchor=CENTER)
    studentTree.heading("Fine", text="Fine", anchor=CENTER)
    # Colums List
    studentTree.column('#0', width=0, stretch=NO)
    studentTree.column('SID', width=10, anchor=CENTER)
    studentTree.column('Name', width=20, anchor=CENTER)
    studentTree.column('DOB', width=10, anchor=CENTER)
    studentTree.column('Gender', width=20, anchor=CENTER)
    studentTree.column('Course', width=10, anchor=CENTER)
    studentTree.column('Branch', width=10, anchor=CENTER)
    studentTree.column('Contact', width=10, anchor=CENTER)
    studentTree.column('Fine', width=10, anchor=CENTER)

    # Styling Treeview
    style = TTK.Style()
    style.configure("Treeview", background='#d3d3d3', foreground="black", rowheight=30, font=('Arial', 9))

    style.map("Treeview",
              background=[('selected', 'green'), ('active', '#D3D3D3')])

    # Fetching data from database
    count = 0
    try:

        query = "SELECT * FROM students;"
        cur.execute(query)
        con.commit()

        # Adding Data to the Treeview Table
        for data in cur:
            data = list(data)

            # Checking if the column is None then change the value to -
            for i in range(len(data)):
                if data[i] == None:
                    data[i] = '-'

            # Inserting in the Treeview
            studentTree.insert( parent='', index=END, iid=count, text="",
                values=(data[0],
                        data[1].title(),
                        data[2],
                        data[9],
                        data[3].upper(),
                        data[4].upper(),
                        data[6],
                        data[10]
                )
            )
            count += 1

        studentTree.place(relx=0.025, rely=0.2, relwidth=0.95, relheight=0.6)
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # QUI Button
    quitImg = PhotoImage(file='img/buttons/studentsButtons/quit.png')
    quitBtn = Button(viewAPP,cursor='hand2', image=quitImg, bd=0, bg='white', command=viewAPP.destroy)
    quitBtn.place(relx=0.39, rely=0.85, relheight=0.1, relwidth=0.22)

    viewAPP.resizable(0,0)
    viewAPP.mainloop()


# ---------------------------------------Student Main Portal Section---------------------------------------------

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
    searchimg = PhotoImage(file='img/buttons/studentsButtons/search.png')

    leftbuttons = {
        addimg: addStudent,
        udtimg: updateData,
        searchimg : SearchData
    }

    rightbuttons = {
        delimg: delStudent,
        viewimg: viewData,
        exitimg : root.destroy
    }

    # bottomButtons = {exitimg: root.destroy}

    # from modules.func
    Function.putButtons(root, leftbuttons, -0.05, 0.35, "+", 0.45,0.17,bgcolor=customColor, bd=0, direction=VERTICAL)
    Function.putButtons(root, rightbuttons, 0.6, 0.35, "+", 0.45, 0.17, bgcolor=customColor, bd=0, direction=VERTICAL)
    # Function.putButtons(root, bottomButtons, 0.37, 0.75, "+", 0.26, 0.17, bgcolor=customColor, bd=0, viewAPPection=VERTICAL)
    root.resizable(0, 0)
    root.mainloop()

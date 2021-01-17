from tkinter import *
from os import  getenv, stat
from mailer import Mailer
from email.message import EmailMessage
from tkinter import messagebox
import re
from dotenv import load_dotenv

load_dotenv()

def sendEmail(event=None):
    global email, password, msg
    senderEmail = email.get()
    senderPassword = password.get()
    feedback = msg.get('1.0', END)

    # Taking String from ENV File
    regx = getenv('VALID_EMAIL')
    receiverEmail = getenv('R_EMAIL')
    
    # Checking email is valid or not
    if re.search(regx, senderEmail):
        print("Valid Email")
    else:
        messagebox.showerror("Failed", "Invalid Email Address")
        # root.destroy()
        email.delete(0, END)
        password.delete(0, END)
        msg.delete(1.0, END)
        return

    mail = Mailer(email= senderEmail, password=senderPassword)
    mail.send(receiver = receiverEmail,
                subject = "FeedBack About LIBRARIAN",
                message = feedback)

    print(mail.status)

    if mail.status:
        messagebox.showinfo("Success", "Email Send Successfully")
        root.destroy()
        return
    else:
        messagebox.showerror("Failed", "Something Went Wrong")
        email.delete(0, END)
        password.delete(0, END)
        msg.delete(1.0, END)


# Changing the Button state on the basis of fields
def verify(self):
    try:
        if email.get() == "" or password.get() == "":
            b.config(state=DISABLED )
        else:
            b.config(state=NORMAL)
    except:
        print("Something Went wrong. Refresh Window.")

def feedBack():
    global root
    root = Tk()
    root.title("Feedback")
    root.iconbitmap('img/feedback-icon.ico')
    root.geometry("300x375")

    global email, password, msg
    l1 = Label(root,text= "Enter Email").grid(row=0, column=0, columnspan=4, pady=2)
    email = Entry(root)
    email.grid(row=1, column=0, columnspan=4, padx=7, pady=5, ipadx=50)

    l2 = Label(root,text= "Enter Password").grid(row=3, column=0, columnspan=4, pady=2)
    password = Entry(root, show="*")
    password.grid(row=4, column=0, columnspan=4, padx=7, pady=5, ipadx=50)

    l3 = Label(root,text= "Enter Feedback").grid(row=5, column=0, columnspan=4, pady=2)
    msg = Text(root, width=33, borderwidth=1, height=10, padx=9, pady=10)
    msg.grid(row=6, column=0, columnspan=4, padx=7, pady=5)

    global b
    b = Button(root, text='Submit', state=DISABLED, command=sendEmail)
    b.grid(row=7, column=1, columnspan=2, pady=10, ipadx=15, ipady=5)

    # Running Verify event on any key press
    root.bind_all("<KeyPress>", verify)
    # Running SendEmail on Enter
    root.bind('<Return>', sendEmail)
    root.resizable(0,0)
    root.mainloop()

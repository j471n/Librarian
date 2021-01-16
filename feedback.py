from tkinter import *
from os import  getenv
from mailer import Mailer
from email.message import EmailMessage
from tkinter import messagebox

from dotenv import load_dotenv

load_dotenv()


###  ankitsharma908437@gmail.com
###  ironman@tonystark

def sendEmail():
    global email, password, msg
    senderEmail = email.get()
    senderPassword = password.get()
    feedback = msg.get('1.0', END)

    receiverEmail = getenv('R_EMAIL')


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

    l2 = Label(root,text= "Enter Feedback").grid(row=5, column=0, columnspan=4, pady=2)
    msg = Text(root, width=35, borderwidth=1, height=10)
    msg.grid(row=6, column=0, columnspan=4, padx=7, pady=5)

    b = Button(root, text='Submit', command=sendEmail)
    b.grid(row=7, column=1, columnspan=2, pady=10, ipadx=15, ipady=5)


    root.resizable(0,0)
    root.mainloop()


from email.mime import text
from tkinter import *
from os import  getenv, stat
from mailer import Mailer
from email.message import EmailMessage
from tkinter import messagebox
import re
from dotenv import load_dotenv
import webbrowser
from PIL import ImageTk, Image  #PIL -> Pillow
from about import aboutUS

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
        root.destroy()
        messagebox.showerror("Failed", "Invalid Email Address")
        return

    mail = Mailer(email= senderEmail, password=senderPassword)
    mail.send(receiver = receiverEmail,
                subject = "FeedBack About LIBRARIAN",
                message = feedback)

    print(mail.status)

    if mail.status:
        messagebox.showinfo("Success", "Email Send Successfully")
        return
    else:
        messagebox.showerror("Failed", "Something Went Wrong")
        email.delete(0, END)
        password.delete(0, END)
        msg.delete(1.0, END)
    root.destroy()



# Changing the Button state on the basis of fields
def verify(self):
    try:
        if email.get() == "" or password.get() == "":
            b.config(state=DISABLED )
        else:
            b.config(state=NORMAL)
    except:
        print("Something Went wrong. Refresh Window.")



def callback(event):
    webbrowser.open(getenv('LESS_SECURE'))



def feedBack():
    global root
    root = Toplevel()
    root.title("Feedback")
    root.iconbitmap('img/feedback-icon.ico')
    root.geometry("600x415")

    global email, password, msg

    leftFrame = Frame(root, border=10)
    leftFrame.grid(row=0, column=0)

    l1 = Label(leftFrame,text= "Enter Email").grid(row=0, column=0, columnspan=4, pady=2)
    email = Entry(leftFrame)
    email.grid(row=1, column=0, columnspan=4, padx=7, pady=5, ipadx=50)

    l2 = Label(leftFrame,text= "Enter Password").grid(row=3, column=0, columnspan=4, pady=2)
    password = Entry(leftFrame, show="*")
    password.grid(row=4, column=0, columnspan=4, padx=7, pady=5, ipadx=50)

    l3 = Label(leftFrame,text= "Enter Feedback").grid(row=5, column=0, columnspan=4, pady=2)
    msg = Text(leftFrame, width=33, borderwidth=1, height=9, padx=9, pady=10, font=('Gill Sans MT', 10))
    msg.grid(row=6, column=0, columnspan=4, padx=7, pady=5)

    # Submit Button for Feedback Form
    global b
    img1= ImageTk.PhotoImage(Image.open("img/buttons/submit.png"))
    b = Button(leftFrame,image=img1, text='efddf', state=DISABLED, command=sendEmail, border=0, cursor='hand2')
    b.grid(row=7, column=1, columnspan=2, pady=10, ipady=2)


    # Labels for Right Frames

    rightLabel1 = Label(root,
                        text="!!! WARNING !!!",
                        foreground='red',
                        font=('Gill Sans MT', 18),
                        padx=10,
                        pady=10,
                        justify='center')
    rightLabel1.place(relx=0.59, rely=0)

    t1 = "We Don't Store Your Password anywhere. We take that and send it to the mail Server for Providing us Feedback. This Process is Totally Secure You Don't need to Worry"
    rightLabel2 = Label(root,
                        text=t1,
                        foreground='black',
                        background='#ffcc00',
                        padx=10,
                        pady=10,
                        anchor=W,
                        justify="left",
                        font=('Gill Sans MT', 13),
                        wraplength=275)
    rightLabel2.place(relx=0.52, rely=0.13)
    t2 = "!!! You need to make Sure that Less Secure Apps is Enable on Your Google Account. If not then - \n"
    rightLabel3 = Label(root,
                        text=t2,
                        foreground='white',
                        background='#339900',
                        padx=10,
                        pady=10,
                        anchor=W,
                        justify="left",
                        font=('Gill Sans MT', 13),
                        wraplength=275)
    rightLabel3.place(relx=0.52, rely=0.5)

    # Less secure apps link
    rightLabel4 = Label(root,
                text="Click Here",
                bg='#339900',
                font=('Gill Sans MT', 12),
                fg="black",
                cursor="hand2")
    rightLabel4.place(relx=0.535, rely=0.71)
    rightLabel4.bind("<Button-1>", callback)


    # About Us Button
    img2 = ImageTk.PhotoImage(Image.open("img/buttons/about.png"))
    aboutbutton = Button(root,image=img2, text='', command=aboutUS, padx=10, border=0, cursor='hand2')
    aboutbutton.place(relx=0.63, rely=0.83, bordermode=None)


    # Running Verify event on any key press
    root.bind_all("<KeyPress>", verify)

    # Running SendEmail on Enter
    root.bind('<Return>', sendEmail)

    root.resizable(0,0)
    root.mainloop()

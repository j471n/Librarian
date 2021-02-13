from tkinter import *
from os import  getenv
from tkinter import messagebox
import re
from dotenv import *
import webbrowser
from PIL import ImageTk, Image  #PIL -> Pillow
from .about import aboutUS
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

env = find_dotenv('env/.env')
load_dotenv(env)


def sendEmail(event=None):
    global email, password, msg
    senderEmail = email.get().strip()
    senderPassword = password.get().strip()
    feedback = msg.get('1.0', END).strip()

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

    message = MIMEMultipart("alternative")

    message["Subject"] = "Feedback Mail"
    message["From"] = senderEmail
    message["To"] = receiverEmail

    # Create the HTML version of your message
    html = f"""\
    <html> 
        <body>
            <h1 style="margin-left:30px;">Feedback Email</h1>
            <div style="background-color: black; padding: 30px 40px; border-radius: 30px; margin: 20px; color:white; font-family:sans-serif; box-shadow: 0px 0px 99px -24px #93beffc9; word-wrap: break-word; overflow:hidden !important;">       
                <h6 style="color: white;">Message from <span>&lt;{senderEmail}&gt;</span></h6>
                <p style="color: white;"><b><u>Note:-</u> </b> This is the Feedback Email from Digital Library.</p>
                <p style="color:white;">{feedback}</p>
            </div>        
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    text = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message

    message.attach(text)

    # Create secure connection with server and send email
    try:

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(senderEmail, senderPassword)
            server.sendmail(senderEmail, receiverEmail, message.as_string())

    except(smtplib.SMTPAuthenticationError):
        root.destroy()
        messagebox.showerror("Failed", "Username and Password not accepted")
        return

    except:
        root.destroy()
        messagebox.showerror("Failed", "Something went wrong try again Later")
        return

    root.destroy()
    messagebox.showinfo("Success","Feedback Submitted Successfully")



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

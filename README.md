# LIBRARIAN 

This is Just like a project Report you can read it to get all the information.


## **CONTENTS**

[**INTRODUCTION**](#1)

 - [OVERVIEW](#1.1)
 - [OBJECTIVE](#1.2)
 - [PROGRAMMING LANGUAGES](#1.3)
     - [PYTHON](#1.3.1)
     - [MySQL](#1.3.2)
 - [REQUIREMENTS](#1.4)
     - [Tkinter](#1.4.1)
     - [PyMySQL](#1.4.2)
     - [Python-Dotenv](#1.4.3)
     - [SMTP & MIME](#1.4.4)
     - [Pillow](#1.4.5)

[**FEATURES**](2)
 - [OVERVIEW](#2.1)
 - [Add Book](#2.2)
 - [Delete Book](#2.3)
 - [Issue Book](#2.4)
 - [Return Book](#2.5)
 - [View Book Details](#2.6)
 - [Feedback Form](#2.7)
 - [Update Books Positions](#2.8)
 - [Search Book](#2.9)

[**FUTURE SCOPE**](#3)<br>
[**APPENDIX – A**](#4)<br>
[**REFERENCES**](#5)<br>
[*Contributors*](#6)<br>
[*FAQ*](#7)<br>


<h2 id='1'>INTRODUCTION </h2>

<h3 id='1.1'>OVERVIEW</h3>


This Project is Based on the Digital Library Management System. In which Our aim was to make a GUI application which can be used for managing the books in the Physical Library as the Digital Form. So that user can use it whenever he wants to check the data of books of the Physical Library. So, we came up with this Project which we’ve named as “Digi Library”.




<h3 id='1.2'>OBJECTIVE</h3>

Our objective was simple that this application should perform all that task which is done by Librarian in the Physical form. E.g., Suppose there are several Books in the Physical Library and Librarian will’ve to maintain the register for each book such as Book Name, Book ID, Author, Publication, etc. So, our Project (Librarian) will help Librarian to do that work easily as digital format. Same goes with other operation such as If one wants to issue a Book then Librarian will just put the Details in our application and it’ll do its job. Some more objectives are given below – 

- Remember the position of every book
- Book Issue System
- Return Book System
- View all Books Present in the Library
- Search Through Books
- Add New Books to the Library
- Update the Books Location 



<h3 id='1.3'>PROGRAMMING LANGUAGES</h3>

<h4 id='1.3.1'>Python</h4>

We’ve used Python Programming Language for our project. It’s easy to learn and it is popular too.

Python gives you very vast environment. You can find a library for basically anything you can imagine. You can do more things in the less code. As we mentioned earlier, our objective to make a GUI Application so in this we’ve used “Tkinter” module/library which is very famous for Python GUI Application. It’s an open source and portable library. Tkinter relies on the Tk library, the GUI library which is in C. Python script that use Tkinter doesn’t require modification from one platform to the other. Tkinter is now included in any Python distribution. Therefore, no supplementary modules are required in order to run scripts using Tkinter.


<h4 id='1.3.2'>MySQL</h4>

For keeping the data, we needed a Database. So, we came up with MySQL for keeping and managing the data. MySQL is easy to use and it is secure as well. MySQL is globally renowned for being the most secure and reliable Database Management System. Whether your Platform is Linux, Windows or Mac or UNIX. MySQL is a comprehensive solution with self-management feature. It can handle almost any amount of data, up to as much as 50 million rows or more. It is also considered as one of the fast database languages.

<h3 id='1.4'>REQUIREMENTS</h3>

There are several things we needed to make our project develop so all the things are listed below – 


<h4 id='1.4.1'>Tkiner</h4>

We needed “Tkinter” module/library it is most popular library in order to work in GUI with python. It is open source and portable library. Tkinter relies on the Tk library, the GUI library which is in C. Python script that use Tkinter doesn’t require modification from one platform to the other. Tkinter is now included in any Python distribution. Therefore, no supplementary modules are required in order to run scripts using Tkinter.


<h4 id='1.4.2'>PyMySQL</h4>

It is an interface for connecting to MySQL database server from Python. It implements the Python Database API v2.0 and contains a pure Python MySQL client Library. In order to install PyMySQL using “pip” you need to execute `pip install pymysql` on your terminal. 

<h4 id='1.4.3'>Python-Dotenv</h4>

It reads the key-value pair from `.env` file and adds them to environment variable. It is great for managing app setting during development and in production. It lets you customize you individual working environment variable. Because `.env` file is hidden. In order to install Python Dotenv using `pip` you need to execute `pip install python-dotenv` on your terminal.




<h4 id='1.4.4'>SMTP & MIME</h4>

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers. The [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).") module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

MIME is a kind of *add on or a supplementary protocol* which allows non-ASCII data to be sent through SMTP. It allows the users to exchange different kinds of data files on the Internet: audio, video, images, application programs as well.

<h4 id='1.4.5'>Pillow</h4>

Pillow mostly known as PIL (Python Imaging Library) is a free and open-source additional library to the Python programming Language that adds supports for opening, manipulating, and saving many different image file formats. It supports mostly every format of image. In order to install Pillow using “pip” you need to execute `pip install Pillow` on your terminal.



<h2 id='2'>FEATURES</h2>

<h3 id='2.1'>OVERVIEW</h3>

![Main window](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.008.png)

*Main Window of the Program*


This project is a GUI Application. As we mentioned earlier our aim to perform most of the operation which is done by Library in the Physical form.

This project gives us the complete information about the library. We can enter the record of new books and retrieve the details of books available in the library. We can issue the books to the students and return as well. The system excludes the use of paper work by managing all the book information digitally. Let’s take a look on the features one by one -


<h3 id='2.2'>Add Book</h3>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.011.png)

*It's the main window which to add book to the Library*



In this feature user/Librarian can add the book to the Library but He/She doesn’t have to maintain the register about how many books are in the Library and so on. As the Book come to the Library, He/She can open this application and click on the ADD BOOK button on the Main window. When Librarian click on it, it’ll get a new window in which he/she have to fill the information about book such as Book ID, Title of the Book, Author, Publication and most importantly Location of the which is the physical location where the book is in the Library. All field listed above are mandatory to filled otherwise Application won’t save the Data to the Database. And when he/she added book to the Library it’s status will be automatically *Available* until someone issues the book. Below are some visual samples so you can understand easily -                                                                                        

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.012.png)

(*Figure 1.2*) This is the success message if you get everything Right Then It will show you where book should be Added.



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.014.png) 


(*Figure 1.3*) This error will occur when you accidentally forget to enter details in any of the field such as Author or Publication. Which shows that every field is required.



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.016.png)

(*Figure 1.4)* This error occurs when something goes wrong which is mostly Book Id is already Present in the Library, then you can’t Insert the Same book twice because every book is unique.

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.018.png)

(*Figure 1.5*) This error occurs when You are adding Book and the location you’ve provide is already reserved for another book. Then it will show you that “Position is already Reserved” with the position and book name which should be at that position. For changing the Book location, you can jump to Book Location Updating Feature.



<h3 id='2.3'>Delete Book</h3>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.020.png)

*Figure 2.1 - Main window of Deleting Book*

In this feature user can permanently delete the digital data of any book by just simply providing the Book Id and the Reason why he/she is deleting the book. E.g., Suppose that A book is missing from the Library or just lost by the student So basically it is not in the physical form so user can delete that book from the database too. So, it’s book id and the location can be free. Below are some visual –

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.022.png)

(*Figure 2.2*) You need to make sure that Book Id should be available in the Digital Database e.g., if the Book It is not present in the Database it’ll pop up an error window.



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.024.png)

(*Figure 2.3*) This error will be popup if you forgot to put the Reason of deleting Book which is mandatory and its length should be at least 15 words. Otherwise, you’ll get the same pop up.

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.025.png)


(*Figure 2.4*) This error will occur when you accidentally forgot to enter the Book Id which is mandatory. 

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.027.png)

(*Figure 2.5*) This is the success message if you get everything right then it will show you which book is deleted. And It’ll delete the Book information permanently.



<h3 id='2.4'>Issue Book</h3>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.030.png)
*Figure 3.1 Main window for Issue a Book*


In order to Issue a Book, you need to provide two things first is Book Id and the second is  Student Name who is going to issue the book. When student Successfully issued the book then user will be prompted the location of the where it is stored in the physical form. We’ll see some visuals about that as well. After issuing, the location will be removed from the database but we’ve used separate temporary table to keeps tracks/reserved the location of the books. 



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.034.png)

(*Figure 3.2*) This error pops up when you accidentally forget to fill up any of the field. So, you need to provide all the parameters which is prompted.



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.035.png)


(*Figure 3.3*) This error pops up when you enter the wrong Book ID which must be correct all the time and it should present in our Digital Library.

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.036.png)

(*Figure 3.4*) This is the Success Message when everything goes smoothly then Book will be issued to requested student with Issued Date (It automatically detects issued date) and location of the book as well.

<h3 id='2.5'>Return Book</h3>

## ![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.038.png)

*Figure 4.1 Main window for Return Book*

In order to return a book to the Library user need to provide Just Book ID and Feedback is optional. We’ve thought about making Feedback mandatory. If you want to know why then you can read Future Scope of this project. Book ID should be available in the Database. 


## ![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.039.png)

(*Figure 4.2*) This error pops up when you accidentally forgot to fill up any of the field. So, you need to provide all the parameters which is prompted. Feedback is optional for now.


![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.042.png)

(*Figure 4.3*) This error pops up when you entered the wrong Book ID which is not in the Database. So, you need to make sure Book Id is correct in order to perform this operation.


![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.044.png)

(*Figure 4.4*) This is the Success Message when everything goes smoothly then Book will be Returned and It will show you where to put the Book which we’ve mentioned earlier (using temp table).


<h3 id='2.6'>View Book Details</h3>


![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.047.png)

*Figure 5 - Main window of View Book*

As you can see in the above image there is so much going on. Let me explain one by one. Firstly, you can see the Table which have all the columns required in order to know about the book and its details such as BookID (BID), Title, Author, Publication, Status, Physical Location, Issued Date, Issued to (Student Name). 

So, if the Book is issued then it will show you Issued date and Issued to and physical location will be Null otherwise Issued Date and Issued To will be empty and physical location will be visible. Suppose if student return the book then it will take the Position of the Book from the Temporary Table and put it in the Main Database Table. And it will make and Issued Date and the Issued To empty.

In the Bottom Right you can see that How much book is in the Library and How many are available or issued respectively? There is a Scrollbar in the right through which you can scroll through list. You don’t need a scrollbar but it looks nicer. 

If you click any of the Book then it’ll be highlighted as shown in the image (*Figure 5*), You can even customize the width of the columns according to your configuration.

<h3 id='2.7'>Feedback Form</h3>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.048.png)

*Figure 6.1 Feedback Form*

This is the Feedback form through which users can send us feedback and their experience. It’ll help us to make it more interact and bug free.



User need to type their email Address and Email Password (not actual) as an Input We take that to the SMTP server, which we’ve mentioned earlier. This process is totally secure You don’t need to worry about your password we don’t save any password in our database. Our interface is just a medium to reach us 

But there are two thing which are mandatory to be enabled in order to complete this process, first is [*Less Secure Apps](https://myaccount.google.com/lesssecureapps)* should be enabled and [*Two-Step* verification](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome) is turned on. If both are enabled then go to [APP Password](https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=web) in Google Accounts Settings and create a new password for email to login here. It’ll be your temporary password to perform any Email operation. So, you can use this temporary password which is auto-generated, and you can delete it whenever you want. So, it’s totally secure. Process is shown below- 
<br>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.050.png)

*Figure 6.2*

As shown in *figure 6.2* you need to select the Mail option from dropdown menu and choose the device as windows computer.*  


![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.052.png)

*Figure 6.3*

After selecting the given option Generate button will be enabled then click on Generate button. After that a window will pop up and it’ll show you the random password which is generated in order to perform Email tasks on third party securely.


After that you can use your original Gmail ID and temporary password to send us feedback. In this process no one can take your account data and whenever you want you delete the temporary passwords via just visiting the [App Password Page](https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=web).

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.054.png)

*Figure 6.4*


In figure *6.1* you can see that the Submit Button is Disabled but in *figure 6.4* Button is Enabled. It is because you need to provide the Email and Password in order to send us an Email. Otherwise, it’ll be Disabled.

If you entered an email which doesn’t have any domain it’ll pop up an error shown in *figure 6.3*.So, you need to make Sure Everything is correct. 




<h3 id='2.8'>Update Books Positions</h3>

## ![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.056.png)
*Figure 7.1 - Main window of Update Position*

We’ve implemented this feature so user can easily change the location of book if required.  E.g., Suppose that user want to put the Book from one position to another place then this feature takes place. In that user can provide the Book ID and the Updated Location So, Librarian can change the Address of the Book in the Database.

Main functionality of this feature is based on certain conditions e.g., If Book is already Issued and user want to change the Location of that Book.


So, when user try to change the Book Location it’ll change the Book location when the Book is returned by the Student (When Book is returned Successfully, it’ll give you the new location to put the book at).

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.058.png)

*Figure 7.2 Enabled Update Button*

The Update Button is DISABLE as default, but when user enters both the fields then it’ll be ENABLE as shown in the *figure 7.2* and if you remove the text from of the fields it’ll go back to DISABLE. So, you need to provide both the field in order to change the position of certain book.



![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.060.png)

*Figure 7.3*

*(Figure 7.3)* shows that if user put the wrong Book ID which does not exist then user will get this kind of Box pop up. So, Book ID should be valid in order to perform operation. You only can change the existed Book Location.


![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.062.png)

*Figure 7.4*

*(Figure 7.4)* This warning pop up when user try to change the position of the book from one position to another but the location entered by user is already occupies by another Book. So, user need to make sure that the position he/she is given should not be occupied by some other book.




![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.064.png)

*Figure 7.5*

*(Figure 4.4*) This is the Success message when everything goes smoothly then Book’s Position will be updated which you’ve entered. And if Book is “Available” then it will be Updated immediately otherwise when Student returns the Book. Then it updates Automatically.


<h3 id='2.9'>Search Book</h3>

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.066.png)

*Figure 8.1 Main window to Search*

Search Book is the very important feature of this project. If user want to search for a particular book and its details this is where this feature takes place. User will have plenty of option from which he/she can search about book e.g., BookID, Author, Title, Position, Date, Student Name.

As you can see in *figure 8.1,* Search button is DISABLED. It’ll Enable automatically as soon as user enter the value in Search Field. After clicking on search Field user gets the Result window (*figure 8.2*)

![](https://github.com/j471n/Previews/blob/main/Librarian/Librarian.069.png)

*Figure 8.2 - Result Window*

In *figure 8.2*** you can see that on the top it shows how many results found and how much time it took. And it also shows that what did you search.

Below that There is a table which shows the actual results of you query with all the details. In the Bottom Section there are several buttons (Add Book, Delete Book, View Book Details, Issue Book, Return Book, Feedback, Update Books Positions, Exit) so that user can perform any operation from here if he/she wants. User doesn’t have to go to the main window for that. 


<h2 id='3'>Future Scope</h2>

There are many features we are currently working on. We will implement them as soon as the testing and coding is over. Below is a little brief about them - 

- We are working on Creating the Database which keeps tracks of all the Students who study in our college, who has ID Card/Library Card. If we implement this then Issuing Book System will be change from Student Name to Student ID.  

    In this user will get a new feature from which he/she can add the student to database or remove the Student from the Database. If Student is not registered or he/she doesn’t have Student ID. Then he/she cannot issue the book from the Library. 


- We are working on Fine System. So, when user Return the Book after due date then, he/she will be charged for some amount. We are not going to user Payment Gateway or any of the Bank Credential. We’ll just put that fine amount to that student, so whenever he wants to issue another book then user will get notification that how much charges are due for particular Student, and the student will also get an email regarding to their fine.

    
    We’ll also going to make the check-in window in which user can see how much profit they get from fine. And it’ll also going to keeps track of which book is most fine Paid Book and which student paid the most amount.

- We are also going to work on Feedback Section when user Returns a Book. We’ll also make another Entry for Rating as well. So, user can keep track about the rating for each book. From which user can check which book has best and worst rating.

<h2 id='4'>APPENDIX – A</h2>
There are some brief about function we’ve use -

<br>

|**Functions Name**|**Work**|
| :- | :- |
|Tk()|The [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.|
|.title()|This gives title to the root window.|
|.iconbitmap()|This gives icon to the root window|
|.geometry()|This set the window size (Width x Height)|
|Image.open()|Opens and identifies the given image file.|
|.resize()|It resizes the image with give ratio.|
|Image.ANTIALIAS|**Image anti-aliasing** is the smoothing of edges and colors in digital **images** and fonts.|
|ImageTk.PhotoImage()|to initialize the photo image object.|
|Label()|This widget implements a display box where you can place text or images|
|.pack()|This geometry manager organizes widgets in blocks before placing them in the parent widget.|
|.place()|This geometry manager organizes widgets by placing them in a specific position in the parent widget.|
|.grid()|This geometry manager organizes widgets in a table-like structure in the parent widget.|
|Frame()|The Frame widget is use for grouping and organizing other widgets. It works like a container.|
|.resizable()|This method is used to allow Tkinter root window to change its size according to the users need|
|.mainloop()|This method listens for events, such as button clicks or keypresses.|
|webbrowser.open()|It opens URL in the default browser|
|datetime.now()|Return current time|
|Toplevel()|A Toplevel widget is used to create a window on top of all other windows.|
|.config()|It is used to access an object's attributes after its initialization|
|.get()|Returns the entry’s current text as a string. |
|Entry()|The Entry Widget is a Tkinter Widget used to Enter or display a single line of text. |
|Text()|Text widgets provide advanced capabilities that allow you to edit a multiline text and format the way it has to be displayed, such as changing its color and font|
|messagebox.showerror()|Display the error message to the user.|
|messagebox.showwarning()|Display the warning to the user.|
|messagebox.showinfo()|Show some relevant information to the user.|
|re.findall()|search for “all” occurrences that match a given pattern|
|re.sub()|Return the string obtained by replacing the leftmost non-overlapping occurrences of *pattern* in *string* by the replacement *repl*|
|re.search()|search the regular expression pattern and return the first occurrence|
|Button()|The Button widget is used to add buttons in a Python application.|
|.bind()|Bind Mouse buttons with Tkinter Frame |
|.bind\_all()|Binding keyboard buttons with the root window|
|getenv()|Python returns the value of the environment variable key if it exists otherwise returns the default value|
|load\_dotenv()|It loads environment variables from a file named “.env” in the current directory|
|ttk.Radiobutton()|It Display the Modern Radio Buttons on the root window. |
|ttk.Entry()|It Display the Modern Entry on the root window|
|ttk.Treeview()|It displays the Table on the root window.|
|Scrollbar()|It creates the Scrollbar|
|ttk.Style()|It changes the style of the widgets.|
|.map()|Query or sets dynamic values of the specified option(s) in *style*.|
|pymysql.connect()|It connects with MySQL database|
|con.Cursor()|t gives us the ability to have multiple separate working environments through the same connection to the database|
|con.Commit()|This method sends a **COMMIT** statement to the MySQL server|
|cur.execute()|It allows us to execute the SQL queries|
|.destroy()|Destroy the window|
|MIMEText()|This class is used to create MIME objects of major type *text*.|
|.attach()|To attach the text, media, etc.|
|Server.login()|Login to SMTP server |
|Server.sendemail()|Send email to requested user|
|ssl.create\_default\_context()|class is used to create MIME objects of major type *text* and usually represent a higher security level than when calling the [SSLContext](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") constructor directly.|


<h2 id='5'>REFERENCES</h2>

 - [Wikipedia](https://www.wikipedia.org/)

 - [Stack Overflow](https://stackoverflow.com/)

 - [Reddit](https://www.reddit.com/)

 - [Quora](https://www.quora.com/)

 - [Stack Exchange](https://stackexchange.com/)

 - [Python Docs](https://docs.python.org/)

 - [PyPI](https://pypi.org/)




<h3 id='6'>Contributors</h3>

 - [Jatin Sharma](https://github.com/j471n/)
 - [Anubhav Srivastava](https://github.com/Anubhav-Sri-04)


<h3 id='7'>FAQs</h3>

 - [How to install Python?](https://www.python.org/downloads/)
 - [How to install PIP in windows?](https://phoenixnap.com/kb/install-pip-windows)
 - [How to install packages in Python using PIP?](https://datatofish.com/install-package-python-using-pip/)

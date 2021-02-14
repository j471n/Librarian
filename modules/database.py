from os import getenv
import sqlite3
from dotenv import *

env = find_dotenv('env/.env')
load_dotenv(env)


def connectDB():
    # try:
    global con, cur

    # Connecting to the Database
    con = sqlite3.connect(getenv('DATABASE'))
    cur = con.cursor()  #cur -> cursor
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = len(cur.fetchall())
    
    if tables < 3:

        # SQL
        q1 = "CREATE TABLE books (book_id varchar(200) NOT NULL, title varchar(50), author varchar(30),publication varchar(100), status varchar(30),phyLocation varchar(50),issued_date varchar(15),issued_to varchar(25),PRIMARY KEY (book_id));"

        q2 = 'CREATE TABLE position (bid varchar(200) NOT NULL,location varchar(50),PRIMARY KEY (bid));'

        q3 = "CREATE TABLE students (student_id INTEGER NOT NULL UNIQUE, student_name VARCHAR(50), dob VARCHAR(15), course VARCHAR(20), branch VARCHAR(10), address VARCHAR(100), contact VARCHAR(20), img BLOB, g_year INTEGER, gender VARCHAR(10), fine INTEGER CONSTRAINT fine_d DEFAULT 0, PRIMARY KEY('student_id' AUTOINCREMENT));"

        con = sqlite3.connect(getenv('DATABASE'))
        con.execute(q1)
        con.execute(q2)
        con.execute(q3)
        con.commit()

        print("Database Connected, New Created")
    else:
        print("Database Connected, Already Existed.")

connectDB()
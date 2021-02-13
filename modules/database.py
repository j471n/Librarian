from os import getenv
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def connectDB():
    # try:
    global con, cur

    # Connecting to the Database
    con = sqlite3.connect(getenv('DATABASE'))
    cur = con.cursor()  #cur -> cursor
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")


    if len(cur.fetchall()) == 0:

        # SQL
        q1 = "CREATE TABLE books (book_id varchar(200) NOT NULL, title varchar(50), author varchar(30),publication varchar(100), status varchar(30),phyLocation varchar(50),issued_date varchar(15),issued_to varchar(25),PRIMARY KEY (book_id));"
        q2 = 'CREATE TABLE position (bid varchar(200) NOT NULL,location varchar(50),PRIMARY KEY (bid));'

        con = sqlite3.connect(getenv('DATABASE'))
        con.execute(q1)
        con.execute(q2)
        con.commit()

        print("Database Connected, New Created")
    else:
        print("Database Connected, Already Existed.")

connectDB()
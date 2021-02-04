from os import getenv
import pymysql
from dotenv import load_dotenv

load_dotenv()


def connectDB():
    try:
        global con, cur
        # Connecting to the Database
        con = pymysql.connect(host=getenv('HOST'),
                              user=getenv('USER'),
                              password=getenv('DB_PASS'),
                              database=getenv('DB_NAME'))
        cur = con.cursor()  #cur -> cursor
        print("Database Connected, Already Existed.")

    except:

        # SQL
        q1 = f"CREATE DATABASE {getenv('DB_NAME')};"
        q2 = f"use {getenv('DB_NAME')};"
        q3 = 'CREATE TABLE books (book_id VARCHAR(200) PRIMARY KEY, title VARCHAR(50), author VARCHAR(30),publication VARCHAR(100), status VARCHAR(30), phyLocation VARCHAR(50), issued_date VARCHAR(15), issued_to VARCHAR(25));'
        q4 = "CREATE TABLE position (bid VARCHAR(200) PRIMARY KEY, location VARCHAR(50));"
        con = pymysql.connect(host=getenv('HOST'),
                              user=getenv('USER'),
                              password=getenv('DB_PASS'))
        cur = con.cursor()

        cur.execute(q1)
        con.commit()
        cur.execute(q2)
        con.commit()
        cur.execute(q3)
        con.commit()
        cur.execute(q4)
        con.commit()

        # Connecting to the Database
        con = pymysql.connect(host=getenv('HOST'),
                              user=getenv('USER'),
                              password=getenv('DB_PASS'),
                              database=getenv('DB_NAME'))
        cur = con.cursor()
        print("Database Connected, New Created")


connectDB()
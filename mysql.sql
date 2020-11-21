-- To Creating Database
CREATE DATABASE db;

-- To Creating books Table
CREATE TABLE books (book_id VARCHAR(200) PRIMARY KEY, title VARCHAR(50), author VARCHAR(30),publication VARCHAR(100), status VARCHAR(30));

-- To Creating Book_issued Table
CREATE TABLE books_issued (bid VARCHAR(200) PRIMARY KEY, issuedto VARCHAR(50),issued_date VARCHAR(15));
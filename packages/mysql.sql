-- To Creating Database
CREATE DATABASE db;

-- To Creating books Table
CREATE TABLE books (book_id VARCHAR(200) PRIMARY KEY, title VARCHAR(50), author VARCHAR(30),publication VARCHAR(100), status VARCHAR(30), phyLocation VARCHAR(50), issued_date VARCHAR(15), issued_to VARCHAR(25));

-- To Track the Book Position
CREATE TABLE position (bid VARCHAR(200) PRIMARY KEY, location VARCHAR(50));

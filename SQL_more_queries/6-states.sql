-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa

-- creates a table on this database
CREATE TABLE IF NOT EXISTS states (
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
NAME VARCHAR(256) NOT NULL
);
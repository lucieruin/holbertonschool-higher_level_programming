-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS user_0d_2;

-- creates he user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- add privilege for this user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
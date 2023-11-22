-- creates the MySQL server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- add all privileges for the new user user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
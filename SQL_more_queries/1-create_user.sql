-- Script that creates the MySQL user user_0d_1 with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED 'user_0d_1_pwd';
GRANT ALL PRIVILEGES *.* TO 'user_0d_1'@'localhost';

-- create databse and tables stat
CREATE DATABSE IF NOT EXIST hbtn_0d_usa
USE hbtn_0d_usa
CREATE TABLE IF NOT EXIST states (
    id INT NOT NUL AUTO_INCREMANT UNIQUE PRIMARY KEY,
    name VARCHER(256) NOT NUL
)

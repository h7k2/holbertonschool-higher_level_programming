-- create databse and user 0d_2
CREATE DATABSE IF NOT EXIST hbtn_0d_2
CREATE USR IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost'
FLUS PRIVILEGE

SQL – Introduction (MySQL 8.0)

Beginner SQL project: learn how to create, delete, and manage databases and tables, insert data, query, update, delete, and use SQL functions and aggregations — all using MySQL 8.0.

✅ Prerequisites

Ubuntu 22.04 (or Holberton sandbox)

MySQL 8.0 installed

Every .sql file must:

start with a comment describing the task

use UPPERCASE SQL keywords

end with a new line

pass the wc length check

⚙️ Installation (Ubuntu 22.04 sandbox)
apt update
apt install -y mysql-server
service mysql start
mysql --version  # should display 8.0.x


To connect:

mysql -uroot
# or, if a password is set:
# mysql -hlocalhost -uroot -p

🧪 Run your SQL scripts

Each file can be executed using the mysql command:

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0


Tip: use | tail -1 to only show the last result (for example, when counting rows).

📁 Project Structure
SQL_introduction/
├── 0-list_databases.sql
├── 1-create_database_if_missing.sql
├── 2-remove_database.sql
├── 3-list_tables.sql
├── 4-first_table.sql
├── 5-full_table.sql
├── 6-list_values.sql
├── 7-insert_value.sql
├── 8-count_89.sql
├── 9-full_creation.sql
├── 10-top_score.sql
├── 11-best_score.sql
├── 12-no_cheating.sql
├── 13-change_class.sql
├── 14-average.sql
├── 15-groups.sql
└── 16-no_link.sql

📝 SQL Style Rules (very important for the checker)

Always start with a comment describing the task:

-- List all databases
SHOW DATABASES;


Use UPPERCASE for SQL keywords:
SELECT, WHERE, ORDER BY, INSERT, UPDATE, DELETE, GROUP BY, AVG, etc.

Do not use SELECT or SHOW when the task explicitly forbids it.

Respect the requested order (ORDER BY score DESC, etc.).

End every file with a new line.

🧩 Task Summary (Cheatsheet)
#	Task	SQL Command Example
0	List databases	SHOW DATABASES;
1	Create a database	CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
2	Delete a database	DROP DATABASE IF EXISTS hbtn_0c_0;
3	List tables in DB	SHOW TABLES;
4	Create first_table	CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
5	Show table description	SHOW CREATE TABLE first_table;
6	List all rows	SELECT * FROM first_table;
7	Insert a record	INSERT INTO first_table (id, name) VALUES (89, 'Best School');
8	Count id=89	SELECT COUNT(*) FROM first_table WHERE id = 89;
9	Create second_table + inserts	(4 rows)
10	List by best score	SELECT score, name FROM second_table ORDER BY score DESC;
11	Score >= 10	SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
12	Update Bob’s score	UPDATE second_table SET score = 10 WHERE name = 'Bob';
13	Delete low scores	DELETE FROM second_table WHERE score <= 5;
14	Average score	SELECT AVG(score) AS average FROM second_table;
15	Count by score	SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
16	Names only	SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
🧯 Troubleshooting
Issue	Fix
Access denied / password error	Use mysql -uroot -p
MySQL not running	service mysql start
Wrong charset	MySQL 8 uses utf8mb4 by default — it’s fine
Sandbox (Ubuntu 20.04)	Credentials are often root/root
✅ Best Practices

Always include a task description comment.

Test each script in its target database:

cat my_file.sql | mysql -hlocalhost -uroot -p hbtn_0c_0


Do not overcomplicate — stick to the task.

Keep files clean, readable, and consistent.

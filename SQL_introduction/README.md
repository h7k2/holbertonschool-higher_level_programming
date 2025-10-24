SQL – Introduction (MySQL 8.0)

A beginner SQL project: create/delete databases and tables, insert, select, update, delete data, and use SQL functions and aggregations — all using MySQL 8.0.

✅ Prerequisites

Ubuntu 22.04 (or Holberton sandbox)

MySQL 8.0

All .sql files must:

start with a comment describing the task

use UPPERCASE SQL keywords

end with a new line

pass the wc length check

⚙️ Quick Installation (Ubuntu 22.04 sandbox)
apt update
apt install -y mysql-server
service mysql start
mysql --version  # should display 8.0.x


Connection:

mysql -uroot
# or with password:
# mysql -hlocalhost -uroot -p

🧪 Running Your Scripts

Each file can be executed with MySQL through standard input:

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0


💡 Tip: To see only the last result (for example, when counting), you can chain with | tail -1.

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

📝 Style Guidelines (very important for the checker)

Each file must start with a comment describing the task:

-- List all databases
SHOW DATABASES;


Rules:

Use UPPERCASE for SQL keywords: SELECT, WHERE, ORDER BY, INSERT, UPDATE, DELETE, GROUP BY, AVG, etc.

Do not use SELECT or SHOW when the instructions forbid it (for example, table creation without verification).

Always respect the required order (e.g., ORDER BY score DESC).

Always end your file with a new line.

🧩 Task Summary (Mini-Cheatsheet)
#	Task	Example SQL
0	List all databases	SHOW DATABASES;
1	Create database if missing	CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
2	Delete database if exists	DROP DATABASE IF EXISTS hbtn_0c_0;
3	List all tables in a database	SHOW TABLES;
4	Create first_table (id INT, name VARCHAR(256))	CREATE TABLE IF NOT EXISTS ...
5	Describe table without DESCRIBE	SHOW CREATE TABLE first_table;
6	List all rows	SELECT * FROM first_table;
7	Insert (89, 'Best School')	INSERT INTO first_table (id, name) VALUES (89, 'Best School');
8	Count id = 89	SELECT COUNT(*) FROM first_table WHERE id = 89;
9	Create second_table and insert multiple rows	—
10	List second_table by score (desc)	SELECT score, name FROM second_table ORDER BY score DESC;
11	List rows with score ≥ 10	SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
12	Update Bob’s score to 10	UPDATE second_table SET score = 10 WHERE name = 'Bob';
13	Delete rows with score ≤ 5	DELETE FROM second_table WHERE score <= 5;
14	Calculate average score	SELECT AVG(score) AS average FROM second_table;
15	Group by score and count records	SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
16	List only non-empty names	SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
🧯 Troubleshooting
Problem	Solution
“Access denied” / password error	Use mysql -uroot -p
MySQL service not running	Run service mysql start
Wrong charset	MySQL 8 uses utf8mb4 by default → no issue
Old 20.04 sandbox	Credentials are usually root/root
✅ Best Practices

Always start your file with a clear comment.

Test each script in the correct database:

cat my_file.sql | mysql -hlocalhost -uroot -p hbtn_0c_0


Don’t over-optimize — follow the task exactly.

Keep your scripts clean, readable, and simple.

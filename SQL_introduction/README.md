SQL – Introduction (MySQL 8.0)

Petit projet d’initiation SQL : créer/effacer des bases, tables, insérer, sélectionner, mettre à jour, supprimer, fonctions et agrégations – le tout sur MySQL 8.0.

✅ Prérequis

Ubuntu 22.04 (ou sandbox Holberton)

MySQL 8.0

Tous les fichiers .sql :

commencent par un commentaire décrivant la tâche

ont les mots-clés SQL en MAJUSCULES

se terminent par une nouvelle ligne

passent wc pour la longueur

⚙️ Installation rapide (sandbox Ubuntu 22.04)
apt update
apt install -y mysql-server
service mysql start
mysql --version  # doit afficher 8.0.x


Connexion :

mysql -uroot
# ou avec mot de passe :
# mysql -hlocalhost -uroot -p

🧪 Exécuter vos scripts

Chaque fichier s’exécute avec mysql en entrée standard :

cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0


Astuce : pour ne voir que le dernier résultat (ex. comptage), vous pouvez chaîner avec | tail -1.

📁 Arborescence
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

📝 Rappels de style (très importants pour le checker)

Un commentaire en tête de fichier décrivant la tâche :

-- List all databases
SHOW DATABASES;


MAJUSCULES pour les mots-clés : SELECT, WHERE, ORDER BY, INSERT, UPDATE, DELETE, GROUP BY, AVG, …

Pas de SELECT/SHOW si l’énoncé le déconseille (ex. création sans vérification).

Respecter l’ordre demandé (ex. ORDER BY score DESC).

Toujours une nouvelle ligne en fin de fichier.

🧩 Résumé des tâches (mini-cheatsheet)

0 – Lister les BDD : SHOW DATABASES;

1 – Créer BDD si absente : CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

2 – Supprimer BDD si présente : DROP DATABASE IF EXISTS hbtn_0c_0;

3 – Lister les tables d’une BDD : SHOW TABLES;

4 – Créer first_table (id INT, name VARCHAR(256)) : CREATE TABLE IF NOT EXISTS ...

5 – Décrire sans DESCRIBE : SHOW CREATE TABLE first_table;

6 – Lister lignes : SELECT * FROM first_table;

7 – Insérer (89, 'Best School') : INSERT INTO first_table (id, name) VALUES (89, 'Best School');

8 – Compter id=89 : SELECT COUNT(*) FROM first_table WHERE id = 89;

9 – Créer second_table + plusieurs INSERT

10 – Lister second_table par score desc (afficher score, name)

11 – Lister score >= 10 (score, name) ordonné desc

12 – Mettre Bob à score=10 sans utiliser l’id : UPDATE second_table SET score=10 WHERE name='Bob';

13 – Supprimer score <= 5 : DELETE FROM second_table WHERE score <= 5;

14 – Moyenne : SELECT AVG(score) AS average FROM second_table;

15 – Grouper par score + compter (alias number) + ORDER BY number DESC

16 – Lister sans name vide/NULL, afficher score, name, ORDER BY score DESC

🧯 Dépannage

“Access denied” / mot de passe : assurez-vous d’utiliser -uroot -p si nécessaire.

Service MySQL down : service mysql start

Charset : MySQL 8 utilise utf8mb4 par défaut → OK pour ces exercices.

Sandbox 20.04 (ancien) : identifiants souvent root/root.

✅ Bonnes pratiques

Commencer par un commentaire clair.

Tester chaque script dans la BDD cible (… | mysql -hlocalhost -uroot -p hbtn_0c_0).

Ne pas “sur-optimiser” : respecter strictement l’énoncé.

Conserver les fichiers simples et lisibles.

👤 Auteur

Projet Holberton School – Foundations v2.1 · Part 2
Par : Guillaume — Adapté & README par toi ✨

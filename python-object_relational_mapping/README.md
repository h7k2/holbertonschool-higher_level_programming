Python – Object-Relational Mapping (ORM)

Holberton – Foundations v2.1 · Part 2

Lien entre Python et MySQL : d’abord avec MySQLdb (SQL direct), puis avec SQLAlchemy (ORM, sans écrire de SQL).

📦 Contenu du dépôt
holbertonschool-higher_level_programming/
└── python-object_relational_mapping/
    ├── 0-select_states.py
    ├── 1-filter_states.py
    ├── 2-my_filter_states.py
    ├── 3-my_safe_filter_states.py
    ├── 4-cities_by_state.py
    ├── 5-filter_cities.py
    ├── model_state.py
    ├── 6-model_state.py
    ├── 7-model_state_fetch_all.py
    ├── 8-model_state_fetch_first.py
    ├── 9-model_state_filter_a.py
    ├── 10-model_state_my_get.py
    ├── 11-model_state_insert.py
    ├── 12-model_state_update_id_2.py
    ├── 13-model_state_delete_a.py
    ├── model_city.py
    └── 14-model_city_fetch_by_state.py

✅ Prérequis & versions

OS : Ubuntu 20.04 LTS

Python : 3.8.5

MySQL Server : 8.0 (localhost:3306)

mysqlclient / MySQLdb : 2.0.x (pip3 install mysqlclient==2.0.3)

SQLAlchemy : 1.4.x (ex. 1.4.22)

Style : pycodestyle 2.7.*

Tous les fichiers :

commencent par #!/usr/bin/python3

sont exécutables

ont docstrings (module, classes, fonctions)

se terminent par une nouvelle ligne

🔧 Installation
# MySQL
sudo apt update
sudo apt install mysql-server
mysql --version  # => 8.0.x

# Dépendances Python pour MySQLdb
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3

# SQLAlchemy
sudo pip3 install SQLAlchemy==1.4.22

🗃️ Jeux de données d’exemple

Charger un SQL d’exemple :

cat 0-select_states.sql | mysql -uroot -p

🚀 Exécution (partie MySQLdb – SQL direct)
# 0. Lister tous les states (tri par id)
./0-select_states.py root root hbtn_0e_0_usa

# 1. Lister les states qui commencent par 'N'
./1-filter_states.py root root hbtn_0e_0_usa

# 2. Filtrer par nom (volontairement vulnérable – demandé)
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

# 3. Version sécurisée (anti-injection SQL)
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'

# 4. Villes + états (JOIN), une seule execute()
./4-cities_by_state.py root root hbtn_0e_4_usa

# 5. Villes d’un état (sécurisé), une seule execute()
./5-filter_cities.py root root hbtn_0e_4_usa 'Texas'

🔒 Injection SQL (rappel)

❌ À éviter (tâche 2 seule l’exige) :

"SELECT ... WHERE name = '{}'".format(user_input)


✅ Correct / sécurisé (tâche 3 et 5) :

cursor.execute("SELECT ... WHERE name = %s", (user_input,))

🧱 ORM & Modélisation (SQLAlchemy)
model_state.py

Base = declarative_base()

Table states :

id (PK, int, autoincr, not null)

name (varchar(128), not null)

⚠️ Importer toutes les classes héritant de Base avant Base.metadata.create_all(engine).

Commandes utiles
# 6. Créer la table states via create_all
./6-model_state.py root root hbtn_0e_6_usa

# 7. Tous les State (ordre par id)
./7-model_state_fetch_all.py root root hbtn_0e_6_usa

# 8. Premier State (ou "Nothing")
./8-model_state_fetch_first.py root root hbtn_0e_6_usa

# 9. États contenant 'a'
./9-model_state_filter_a.py root root hbtn_0e_6_usa

# 10. Obtenir l’id d’un state par nom (sécurisé)
./10-model_state_my_get.py root root hbtn_0e_6_usa 'Texas'

# 11. Ajouter “Louisiana” (affiche l’id)
./11-model_state_insert.py root root hbtn_0e_6_usa

# 12. Renommer id=2 en “New Mexico”
./12-model_state_update_id_2.py root root hbtn_0e_6_usa

# 13. Supprimer les states contenant 'a'
./13-model_state_delete_a.py root root hbtn_0e_6_usa

Villes (tâche 14)

model_city.py : classe City → table cities

id (PK, int, autoincr, not null)

name (varchar(128), not null)

state_id (FK → states.id, not null)

14-model_city_fetch_by_state.py : sortie :

<state name>: (<city id>) <city name>

./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa

🧭 Bonnes pratiques

MySQLdb : requêtes paramétrées (%s) pour toute entrée utilisateur (sauf tâche 2).

SQLAlchemy : pas de engine.execute() ; utiliser Session, query(), filter(), order_by(), first(), all().

Tri : respecter ORDER BY ... ASC.

Affichage : coller aux formats d’exemple.

Style : docstrings claires, fichiers exécutables, fin de fichier avec newline.

🧩 Dépannage

ModuleNotFoundError: No module named 'MySQLdb'
→ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev && sudo pip3 install mysqlclient==2.0.3

Connexion refusée
→ sudo service mysql status, vérifier port 3306 et identifiants.

sqlalchemy.exc.OperationalError
→ DB inexistante / mauvais credentials / socket : vérifier l’URL :
mysql+mysqldb://USER:PASSWORD@localhost/DB_NAME

🎯 Objectifs pédagogiques

Se connecter à MySQL en Python (MySQLdb).

Exécuter SELECT / INSERT / UPDATE / DELETE.

Comprendre l’ORM et mapper des classes Python à MySQL.

Manipuler des objets avec SQLAlchemy sans SQL direct.

Respecter contraintes d’E/S (tri, format, 1 seule exécution, etc.).

**Analyses et exposition des données spotify:**
Ce projet vise à extraire des données spotify dans un fichier CSV ensuite les transformer (nettoyer) et les charger dans une base de donnée Mongodb, puis exposer ces données via API FasteAPI, pour permettre des opérations CRUD et des statistiques.

**Structure du projet:**
TP/
│── Data/                  # Dossier contenant les fichiers de données CSV
│── scripts/               # Scripts de traitement des données
│   │── extract.py         # Extraction des données depuis le CSV
│   │── transform.py       # Nettoyage et transformation des données
│   │── load.py            # Chargement des données dans MongoDB
│── requirements.txt       # Dépendances du projet
│── README.md              # Documentation du projet

📌 Le fichier extract.py permet de lire le fichier CSV et de charger les données dans un DataFrame Pandas.

📌 Le fichier transform.py effectue les opérations suivantes :

Remplacement des valeurs manquantes par "unknown"

Conversion de la colonne ts en format datetime

Conversion de ms_played en entier et ajout de minutes_played

Extraction du jour de la semaine (day_of_week) et de l'heure (hour_of_day)

Nettoyage des chaînes de caractères (suppression des espaces inutiles, format en title case)

Suppression des doublons et filtrage des écoutes de moins de 5 secondes

📌 Le fichier load.py insère les données nettoyées dans la base MongoDB 
*on doit se connecter sur mongodb avec le shell et on doit instaler mongodb compass, on tape les commandes suivantes:
🔧mongod --dbpath ~/data/db
🔧on ouvre un autre terminale et on tape: mongosh
cela permet de démarrer directement MongoDB Compass, ou on verra la base de donnée crée avec la collection et les documents insérer sous forme json.

On verifie que les données sont bien insérer sur la base de donnée MongoDB.

🔧 Requirement.txt contient toutes les dépendances nécéssaire pour le projet.

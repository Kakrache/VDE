# Analyse et Exposition des Données Spotify

Ce projet permet d'extraire des données Spotify depuis un fichier CSV, de les transformer et de les charger dans une base de données MongoDB. Ensuite, une API FastAPI est exposée pour gérer les données via des opérations CRUD et des statistiques.

# Structure du projet

TP/
│── Data/                  # Dossier contenant les fichiers de données CSV
│── scripts/               # Scripts de traitement des données
│   │── extract.py         # Extraction des données depuis le CSV
│   │── transform.py       # Nettoyage et transformation des données
│   │── load.py            # Chargement des données dans MongoDB
│── fastapi_app/           # Dossier contenant l'application FastAPI
│   │── main.py            # Point d'entrée de l'API FastAPI
│── dags/                  # Dossier contenant les scripts d'automatisation Airflow
│   │── spotify_pipeline_dag.py # Script Airflow pour l'orchestration du pipeline
│── requirements.txt       # Liste des dépendances du projet
│── README.md              # Documentation du projet
Étapes pour lancer l'application

# 1. Installer MongoDB
Pour stocker les données, MongoDB doit être installé et exécuté. Voici les étapes pour démarrer MongoDB sur ton environnement local.

**a. Démarrer MongoDB:**

Ouvre un terminal et exécute les commandes suivantes pour démarrer MongoDB :

mongod --dbpath ~/data/db
**b. Connexion à MongoDB:**

Ouvre un autre terminal et lance MongoDB avec mongosh :

mongosh
Cela permettra de démarrer MongoDB Compass et tu pourras voir la base de données et les collections créées avec les documents insérés au format JSON.

# 2. Installer les dépendances du projet
Avant de commencer, il est nécessaire d'installer toutes les dépendances du projet. Utilise pip pour cela :

pip install -r requirements.txt

# 3. Exécuter le pipeline de traitement des données
Le pipeline de traitement des données est constitué de trois étapes : extraction, transformation, et chargement dans MongoDB. Pour exécuter le script qui orchestre cela, exécute la commande suivante::

**cd dags --->aller dans le répertoire du fichier:**

**python spotify_pipeline_dag.py:**

Ce script Airflow va lire les données du fichier CSV, les transformer, et les charger dans MongoDB.

# 4. Lancer l'API FastAPI
Une fois les données chargées dans MongoDB, tu peux lancer l'API FastAPI pour exposer les opérations CRUD et les statistiques.

**a. Navigue jusqu'au dossier fastapi_app:**

cd fastapi_app

**b. Lance l'API avec Uvicorn:**

uvicorn main:app --reload

Cela démarrera le serveur FastAPI sur http://127.0.0.1:8000. L'API sera disponible pour recevoir des requêtes.

# 5. Accéder à la documentation de l'API
Une fois l'API lancée, tu peux accéder à la documentation interactive générée automatiquement par FastAPI via Swagger UI à l'adresse suivante :


http://127.0.0.1:8000/docs
Tu peux y tester toutes les routes CRUD ainsi que les statistiques de manière interactive.

# 6. Vérification des données dans MongoDB
Pour vérifier que les données ont été correctement insérées dans MongoDB, tu peux naviguer dans MongoDB Compass et consulter la base de données, la collection, et les documents insérés.

**Pour resumé, le Dags est un workflow qui exécute les tâches dans un ordre bien définit:**
*Automatisé le pipeline ETL
*définir les étapes du pipeline sous forme de taches
*Planifier l'éxecution de ces taches avec intervalle régulier
*Gérer les erreurs et surveiller les éxecutions vial'interface Airflow

Ce fichier est le point d'entrée de ton API FastAPI. Il permet :
*D'exposer les données stockés dans mongodb via endpoints RESET (CRUD et statistiques)
*Intéragir avec les données via des requêtes HTTP(GET, POST, PUT, DELETE )
*De sezrvir de backend pour toute applications front qui consommerait ces 
données.

**Pour tester notre API:**
avec une requête POST avec Postman, on clique sur la boutton **"Try it out":** de la méthode **POST :**---> Requete Body---> on selectionne le json puis on colle ici ----> on **execute:**
Ensuite on a sur Mongodb Compass, on refresh, et on, vois bien si le document est bien insérer dans notre collection. on peut tester les autres méthode **DELETE:**, **GET:** etc 
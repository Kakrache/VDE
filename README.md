**Analyse et Exposition des Données Spotify:**

Ce projet permet d'extraire des données Spotify depuis un fichier CSV, de les transformer et de les charger dans une base de données MongoDB. Ensuite, une API FastAPI est exposée pour gérer les données via des opérations CRUD et des statistiques.

**Structure du projet:**

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

1. Installer MongoDB
Pour stocker les données, MongoDB doit être installé et exécuté. Voici les étapes pour démarrer MongoDB sur ton environnement local.

a. Démarrer MongoDB

Ouvre un terminal et exécute les commandes suivantes pour démarrer MongoDB :

mongod --dbpath ~/data/db
b. Connexion à MongoDB

Ouvre un autre terminal et lance MongoDB avec mongosh :

mongosh
Cela permettra de démarrer MongoDB Compass et tu pourras voir la base de données et les collections créées avec les documents insérés au format JSON.

2. Installer les dépendances du projet
Avant de commencer, il est nécessaire d'installer toutes les dépendances du projet. Utilise pip pour cela :


pip install -r requirements.txt
3. Exécuter le pipeline de traitement des données
Le pipeline de traitement des données est constitué de trois étapes : extraction, transformation, et chargement dans MongoDB. Pour exécuter le script qui orchestre cela, exécute la commande suivante :


cd dags
python spotify_pipeline_dag.py
Ce script Airflow va lire les données du fichier CSV, les transformer, et les charger dans MongoDB.

4. Lancer l'API FastAPI
Une fois les données chargées dans MongoDB, tu peux lancer l'API FastAPI pour exposer les opérations CRUD et les statistiques.

a. Navigue jusqu'au dossier fastapi_app :

cd fastapi_app
b. Lance l'API avec Uvicorn :


uvicorn main:app --reload
Cela démarrera le serveur FastAPI sur http://127.0.0.1:8000. L'API sera disponible pour recevoir des requêtes.

5. Accéder à la documentation de l'API
Une fois l'API lancée, tu peux accéder à la documentation interactive générée automatiquement par FastAPI via Swagger UI à l'adresse suivante :

http://127.0.0.1:8000/docs
Tu peux y tester toutes les routes CRUD ainsi que les statistiques de manière interactive.

6. Vérification des données dans MongoDB
Pour vérifier que les données ont été correctement insérées dans MongoDB, tu peux naviguer dans MongoDB Compass et consulter la base de données, la collection, et les documents insérés.

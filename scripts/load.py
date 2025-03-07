#charger les données dans mongodb
import pandas as pd
import pymongo
from pymongo import MongoClient
print(pymongo.__version__)

df = pd.read_csv("data/data_cleaned.csv", sep = ',', encoding = "utf-8")

# Connexion au serveur MongoDB (localhost:27017)
client = MongoClient("mongodb://localhost:27017")

# Sélection de la base de données
db = client["spotify_history"]
collection = db["history_data"]
print("Connexion réussie à MongoDB !")


data_to_insert = df.to_dict(orient='records')
collection.insert_many(data_to_insert)


for doc in collection.find().limit(5):
    print(doc)


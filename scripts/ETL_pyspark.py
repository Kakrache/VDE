from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pymongo import MongoClient
from pyspark.sql.functions import col, to_date, dayofweek, hour, trim, initcap
from pyspark.sql.types import IntegerType
import pandas as pd


spark = SparkSession.builder \
    .appName("SpotifyData") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/spotify_history_S.history") \
    .getOrCreate()


df = spark.read.csv("/Users/sciarbouche/Documents/Village_emploi/Mongodb/TP_mongodb/TP/Data/spotify_history.csv", header=True, inferSchema=True)

df.show()

#remplacer les valeurs manquentes par "Unkonown"
df = df.fillna({"reason_start": "unknown", "reason_end": "unknown"})

#conversion des types des données
df = df.withColumn("ts", col("ts").cast("timestamp")) \
       .withColumn("ms_played", col("ms_played").cast(IntegerType()))

#création des nouvelles colonnes

df = df.withColumn("minutes_played", col("ms_played") / 60000) \
       .withColumn("day_of_week", dayofweek(col("ts"))) \
       .withColumn("hour_of_day", hour(col("ts")))

#nettoyage des chaines de caractères
df = df.withColumn("artist_name", initcap(trim(col("artist_name")))) \
       .withColumn("track_name", initcap(trim(col("track_name")))) \
       .withColumn("album_name", initcap(trim(col("album_name"))))

#suppressions des doublons
df = df.dropDuplicates(["ts", "artist_name", "track_name"])

df = df.filter(col("ms_played") > 5000)

# Convertir le DataFrame PySpark en liste de dictionnaires
data_dict = [row.asDict() for row in df.collect()]

#connexion a mongodb

client = MongoClient("mongodb://localhost:27017/")
db = client.spotify_history_S
collection = db.history

collection.insert_many(data_dict)

print("les données sont bien nettoyer et insérer dans la base de donnée spotify_history avec succès")

spark.stop()
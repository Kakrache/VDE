import pandas as pd

df = pd.read_csv("Data/spotify_history.csv", sep = ",",encoding = "utf-8")

#Gestion des valeurs manquantes : Remplacer reason_start et reason_end manquants par "unknown".
df["reason_start"].fillna('unknown', inplace = True)
df["reason_end"].fillna("unknown", inplace= True)

#transformation de la colonne ts en format datetime et ms en Entier
df["ts"] = pd.to_datetime(df["ts"])
df["ms_played"] = df["ms_played"].astype(int)
print(df['ts'].dtype)
print(df["ms_played"].dtype)

#création des nouvelles colonnes
df["minutes_played"]= df["ms_played"] / 60000
df["day_of_week"] = df["ts"].dt.day_name()
df["hour_of_day"] = df["ts"].dt.hour

#supprimer les espaces inutiles pour les chaines de caractères
df["track_name"] = df["track_name"].str.strip().str.title() #nettoyage de base
df["track_name"] = df["track_name"].str.split().str.join(" ")  # Séparer les mots ensuite les recoller avec un espace
df["artist_name"] = df["artist_name"].str.strip().str.title()
df["artist_name"] = df["artist_name"].str.split().str.join(" ")
df["album_name"] = df["album_name"].str.strip().str.title()
df["album_name"] = df["album_name"].str.split().str.join(" ")

#supprimer les doublons pour les colonnes données
df.drop_duplicates( subset= ["ts", "artist_name", "track_name"], keep = "first", inplace= True)
print(len(df))

#filtrer la colonne ts(ts < 5000 a exxlure)
df= df[df["ms_played"] >= 5000]
df["ms_played"].min()  # afficher la val la plus petite pour verifier si il a a supprimer tous ce qui est > 5000

print(df.head())

df.to_csv("data/data_cleaned.csv", index= False)

print(len(df))
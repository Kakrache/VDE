import pandas as pd

df = pd.read_csv("Data/spotify_history.csv", sep = ",",encoding = "utf-8")

print(len(df))

print(df.head())

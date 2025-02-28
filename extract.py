import pandas as pd
df = pd.read_csv("Data/spotify_data_dictionary.csv", sep = ",",encoding = "utf-8")
print(len(df))
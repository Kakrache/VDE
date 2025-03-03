# VDE
crée un projet sur git
Le pipeline à mettre en place comprend 5 grandes étapes :
**Extraction des données depuis un fichier CSV :**
📌 Chargement du fichier CSV.
   Nous utilisons `pandas` pour lire le fichier CSV qui contient les données 'SpotifyHistory.csv.

  **Transformation et Nettoyage des Données avec pandas:**

📌 Appliquer les règles suivantes :
#Gestion des valeurs manquantes : Remplacer reason_start et reason_end manquants par "unknown".
#Conversion des types : Transformer ts en format datetime, ms_played en entier.

#Création de nouvelles colonnes

    minutes_played = ms_played / 60000
    day_of_week = Jour de la semaine (Monday, Tuesday, etc.)
    hour_of_day = Heure de la journée (ex : 13 pour 13h00)
#Nettoyage des chaînes de caractères : Supprimer espaces inutiles, mettre en format titre (title case).
#Suppression des doublons : Vérifier et éliminer les écoutes identiques (ts, artist_name, track_name).
#Filtrage : Exclure les écoutes de moins de 5 secondes (ms_played < 5000).

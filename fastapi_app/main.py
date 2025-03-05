from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["spotify_history"]
collection = db["listening_history"]

#  POST /history/ : Ajouter une écoute
@app.post("/history/")
def add_history(history: dict):
    result = collection.insert_one(history)
    return {"id": str(result.inserted_id)}

# gET /history/ : Lister toutes les écoutes (pagination)
@app.get("/history/")
def get_history(skip: int = 0, limit: int = 10):
    history = list(collection.find().skip(skip).limit(limit))
    return [{"id": str(item["_id"]), **item} for item in history]

# gET /history/{id} : Récupérer une écoute spécifique
@app.get("/history/{id}")
def get_history_by_id(id: str):
    history = collection.find_one({"_id": ObjectId(id)})
    if not history:
        raise HTTPException(status_code=404, detail="Écoute non trouvée")
    return {"id": str(history["_id"]), **history}

# PUT /history/{id} : Mettre à jour une écoute existante
@app.put("/history/{id}")
def update_history(id: str, updated_history: dict):
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_history})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Écoute non trouvée")
    return {"message": "Écoute mise à jour"}

# DELETE /history/{id} : Supprimer une écoute
@app.delete("/history/{id}")
def delete_history(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Écoute non trouvée")
    return {"message": "Écoute supprimée"}

# GET /top-artists/ : Liste des artistes les plus écoutés
@app.get("/top-artists/")
def top_artists(limit: int = 5):
    pipeline = [
        {"$group": {"_id": "$artist_name", "total_ms_played": {"$sum": "$ms_played"}}},
        {"$sort": {"total_ms_played": -1}},
        {"$limit": limit}
    ]
    results = list(collection.aggregate(pipeline))
    return [{"artist": r["_id"], "total_ms_played": r["total_ms_played"]} for r in results]

#  GET /skipped-ratio/ : Pourcentage de morceaux sautés
@app.get("/skipped-ratio/")
def skipped_ratio():
    total = collection.count_documents({})
    skipped = collection.count_documents({"skipped": True})
    return {"skipped_ratio": skipped / total * 100 if total > 0 else 0}

#  GET /listening-time-per-day/ : Temps total d’écoute par jour de la semaine
@app.get("/listening-time-per-day/")
def listening_time_per_day():
    pipeline = [
        {"$group": {"_id": "$day_of_week", "total_ms_played": {"$sum": "$ms_played"}}},
        {"$sort": {"total_ms_played": -1}}
    ]
    results = list(collection.aggregate(pipeline))
    return {r["_id"]: r["total_ms_played"] for r in results}

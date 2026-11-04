# J'importe pymongo, mes deux classes et random
import pymongo
from modèles import Personnage, Monstre
import random

# Je me connecte à MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Je choisis la base de données jeu
db = client["jeu"]


# Je crée une fonction qui récupère les personnages de la base sous forme d'objets
def get_personnages():
    # Je commence avec une liste vide
    liste = []
    # Je parcours chaque personnage de la collection
    for p in db["personnages"].find():
        # Je crée un objet Personnage avec les infos du dictionnaire
        perso = Personnage(p["nom"], p["classe"], p["degats"], p["def"], p["pv"])
        # J'ajoute l'objet à la liste
        liste.append(perso)
    # Je renvoie la liste
    return liste


# Je crée une fonction qui renvoie un monstre au hasard
def get_monstre():
    # Je mets tous les monstres de la collection dans une liste
    data = list(db["monstres"].find())
    # Je choisis un monstre au hasard dans la liste
    m = random.choice(data)
    # Je renvoie un objet Monstre créé avec ses infos
    return Monstre(m["nom"], m["degats"], m["def"], m["pv"], m["recompense"])


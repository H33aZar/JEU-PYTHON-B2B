# J'importe MongoClient pour pouvoir utiliser MongoDB avec Python
from pymongo import MongoClient

# Je me connecte au serveur MongoDB sur mon ordinateur
client = MongoClient("mongodb://localhost:27017/")

# Je choisis la base de données "jeu"
db = client["jeu"]

# Je crée une collection pour les personnages et une pour les monstres
personnages = db["personnages"]
monstres = db["monstres"]

# Je supprime tous les documents des collections pour éviter les doublons
personnages.delete_many({})
monstres.delete_many({})

# Liste de dictionnaires : chaque dictionnaire est un personnage (degats = dégâts infligés, def = défense, pv = points de vie)
liste_perso = [
    {"nom": "Guerrier", "degats": 100, "def": 50, "pv": 200},
    {"nom": "Mage", "degats": 50, "def": 20, "pv": 100},
    {"nom": "Voleur", "degats": 18, "def": 7, "pv": 90}
]

# Liste de dictionnaires : chaque dictionnaire est un monstre
liste_monstres = [
    {"nom": "Squelette", "degats": 10, "def": 5, "pv": 50},
    {"nom": "Troll", "degats": 20, "def": 8, "pv": 120}
]

# J'insère tous les dictionnaires dans leur collection
personnages.insert_many(liste_perso)
monstres.insert_many(liste_monstres)

# J'affiche un message quand c'est terminé
print("Base remplie")
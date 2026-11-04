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

# Liste de dictionnaires : chaque dictionnaire est un personnage
# (classe = son rôle, degats = dégâts infligés, def = défense, pv = points de vie)
liste_perso = [
    {"nom": "Guerrier", "classe": "Tank", "degats": 100, "def": 50, "pv": 200},
    {"nom": "Mage", "classe": "Magie", "degats": 50, "def": 20, "pv": 100},
    {"nom": "Voleur", "classe": "Assassin", "degats": 18, "def": 7, "pv": 90},
    {"nom": "Paladin", "classe": "Soutien", "degats": 40, "def": 40, "pv": 150},
    {"nom": "Archer", "classe": "Distance", "degats": 35, "def": 10, "pv": 80}
]

# Liste de dictionnaires : chaque dictionnaire est un monstre
# (recompense = or gagné quand on le bat)
liste_monstres = [
    {"nom": "Gobelin", "degats": 8, "def": 3, "pv": 40, "recompense": 5},
    {"nom": "Squelette", "degats": 10, "def": 5, "pv": 50, "recompense": 10},
    {"nom": "Orc", "degats": 15, "def": 8, "pv": 90, "recompense": 20},
    {"nom": "Troll", "degats": 20, "def": 8, "pv": 120, "recompense": 30},
    {"nom": "Dragon", "degats": 60, "def": 30, "pv": 300, "recompense": 100}
]

# Je met tous les dictionnaires dans leur collection
personnages.insert_many(liste_perso)
monstres.insert_many(liste_monstres)

# J'affiche un message quand c'est terminé
print("Base remplie")
# J'importe MongoClient pour parler à MongoDB
from pymongo import MongoClient

# Je me connecte à MongoDB sur mon ordinateur
client = MongoClient("mongodb://localhost:27017/")

# Je choisis la base de données jeu
db = client["jeu"]

# Je prends la collection des personnages et celle des monstres
personnages = db["personnages"]
monstres = db["monstres"]


# Cette fonction vide les deux collections pour ne pas avoir de doublons
def vider_collections():
    personnages.delete_many({})
    monstres.delete_many({})


# Cette fonction ajoute les personnages dans la base
def remplir_personnages():
    # Chaque dictionnaire est un personnage avec sa classe, ses degats, sa defense et ses pv
    liste_perso = [
        {"nom": "Guerrier", "classe": "Tank", "degats": 100, "def": 50, "pv": 200},
        {"nom": "Mage", "classe": "Magie", "degats": 50, "def": 20, "pv": 100},
        {"nom": "Voleur", "classe": "Assassin", "degats": 18, "def": 7, "pv": 90},
        {"nom": "Paladin", "classe": "Soutien", "degats": 40, "def": 40, "pv": 150},
        {"nom": "Archer", "classe": "Distance", "degats": 35, "def": 10, "pv": 80}
    ]
    # J'envoie tous les personnages dans la collection
    personnages.insert_many(liste_perso)


# Cette fonction ajoute les monstres dans la base
def remplir_monstres():
    # Chaque dictionnaire est un monstre avec la récompense en or qu'il donne quand on le bat
    liste_monstres = [
        {"nom": "Gobelin", "degats": 8, "def": 3, "pv": 40, "recompense": 5},
        {"nom": "Squelette", "degats": 10, "def": 5, "pv": 50, "recompense": 10},
        {"nom": "Orc", "degats": 15, "def": 8, "pv": 90, "recompense": 20},
        {"nom": "Troll", "degats": 20, "def": 8, "pv": 120, "recompense": 30},
        {"nom": "Dragon", "degats": 60, "def": 30, "pv": 300, "recompense": 100}
    ]
    # J'envoie tous les monstres dans la collection
    monstres.insert_many(liste_monstres)


# Fonction principale qui appelle les autres dans l'ordre
def main():
    vider_collections()
    remplir_personnages()
    remplir_monstres()
    # Je prévient que tout est fini
    print("Base remplie")


# Je lance le programme
main()
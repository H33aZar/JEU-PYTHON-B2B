# J'importe les fonctions dont j'ai besoin
from utils import get_personnages, get_monstre
from game import combat


# Je crée une fonction qui affiche le menu et renvoie le choix du joueur
def afficher_menu():
    print("1. Jouer")
    print("2. Quitter")
    return input("Choix: ")


# Je crée une fonction qui affiche les personnages avec leur numéro et leurs stats
def afficher_persos(persos):
    for i in range(len(persos)):
        p = persos[i]
        print(i, p.nom, "-", p.classe, "| degats:", p.degats, "| def:", p.defense, "| pv:", p.pv)


# Je crée une fonction qui laisse choisir 3 personnages et renvoie l'équipe
def choisir_equipe(persos):
    # Je commence avec une équipe vide
    equipe = []
    # Je répète 3 fois pour avoir 3 personnages
    for i in range(3):
        print("Choisis perso:")
        afficher_persos(persos)
        x = input()
        # Tant que le numéro n'existe pas, je redemande
        while not x.isdigit() or int(x) >= len(persos):
            print("Numéro invalide, recommence:")
            x = input()
        # Je transforme la réponse en nombre et j'ajoute le personnage à l'équipe
        equipe.append(persos[int(x)])
    return equipe


# Je crée une fonction qui enchaîne les combats jusqu'à la défaite
def jouer(equipe):
    # Je pars avec un score de 0 et 0 or
    score = 0
    gold = 0

    # Je boucle sans fin jusqu'à ce que le joueur perde
    while True:
        # Je prends un monstre au hasard et je lance le combat
        monstre = get_monstre()
        win = combat(equipe, monstre)

        # Si c'est gagné j'ajoute 1 au score et l'or du monstre
        if win:
            score += 1
            gold += monstre.recompense
            print("Score:", score, "| Or:", gold)
        # Si c'est perdu j'affiche le score final et je sors de la boucle
        else:
            print("Score final:", score, "| Or:", gold)
            break


# Je crée la fonction principale du programme
def main():
    # Je demande le choix au joueur
    choix = afficher_menu()

    # Si le joueur veut jouer je récupère les personnages, il choisit son équipe et la partie commence
    if choix == "1":
        persos = get_personnages()
        equipe = choisir_equipe(persos)
        jouer(equipe)
    # Sinon j'arrête le programme
    else:
        print("Fin")


# Je lance le programme
main()
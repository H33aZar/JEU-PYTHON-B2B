# J'importe random pour choisir une cible au hasard
import random

# Fonction qui gère un combat entre l'équipe et un monstre
def combat(equipe, monstre):
    # J'affiche le nom du monstre affronté
    print("Combat contre", monstre.nom)

    # Je boucle tant que le monstre a des pv
    while monstre.pv > 0:
        # Je parcours l'équipe, seuls les personnages vivants attaquent
        for p in equipe:
            if p.pv > 0:
                # Dégâts = degats du perso - defense du monstre, jamais en dessous de 0
                degats = p.degats - monstre.defense
                if degats < 0:
                    degats = 0
                # Je retire les dégâts aux pv du monstre et j'affiche l'attaque
                monstre.pv -= degats
                print(p.nom, "attaque", degats)

        # Si le monstre n'a plus de pv, je renvoie True (victoire)
        if monstre.pv <= 0:
            print("Ennemi vaincu")
            return True

        # Le monstre choisit un personnage au hasard comme cible
        cible = random.choice(equipe)
        # Dégâts = degats du monstre - defense de la cible, jamais en dessous de 0
        degats = monstre.degats - cible.defense
        if degats < 0:
            degats = 0

        # Je retire les dégâts aux pv de la cible et j'affiche l'attaque
        cible.pv -= degats
        print(monstre.nom, "attaque", cible.nom)

        # Je compte combien de personnages ont 0 pv ou moins
        morts = 0
        for p in equipe:
            if p.pv <= 0:
                morts += 1

        # Si tous les personnages sont morts, je renvoie False (défaite)
        if morts == len(equipe):
            print("YOU DIED")
            return False
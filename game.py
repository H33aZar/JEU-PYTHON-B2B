# J'importe random pour choisir une cible au hasard
import random


# Je crée une fonction qui calcule les dégâts
def calculer_degats(attaque, defense):
    # Je fais l'attaque moins la défense
    degats = attaque - defense
    # Si le résultat est négatif je mets 0
    if degats < 0:
        degats = 0
    return degats


# Je crée une fonction où l'équipe attaque le monstre
def equipe_attaque(equipe, monstre):
    # Je passe sur chaque personnage de l'équipe
    for p in equipe:
        # Seuls les personnages vivants attaquent
        if p.est_vivant():
            degats = calculer_degats(p.degats, monstre.defense)
            # Je retire les dégâts aux pv du monstre et j'affiche l'attaque
            monstre.pv -= degats
            print(p.nom, "attaque", degats)


# Je crée une fonction où le monstre attaque un personnage
def monstre_attaque(equipe, monstre):
    # Je prépare une liste vide pour les personnages vivants
    vivants = []
    # Je garde seulement les personnages encore en vie
    for p in equipe:
        if p.est_vivant():
            vivants.append(p)

    # Je choisis la cible au hasard parmi les vivants
    cible = random.choice(vivants)
    degats = calculer_degats(monstre.degats, cible.defense)
    # Je retire les dégâts aux pv de la cible et j'affiche l'attaque
    cible.pv -= degats
    print(monstre.nom, "attaque", cible.nom, "et fait", degats)


# Je crée une fonction qui renvoie True si toute l'équipe est morte
def equipe_morte(equipe):
    # Si je trouve un personnage vivant je renvoie False
    for p in equipe:
        if p.est_vivant():
            return False
    # Sinon personne n'est vivant donc je renvoie True
    return True


# Je crée la fonction qui gère tout le combat
def combat(equipe, monstre):
    # J'affiche le nom du monstre affronté
    print("Combat contre", monstre.nom)

    # Je continue tant que le monstre a des pv
    while monstre.pv > 0:
        # Je fais attaquer l'équipe
        equipe_attaque(equipe, monstre)

        # Si le monstre n'a plus de pv je renvoie True pour la victoire
        if monstre.pv <= 0:
            print("Ennemi vaincu")
            return True

        # Je fais attaquer le monstre
        monstre_attaque(equipe, monstre)

        # Si toute l'équipe est morte je renvoie False pour la défaite
        if equipe_morte(equipe):
            print("YOU DIED")
            return False

    # Si la boucle se termine, le monstre n'a plus de pv donc c'est une victoire
    return True

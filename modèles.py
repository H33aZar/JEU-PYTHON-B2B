# Je crée une classe Personnage
class Personnage:
    # Je crée le constructeur avec les caractéristiques du personnage
    def __init__(self, nom, classe, degats, defense, pv):
        # Je range chaque caractéristique dans l'objet
        self.nom = nom
        self.classe = classe
        self.degats = degats
        self.defense = defense
        self.pv = pv

    # Je crée une méthode qui renvoie True si le personnage a encore des pv
    def est_vivant(self):
        return self.pv > 0


# Je crée une classe Monstre
class Monstre:
    # Je crée le constructeur avec les caractéristiques du monstre
    def __init__(self, nom, degats, defense, pv, recompense):
        # Je range chaque caractéristique dans l'objet
        self.nom = nom
        self.degats = degats
        self.defense = defense
        self.pv = pv
        self.recompense = recompense
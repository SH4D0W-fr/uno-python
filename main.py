### IMPORT DES ELEMENTS ###
from cartes_bonus import cartes_bonus
from cartes import cartes
import random

### VERIF CHARGEMENT CARTES ###
print(str(len(cartes_bonus) + len(cartes))  + " cartes chargées.")
print(str(len(cartes)) + " cartes nombres")
print(str(len(cartes_bonus)) + " cartes actions")

### MELANGE CARTE ###
toutes_cartes = cartes + cartes_bonus
random.shuffle(toutes_cartes)

### GESTION JOUEUR ###
class Joueur:
    def __init__(self, nom:str):
        self.nom = nom
        self.main = []

    def ajouter_cartes(self, carte):
        self.main.append(carte)

    def voir_cartes(self):
        return self.main

### FONCTION AJOUT JOUEUR ###
def ajouter_joueur():
    noms_joueurs = []
    txt = ""
    while txt.lower() != "x":
        txt = input("Entrez le nom du joueur suivant (X quand vous avez terminé) : ")
        if txt.lower() != "x": noms_joueurs.append(txt)

    joueurs = [Joueur(nom) for nom in noms_joueurs]
    return joueurs

### FONCTION DISTRIBUTION CARTES ###
def distribuer_cartes(joueurs:list, paquet:list, nb_cartes:int):
    for joueur in joueurs:
        for _ in range(nb_cartes):
            joueur.ajouter_cartes(paquet.pop())

joueurs = ajouter_joueur()
distribuer_cartes(joueurs, toutes_cartes, 7)

for joueur in joueurs:
    print(f"{joueur.nom} : {joueur.voir_cartes()}")


### TESTS UNITAIRES ###
# if __name__ == "__main__":
    # joueur1 = Joueur("Timéo")
    # joueur2 = Joueur("Roger")

    # for i in range(7):
    #     joueur1.ajouter_cartes(toutes_cartes[0])
    #     toutes_cartes.pop(0)

    # for i in range(7):
    #         joueur2.ajouter_cartes(toutes_cartes[0])
    #         toutes_cartes.pop(0)
    # print(joueur1.voir_cartes())
    # print(joueur2.voir_cartes())
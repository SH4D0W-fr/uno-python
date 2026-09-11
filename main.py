### IMPORT DES ELEMENTS ###
from cartes_bonus import cartes_bonus
from cartes import cartes
from pioche import piocher
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

    def pioche(self, paquet, nombre):
        cartes, nouveau_paquet = piocher(paquet, nombre)
        for i in range(len(cartes)):
            self.ajouter_cartes(cartes[i])
        toutes_cartes = nouveau_paquet

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

### TESTS UNITAIRES ###
if __name__ == "__main__":
    joueurs = ajouter_joueur()
    distribuer_cartes(joueurs, toutes_cartes, 7)

    for joueur in joueurs:
        print(f"{joueur.nom} : {joueur.voir_cartes()}")

    ### TEST PIOCHE ###
    print("Cartes joueurs")
    joueurs[0].voir_cartes()
    print("Pioche")
    print(toutes_cartes)

    joueurs[0].pioche(toutes_cartes, 2)
    print("Après pioche 1 :")
    print("Cartes joueurs")
    print(joueurs[0].voir_cartes())
    print("Pioche")
    print(toutes_cartes)
    
    joueurs[0].pioche(toutes_cartes, 2)
    print("Après pioche 2 :")
    print("Cartes joueurs")
    print(joueurs[0].voir_cartes())
    print("Pioche")
    print(toutes_cartes)
    
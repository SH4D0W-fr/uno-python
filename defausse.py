import random

pile = []

# Fonction 1 : ajouter une carte dans la défausse
# Fonction 2 : Récupérer toutes les cartes de la défausse
# Fonction 3 : Récupérer la dernière carte posée

class Défausse:

    def pileDéfausse(self, carte):
        pile.append((0, "rouge", 0))    ### IMPLEMETNER LE VRAI SYSTEME


    def __init__(self):
        self.défausse = Défausse.pileDéfausse

    def mélangerDéfausse(self):
        return random.shuffle(self.défause)

    def getDéfausse(self):
        return self.défausse
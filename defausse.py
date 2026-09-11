import random

pile = []

class Défausse:

    def pileDéfausse(self, carte):
        pile.append((0, "rouge", 0))    ### IMPLEMETNER LE VRAI SYSTEME


    def __init__(self):
        self.défausse = Défausse.pileDéfausse

    def mélangerDéfausse(self):
        return random.shuffle(self.défause)

    def getDéfausse(self):
        return self.défausse
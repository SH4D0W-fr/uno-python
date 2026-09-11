import random


def piocher(pioche, defausse):
        #il faut que "pioche et défausse" soient des listes de cartes dcp?
    if len(pioche) == 0:
        #transfère :
        pioche.extend(defausse)
        #pour vider :
        defausse.clear()
        #et pour mélanger :
        random.shuffle(pioche)
    return pioche.pop()


def piocher_plusieurs(pioche, defausse, nombre):
    cartes = []
    for i in range(nombre):
        #dcp nombre de carte c un entier mais il vient de où?
        carte = piocher(pioche, defausse)
        cartes.append(carte)
    return cartes




#dcp il faut relier avec le jeu de cartes pour que ça fonctionne ?
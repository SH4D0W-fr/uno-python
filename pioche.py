#import defausse

def piocher(paquet:list, nombre:int):
    pioche = []
    if len(paquet) == 0:
        # ICI, on va transférer la defausse dans la pioche : pioche.extend(defausse)
        pass
    for i in range(nombre):
        pioche.append(paquet[0])
        paquet.pop(0)
    return pioche, paquet
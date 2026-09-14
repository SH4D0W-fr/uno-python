import random

pile = [(9, "vert", 1)]

# Fonction 1 : ajouter une carte dans la défausse              FAIT
# Fonction 2 : Récupérer toutes les cartes de la défausse      FAIT
# Fonction 3 : Récupérer la dernière carte posée               FAIT 

class Defausse:


    def __init__(self, pile, carte):
        self.defausse =  pile

    def ajouterDefausse(self, carte):                       ### ajouter une ou plusieurs cartes
        self.defausse = self.defausse + carte 
        return(self.defausse)   

    def melangerDéfausse(self):                             ### mélange de la défausse (on garde ?)
        return(random.shuffle(self.defausse))          

    def getDefausse(self):                                  ### obtenir la défausse en entier
        return self.defausse

    def getLastCard(self):                                  ### obtient la derni-re carte posé pour pouvoir continuer à jouer 
        return(self.defausse.pop())                         ### quand la pioche est vide


if __name__ == "__main__":

    carte = [(0, "vert", 1), (3, "jaune", 1)]
    poubelle = Defausse(pile, carte) 
    

    print(poubelle.ajouterDefausse(carte))
    print(poubelle.getDefausse())
    print(poubelle.getLastCard())
    print(poubelle.getDefausse())
    
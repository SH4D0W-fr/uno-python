import random

pile = [(9, "vert", 1)]

# Fonction 1 : ajouter une carte dans la défausse              FAIT
# Fonction 2 : Récupérer toutes les cartes de la défausse      FAIT
# Fonction 3 : Récupérer la dernière carte posée               FAIT 

class Défausse:


    def __init__(self, pile, carte):
        self.défausse =  pile

    def ajouterDéfausse(self, carte):                       ### ajouter une ou plusieurs cartes
        self.défausse = self.défausse + carte 
        return(self.défausse)   

    def mélangerDéfausse(self):                             ### mélange de la défausse (on garde ?)
        return(random.shuffle(self.défausse))          

    def getDéfausse(self):                                  ### obtenir la défausse en entier
        return self.défausse

    def getLastCard(self):                                  ### obtient la derni-re carte posé pour pouvoir continuer à jouer 
        return(self.défausse.pop())                         ### quand la pioche est vide


if __name__ == "__main__":

    carte = [(0, "vert", 1), (3, "jaune", 1)]
    poubelle = Défausse(pile, carte) 
    

    print(poubelle.ajouterDéfausse(carte))
    print(poubelle.getDéfausse())
    print(poubelle.getLastCard())
    print(poubelle.getDéfausse())
    
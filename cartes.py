class CarteNombre:

    def setCartes(self):
        cartes = [(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 0)]
        for i in range(9):
            for k in range(4):
                for id in range(2):
                    carte = (i+1, k, id+1)
                    cartes.append(carte)
        return(cartes)


    ## 0 = rouge
    ## 1 = jaune
    ## 2 = vert
    ## 3 = bleu

    def __init__(self, nombre, couleur, identifiant):
        self.cartes = self.setCartes()
        self.col = couleur #4 couleurs disponible (rouge,  bleu, jaune, vert)
        self.num = nombre #nombre de 0 à 9
        self.id = identifiant #identifiant de la carte de 1 à 2

    def getAttributs(self):
        return(self.num, self.col, self.id)

    def getCartes(self):
        return(self.cartes)



if __name__ == "__main__":
    c1 = CarteNombre("jaune", 4, 1)
    print(CarteNombre.getAttributs(c1))
    print(CarteNombre.setCartes())
    a = 0
    for i in CarteNombre.setCartes():
        a = a + 1
        print(a)

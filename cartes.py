class CartesNombre:

    def creerCartes(self):
        cartes = [(0, "rouge", 0), (0, "jaune", 0), (0, "vert", 0), (0, "bleu", 0)] # Création manuelle des cartes 0 de chaque couleur
        couleurs = ["rouge", "jaune", "vert", "bleu"]
        for i in range(9):
            for k in range(4):
                for num in range(2):
                    carte = (i+1, couleurs[k], num+1) # Format du tuple : (numéro:int, couleur:str, id:int)
                    cartes.append(carte)
        return(cartes)


    def __init__(self):
        self.cartes = self.creerCartes()

    def getCartes(self):
        return(self.cartes)


cartes = CartesNombre().getCartes() # Liste importée par main.py


if __name__ == "__main__":
    print(cartes)
    print(len(cartes))
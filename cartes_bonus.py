cartes_bonus = [] # Liste stockant toutes les cartes bonus

class CartesBonus:
    def creer_cartes_bonus(self, couleur:list, valeur:str, nombre:int, sansCouleur:bool):
        if not sansCouleur:
            for i in range(len(couleur)):
                for k in range(nombre):
                    id_carte = (valeur, couleur[i], str(k+1))
                    cartes_bonus.append(id_carte) # Exemple : "("inversion", "rouge", 1)", "("plus2", "vert", 2)"
        else:
            for k in range(nombre):
                id_carte = (valeur, str(k+1))
                cartes_bonus.append(id_carte) # Exemple : "("plus4", 1"), "("plus2", "vert", 2)"

    def __init__(self, valeur:str, nombre:int, sansCouleur:bool):
        """
        valeur:str : Valeur de la carte (plus2, inversion, plus4...)
        nombre:int : Nombre de carte par couleur
        sansCouleur:bool : Est-ce que la carte n'a pas de couleur ?
        """
        self.col = ["rouge", "bleu", "vert", "jaune"]
        self.val = valeur
        self.n = nombre
        self.wcol = sansCouleur
        # On créé un ID par carte
        self.creer_cartes_bonus(self.col, self.val, self.n, self.wcol)

### CREATION DES CARTES BONUS ###
plus2 = CartesBonus("plus2", 2, False)
inversion = CartesBonus("inversion", 2, False)
passer = CartesBonus("passer", 2, False)
joker = CartesBonus("joker", 4, True)
plus4 = CartesBonus("plus4", 4, True)

# Tests unitaires
if __name__ == "__main__":
    # plus2 = CartesBonus("plus2", 2, False)
    # plus4 = CartesBonus("plus4", 2, True)
    print(len(cartes_bonus))
    pass
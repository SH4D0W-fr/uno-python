### IMPORT DES ELEMENTS ###
from cartes_bonus import cartes_bonus
from cartes import cartes
from pioche import piocher
from defausse import Defausse
import random
import os
import time

try:
    import msvcrt          # Windows uniquement : permet de lire une touche sans Entree
except ImportError:
    msvcrt = None

### VERIF CHARGEMENT CARTES ###
print(str(len(cartes_bonus) + len(cartes))  + " cartes chargées.")
print(str(len(cartes)) + " cartes nombres")
print(str(len(cartes_bonus)) + " cartes actions")

### MELANGE CARTE ###
toutes_cartes = cartes + cartes_bonus
random.shuffle(toutes_cartes)

COULEURS = ["rouge", "jaune", "vert", "bleu"]

ROUGE = "\033[91m"
JAUNE = "\033[93m"
VERT = "\033[92m"
BLEU = "\033[94m"
NEUTRE = "\033[95m"
RESET = "\033[0m"
CODES_COULEUR = {"rouge": ROUGE, "jaune": JAUNE, "vert": VERT, "bleu": BLEU}
DELAI = 2

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


### OUTILS SUR LES CARTES ###
# Les tuples des cartes nombres et des cartes bonus colorées ont 3 valeurs : (valeur, couleur, id)
# Les tuples des jokers et des plus4 ont 2 valeurs : (valeur, id)

def est_sans_couleur(carte:tuple):
    """Renvoie True si la carte est un joker ou un plus4 (pas de couleur)."""
    return len(carte) == 2

def couleur_de(carte:tuple):
    """Couleur de la carte, ou une chaine vide pour un joker / plus4."""
    if est_sans_couleur(carte):
        return ""
    return carte[1]

def valeur_de(carte:tuple):
    """Valeur de la carte : un int (0-9) ou un str ('plus2', 'inversion'...)."""
    return carte[0]

def nom_carte(carte:tuple):
    """Version lisible d'une carte pour l'affichage."""
    if est_sans_couleur(carte):
        return f"{NEUTRE}{carte[0]}{RESET}"
    return f"{CODES_COULEUR[carte[1]]}{carte[0]} {carte[1]}{RESET}"

def est_jouable(carte:tuple, couleur_active:str, valeur_active):
    """Une carte est jouable si elle n'a pas de couleur, ou si elle correspond
    à la couleur active ou à la valeur de la carte du dessus."""
    if est_sans_couleur(carte):
        return True
    return couleur_de(carte) == couleur_active or valeur_de(carte) == valeur_active


### GESTION DE LA PIOCHE ET DE LA DEFAUSSE ###

def carte_du_dessus(defausse:Defausse):
    """Dernière carte posée"""
    return defausse.getDefausse()[-1]

def recharger_pioche(paquet:list, defausse:Defausse):
    """Quand la pioche est vide on remet la défausse dedans"""
    pile = defausse.getDefausse()
    if len(pile) <= 1:
        return False
    dessus = pile[-1]
    reste = pile[:-1]
    random.shuffle(reste)
    paquet.extend(reste)
    defausse.defausse = [dessus]   # à transformer en méthode viderDéfausse() plus tard
    print("(La défausse a été remélangée dans la pioche.)")
    pause()
    return True

def piocher_cartes(paquet:list, defausse:Defausse, nombre:int):
    """Pioche (nombre) cartes en rechargeant la pioche si besoin."""
    obtenues = []
    for _ in range(nombre):
        if len(paquet) == 0 and not recharger_pioche(paquet, defausse):
            break
        tirees, paquet = piocher(paquet, 1)
        obtenues.extend(tirees)
    return obtenues


### AFFICHAGE ET SAISIE ###

def effacer_ecran():
    """Efface les messages precedents pour ne garder que le tour en cours."""
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    """Laisse le temps de lire le dernier message avant la suite."""
    time.sleep(DELAI)

def attendre_touche():
    """Attend une touche avant de fermer le programme.
    Sans cela, la fenetre de l'executable se fermerait aussitot la partie finie."""
    print("\nAppuyez sur une touche pour quitter...")
    if msvcrt is None:                  # Linux / macOS : pas de msvcrt
        input()
        return
    while msvcrt.kbhit():               # on vide les touches tapees pendant la partie
        msvcrt.getch()
    msvcrt.getch()

def afficher_main(joueur:Joueur, couleur_active:str, valeur_active):
    print(f"\nMain de {joueur.nom} ({len(joueur.main)} cartes) :")
    for i, carte in enumerate(joueur.main):
        marque = "*" if est_jouable(carte, couleur_active, valeur_active) else " "
        print(f"  {marque} [{i}] {nom_carte(carte)}")
    print("  (* = carte jouable)")

def demander_entier(message:str, minimum:int, maximum:int):
    """Redemande tant que la saisie n'est pas un entier dans l'intervalle."""
    while True:
        reponse = input(message)
        try:
            valeur = int(reponse)
        except ValueError:
            print("Il faut entrer un nombre.")
            continue
        if minimum <= valeur <= maximum:
            return valeur
        print(f"Entrez un nombre entre {minimum} et {maximum}.")

def demander_couleur(joueur:Joueur):
    print(f"{joueur.nom}, choisissez une couleur :")
    for i, couleur in enumerate(COULEURS):
        print(f"  [{i}] {CODES_COULEUR[couleur]}{couleur}{RESET}")
    return COULEURS[demander_entier("Couleur : ", 0, len(COULEURS) - 1)]


### DEROULEMENT D'UN TOUR ###

def choisir_carte(joueur:Joueur, paquet:list, defausse:Defausse, couleur_active:str, valeur_active):
    """Fait jouer un joueur. Renvoie la carte posée, ou None s'il passe."""
    jouables = [i for i, c in enumerate(joueur.main)
                if est_jouable(c, couleur_active, valeur_active)]

    if len(jouables) == 0:
        print(f"{joueur.nom} n'a aucune carte jouable : il pioche.")
        pause()
        nouvelles = piocher_cartes(paquet, defausse, 1)
        if len(nouvelles) == 0:
            print("Plus aucune carte à piocher, le tour est passé.")
            pause()
            return None
        carte = nouvelles[0]
        joueur.ajouter_cartes(carte)
        print(f"{joueur.nom} pioche : {nom_carte(carte)}")
        if est_jouable(carte, couleur_active, valeur_active):
            if input("Voulez-vous la jouer ? (o/n) ").lower() == "o":
                return joueur.main.pop()
        pause()
        return None

    afficher_main(joueur, couleur_active, valeur_active)
    while True:
        indice = demander_entier("Numéro de la carte à jouer : ", 0, len(joueur.main) - 1)
        if indice in jouables:
            return joueur.main.pop(indice)
        print("Cette carte n'est pas jouable, choisissez-en une autre.")

def appliquer_effet(carte:tuple, joueurs:list, suivant:int, sens:int,
                    paquet:list, defausse:Defausse, poseur:Joueur):
    """Applique l'effet d'une carte action.
    Renvoie (couleur_active, sens, saute) où (saute)s indique si le joueur
    suivant perd son tour."""
    valeur = valeur_de(carte)
    couleur = couleur_de(carte)

    if valeur == "plus2":
        for c in piocher_cartes(paquet, defausse, 2):
            joueurs[suivant].ajouter_cartes(c)
        print(f"{joueurs[suivant].nom} pioche 2 cartes et passe son tour.")
        return couleur, sens, True

    if valeur == "plus4":
        nouvelle_couleur = demander_couleur(poseur)
        for c in piocher_cartes(paquet, defausse, 4):
            joueurs[suivant].ajouter_cartes(c)
        print(f"Couleur choisie : {CODES_COULEUR[nouvelle_couleur]}{nouvelle_couleur}{RESET}.")
        print(f"{joueurs[suivant].nom} pioche 4 cartes et passe son tour.")
        return nouvelle_couleur, sens, True

    if valeur == "joker":
        nouvelle_couleur = demander_couleur(poseur)
        print(f"Couleur choisie : {CODES_COULEUR[nouvelle_couleur]}{nouvelle_couleur}{RESET}.")
        return nouvelle_couleur, sens, False

    if valeur == "passer":
        print(f"{joueurs[suivant].nom} passe son tour.")
        return couleur, sens, True

    if valeur == "inversion":
        if len(joueurs) == 2:   # à 2 joueurs, l'inversion revient à passer le tour
            print("Inversion : à 2 joueurs, le tour est passé.")
            return couleur, sens, True
        print("Le sens de jeu est inversé.")
        return couleur, -sens, False

    return couleur, sens, False   # carte nombre -> aucun effet


### PARTIE COMPLETE ###

def jouer_partie():
    ### PREPARATION DU PAQUET ###
    # On travaille sur une copie pour pouvoir relancer une partie ensuite
    paquet = list(toutes_cartes)
    random.shuffle(paquet)

    ### JOUEURS ###
    joueurs = ajouter_joueur()
    if len(joueurs) < 2:
        print("Il faut au moins 2 joueurs pour jouer.")
        pause()
        return None
    distribuer_cartes(joueurs, paquet, 7)
    ### PREMIERE CARTE : on cherche une carte nombre pour démarrer simplement ###
    defausse = Defausse([], None)
    premiere = paquet.pop(0)
    while not isinstance(valeur_de(premiere), int):
        paquet.append(premiere)
        premiere = paquet.pop(0)
    defausse.ajouterDefausse([premiere])

    couleur_active = couleur_de(premiere)
    tour = 0        # index du joueur courant (on commence par le premier joueur ajouté)
    sens = 1        # 1 = sens horaire, -1 = sens inverse

    effacer_ecran()
    print("\n=== DEBUT DE LA PARTIE ===")
    pause()

    while True:
        effacer_ecran()
        dessus = carte_du_dessus(defausse)
        valeur_active = valeur_de(dessus)
        joueur = joueurs[tour]

        print("\n" + "-" * 40)
        print(f"Carte du dessus : {nom_carte(dessus)} | Couleur active : {CODES_COULEUR[couleur_active]}{couleur_active}{RESET}")
        print(f"Au tour de {joueur.nom}. Pioche : {len(paquet)} carte(s)")
        for autre in joueurs:
            if autre is not joueur:
                print(f"   {autre.nom} : {len(autre.main)} carte(s)")

        carte = choisir_carte(joueur, paquet, defausse, couleur_active, valeur_active)

        if carte is None:                       # le joueur n'a rien pu poser
            tour = (tour + sens) % len(joueurs)
            continue

        defausse.ajouterDefausse([carte])
        print(f"{joueur.nom} pose : {nom_carte(carte)}")
        pause()

        ### VICTOIRE ###
        if len(joueur.main) == 0:
            print(f"\n*** {joueur.nom} a gagné la partie ! ***")
            return joueur

        if len(joueur.main) == 1:
            print(f"!!! {joueur.nom} annonce UNO !!!") # flm de faire des contre uno
            pause()

        ### EFFET DE LA CARTE ###
        suivant = (tour + sens) % len(joueurs)
        couleur_active, sens, saute = appliquer_effet(
            carte, joueurs, suivant, sens, paquet, defausse, joueur)
        pause()

        ### JOUEUR SUIVANT ###
        tour = (tour + sens) % len(joueurs)
        if saute:
            tour = (tour + sens) % len(joueurs)


### LANCEMENT DU JEU ###
if __name__ == "__main__":
    jouer_partie()
    attendre_touche()

from joueur import Joueur
from deck import Deck
from Pile_File import Pile, File


class Jeu:
    """Classe représentant un jeu de cartes."""
    def __init__(self, nb_joueurs: int = 2):
        """Création d'un jeu de cartes."""
        self.deck = Deck()
        self.__tour = 0
        self.__liste_joueurs = []

        for i in range(nb_joueurs):
            self.__liste_joueurs.append(Joueur())

        self.__paquet = self.deck.partage()

        for i in range(len(self.__liste_joueurs)):
            self.__liste_joueurs[i].set_paquet(self.__paquet[i])

    def get_liste_joueurs(self):
        """Renvoie la liste des joueurs."""
        return self.__liste_joueurs

    def get_tour(self):
        """Renvoie le tour."""
        return self.__tour

    def set_tour(self, tour):
        """Modifie le tour."""
        self.__tour = tour

    def get_paquet(self):
        """Renvoie le paquet."""
        return self.__paquet

    def partie(self):
        """Déroulement d'une partie."""
        pass

    def __str__(self):
        """Affiche le jeu."""
        s = ""
        for joueur in self.get_liste_joueurs():
            s += str(joueur) + "\n"
        return s


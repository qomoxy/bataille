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

    def gagnant(self):
        """Renvoie le gagnant."""
        if self.get_liste_joueurs()[0].est_vide():
            return self.get_liste_joueurs()[1]
        else:
            return self.get_liste_joueurs()[0]

    def bataille(self, Joueur1, Joueur2, carte1, carte2):
        """Déroulement d'une bataille.
        :param Joueur1: le joueur 1
        :param Joueur2: le joueur 2
        :param carte1: la carte du joueur 1
        :param carte2: la carte du joueur 2
        """
        carte_cachee1 = Joueur1.get_paquet().defiler()
        carte_cachee2 = Joueur2.get_paquet().defiler()
        carte_dessus1 = Joueur1.get_paquet().defiler()
        carte_dessus2 = Joueur2.get_paquet().defiler()

        print("Bataille !")
        print("Carte dessus du joueur 1 :", carte_dessus1)
        print("Carte dessus du joueur 2 :", carte_dessus2)

        if carte_dessus1.get_point() > carte_dessus2.get_point():

            Joueur1.get_paquet().enfiler(carte1)
            Joueur1.get_paquet().enfiler(carte2)
            Joueur1.get_paquet().enfiler(carte_cachee1)
            Joueur1.get_paquet().enfiler(carte_cachee2)

        elif carte_dessus1.get_point() < carte_dessus2.get_point():

            Joueur2.get_paquet().enfiler(carte1)
            Joueur2.get_paquet().enfiler(carte2)
            Joueur2.get_paquet().enfiler(carte_cachee1)
            Joueur2.get_paquet().enfiler(carte_cachee2)

        else:

            self.bataille(Joueur1, Joueur2, carte1, carte2)

    def tour(self, Joueur1, Joueur2):
        """
        Déroulement d'une partie.
        :param Joueur1: le joueur 1
        :param Joueur2: le joueur 2
        """
        while not Joueur1.est_vide() and not Joueur2.est_vide():

            carte1 = Joueur1.get_paquet().defiler()
            carte2 = Joueur2.get_paquet().defiler()
            print("Tour", self.get_tour(), ":", carte1, "vs", carte2)

            if carte1.get_point() > carte2.get_point():

                Joueur1.get_paquet().enfiler(carte1)
                Joueur1.get_paquet().enfiler(carte2)
            elif carte1.get_point() < carte2.get_point():

                Joueur2.get_paquet().enfiler(carte1)
                Joueur2.get_paquet().enfiler(carte2)
            else:
                self.bataille(Joueur1, Joueur2, carte1, carte2)

    def partie(self):
        """Déroulement d'une partie."""
        while not self.get_liste_joueurs()[0].est_vide() and not self.get_liste_joueurs()[1].est_vide():
            self.tour(self.get_liste_joueurs()[0], self.get_liste_joueurs()[1])
            self.set_tour(self.get_tour() + 1)
        print("Le gagnant est", self.gagnant())

    def __str__(self):
        """Affiche le jeu."""
        s = ""
        for joueur in self.get_liste_joueurs():
            s += str(joueur) + "\n"
        return s

if __name__ == "__main__":
    jeu = Jeu()
    print(jeu)
    jeu.partie()

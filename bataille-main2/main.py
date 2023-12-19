from joueur import Joueur
from deck import Deck


class Jeu:
    """Classe représentant un jeu de cartes."""

    def __init__(self, nb_joueurs: int = 2):
        """Création d'un jeu de cartes."""
        self.deck = Deck()
        self.__tour = 0
        self.__liste_joueurs = []

        self.__paquet = self.deck.partage()

        for i in range(nb_joueurs):
            self.__liste_joueurs.append(Joueur(self.__paquet[i], i))

    def get_liste_joueurs(self):
        """Renvoie la liste des joueurs."""
        return self.__liste_joueurs

    def get_tour(self):
        """Renvoie le tour."""
        return self.__tour

    def get_paquet(self):
        """Renvoie le paquet."""
        return self.__paquet

    def set_tour(self, tour):
        """Modifie le tour."""
        self.__tour = tour

    def nb_cartes(self):
        """Renvoie le nombre de cartes."""
        n = 0
        for joueur in self.get_liste_joueurs():
            n = n + joueur.get_paquet().taille()
            print(f"Le nombre de cartes du joueur : {joueur.get_nom()} est : {self.__paquet[joueur.get_id()].taille()}")
        if n != 52:
            print(self.__paquet[0])
            print(self.__paquet[1])
            print(n)
            raise ValueError("Le nombre de cartes est incorrect !")
        print(n)

    def verification(self, Joueur1, Joueur2):
        """Vérifie si les joueurs ont le même nombre de cartes."""
        if Joueur1.get_paquet().est_vide() or Joueur2.get_paquet().est_vide():
            self.gagnant()
        else :
            carte_cache1 = Joueur1.get_paquet().defiler()
            carte_cache2 = Joueur2.get_paquet().defiler()

        if Joueur1.get_paquet().est_vide() or Joueur2.get_paquet().est_vide():
            self.gagnant()
        return carte_cache1, carte_cache2

    def gagnant(self):
        """Renvoie le gagnant."""
        if self.get_liste_joueurs()[0].get_paquet().est_vide():
            print(f" \n La gagnant est : {self.get_liste_joueurs()[1].get_nom()} au {self.__tour} tours.")
        else:
            print(f" \n La gagnant est : {self.get_liste_joueurs()[0].get_nom()} au {self.__tour} tours.")

    def bataille(self, Joueur1, Joueur2, carte1, carte2, cartes_en_jeu=None):
        """
        Déroulement d'une bataille.
        :param Joueur1: le joueur 1
        :param Joueur2: le joueur 2
        :param carte1: la carte du joueur 1
        :param carte2: la carte du joueur 2
        :param cartes_en_jeu: les cartes en jeu lors de la bataille
        """
        if cartes_en_jeu is None:
            cartes_en_jeu = []

        carte_cachee1, carte_cachee2 = self.verification(Joueur1, Joueur2)

        carte_dessus1 = Joueur1.get_paquet().defiler()
        carte_dessus2 = Joueur2.get_paquet().defiler()

        # Ajouter les cartes en jeu à la liste temporaire
        if not cartes_en_jeu:
            cartes_en_jeu.extend([carte1, carte2, carte_dessus1, carte_dessus2, carte_cachee1, carte_cachee2])
        else :
            cartes_en_jeu.extend([carte_dessus1, carte_dessus2, carte_cachee1, carte_cachee2])

        print("\n")
        print(f" ---- BATAILLE ---- ")
        print(carte_dessus1, "\n vs")
        print(carte_dessus2)

        if carte_dessus1.__gt__(carte_dessus2):
            print(carte_dessus1.get_point(), carte_dessus2.get_point())
            # Le joueur 1 gagne la bataille, ajouter toutes les cartes en jeu à son paquet
            for carte in cartes_en_jeu:
                Joueur1.get_paquet().enfile(carte)
            print(f"Le joueur {Joueur1.get_nom()} gagne cette bataille !")

        elif carte_dessus1.__lt__(carte_dessus2):
            print(carte_dessus1.get_point(), carte_dessus2.get_point())
            # Le joueur 2 gagne la bataille, ajouter toutes les cartes en jeu à son paquet
            for carte in cartes_en_jeu:
                Joueur2.get_paquet().enfile(carte)
            print(f"Le joueur {Joueur2.get_nom()} gagne cette bataille !")

        else:
            # Une autre bataille se produit, rappeler la méthode bataille avec la liste temporaire
            self.bataille(Joueur1, Joueur2, carte1, carte2, cartes_en_jeu)

    def tour(self, Joueur1, Joueur2):
        """
        Déroulement d'un tour.
        :param Joueur1: le joueur 1
        :param Joueur2: le joueur 2
        """

        carte1 = Joueur1.get_paquet().defiler()
        carte2 = Joueur2.get_paquet().defiler()

        print("\n")
        print(f" ---- TOUR : {self.__tour} ---- ")
        print(carte1, "\n vs")
        print(carte2)

        if carte1.__gt__(carte2):

            Joueur1.get_paquet().enfile(carte1)
            Joueur1.get_paquet().enfile(carte2)

            print(f"Le joueur {Joueur1.get_nom()} gagne ce tour !")

        elif carte1.__lt__(carte2):

            Joueur2.get_paquet().enfile(carte1)
            Joueur2.get_paquet().enfile(carte2)

            print(f"Le joueur {Joueur2.get_nom()} gagne ce tour !")

        else:

            self.bataille(Joueur1, Joueur2, carte1, carte2)

    def partie(self):
        """Déroulement d'une partie."""
        while not self.get_liste_joueurs()[0].get_paquet().est_vide() and not self.get_liste_joueurs()[1].get_paquet().est_vide():
            self.nb_cartes()
            self.tour(self.get_liste_joueurs()[0], self.get_liste_joueurs()[1])
            self.set_tour(self.get_tour() + 1)

        self.gagnant()

    def test(self):
        """Teste la création du jeu."""
        n = 0
        print("la")
        for i in self.__liste_joueurs[1].get_paquet():
            n += 1
            print(i)
        for i in self.__liste_joueurs[1].get_paquet():
            n += 1
            print(i)
        print(n)

    def __str__(self):
        """Affiche le jeu."""
        s = ""
        for joueur in self.get_liste_joueurs():
            s += str(joueur) + "\n"
        return s


if __name__ == "__main__":
    """Lance le jeu."""
    jeu = Jeu()
    jeu.partie()

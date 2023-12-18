class Joueur:
    """Classe Joueur"""
    def __init__(self, paquet):
        self.__nom = input("Entrez votre nom: ")
        self.__paquet = paquet

    def get_nom(self):
        """Renvoie le nom du joueur."""
        return self.__nom

    def get_paquet(self):
        """Renvoie le paquet du joueur."""
        return self.__paquet

    def set_paquet(self, paquet):
        """Modifie le paquet du joueur."""
        self.__paquet = paquet
        
    def paquet_vide(self):
        """Verifie si le paquet est vide."""
        return self.__paquet == []

    def ajouter_carte(self, carte):
        """Ajoute une carte au paquet du joueur."""
        self.__paquet.append(carte)

    def retirer_carte(self, carte):
        """Retire une carte du paquet du joueur."""
        self.__paquet.remove(carte)

    def est_vide(self):
        """Teste si le paquet du joueur est vide."""
        return len(self.__paquet) == 0

    def __str__(self):
        """Affiche le joueur."""
        return self.get_nom() + " : " + str(self.get_paquet())



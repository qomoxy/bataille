import random

class Carte:
    """Classe représentant une carte à jouer."""
    
    def __init__(self, points, symbol):
        """
        Création d'une carte à points et symbol.
        :param points: Le nombre de points de la carte
        :param symbol: le symbol de la carte
        """
        self.__point = points
        self.__symbol = symbol

    def get_point(self):
        """Renvoie le nombre de points de la carte."""
        return self.__point

    def get_symbol(self):
        """Renvoie le symbol de la carte."""
        return self.__symbol
        
    def __eq__(self, carte2):
        """Teste si la carte est égale à carte2."""
        return self.get_point() == carte2.point
    
    def __gt__(self, carte2):
        """Teste si la carte est strictement supérieure à carte2."""
        return self.get_point() > carte2.point
    
    def __lt__(self, carte2):
        """Teste si la carte est strictement inférieure à carte2."""
        return self.get_point() < carte2.point
            
    def __str__(self):
        """Affiche la carte."""
        return f"La carte à points : {self.get_point()} et pour symbol : {self.get_symbol()}"

class Deck:
    """Classe représentant un deck de cartes."""
    
    def __init__(self):
        """Création d'un deck de cartes."""
        self.__nb_cartes = 15
        self.__tete = ["Valet", "Dame", "Roi", "As"]
        self.__symbol = ["♦", "♥", "♠", "♣"]
        self.__deck = []
        self.creation_deck()

    def get_nb_cartes(self):
        """Renvoie le nombre de cartes du deck."""
        return self.__nb_cartes

    def get_tete(self):
        """Renvoie la tête du deck."""
        return self.__tete

    def get_symbol(self):
        """Renvoie le symbol du deck."""
        return self.__symbol

    def get_deck(self):
        """Renvoie le deck."""
        return self.__deck
        
    def creation_deck(self):
        """Création d'un deck de cartes."""
        for symbol in self.get_symbol():
            for point in range(2, self.get_nb_cartes()):
                self.__deck.append(Carte(point, symbol))
        random.shuffle(self.__deck)

    def tirer(self):
        """Tire une carte au hasard dans le deck."""
        """Retire la carte en sommet de pile."""
        return self.__deck.pop()

    def ajouter(self, carte):
        """Ajoute la carte en sommet de pile."""
        self.__deck.append(carte)

    def est_vide(self):
        """Teste si la pile est vide."""
        return len(self.get_deck()) == 0

    def melanger(self):
        """Mélange la pile."""
        random.shuffle(self.__deck)

    def trier(self):
        """Trie la pile."""
        self.__deck.sort()

    def tete(self, carte):
        """Regarde la tête de la carte."""
        match carte:
            case 11:
                return self.get_tete()[0]
            case 12:
                return self.get_tete()[1]
            case 13:
                return self.get_tete()[2]
            case 14:
                return self.get_tete()[3]
            case _:
                return carte.get_point()
        
    def partage(self):
        """Partage le deck en deux paquets."""
        paquet1= []
        paquet2 = []
        
        for i in range(len(self.__deck)):
            if i % 2 == 0:
                paquet1.append(self.__deck[i])
            else:
                paquet2.append(self.__deck[i])
        return paquet1, paquet2
            
            
                
    def __str__(self):
        """Affiche le deck."""
        res = ""
        for carte in self.get_deck():
            res += "\n" + str(carte)
        return res
                
deck = Deck()


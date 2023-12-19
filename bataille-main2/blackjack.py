class Blackjack:
    def __init__(self):
        self.score = 21
        self.deck = Deck()
        self.__tour = 0
        self.__liste_joueurs = []

        for i in range(nb_joueurs):
            self.__liste_joueurs.append(Joueur([], i))
        
        self.main = []
        self.main2 = []
        
        self.mise1 = 0
        self.mise2 = 0
        self.debut()
    
    def debut(self):
        print("Bienvenue à notre table !")
        reponse = input("Connaisais vous les regle du black Jack ?")
        if reponse == "oui":
            pass
        else :
            print("La partie oppose individuellement chaque joueur à la banque. Le but est de battre le croupier sans dépasser le score de 21. Dès qu'un joueur fait plus que 21, on dit qu'il « brûle » et il perd sa mise initiale. Les valeurs des cartes sont les suivantes.")
        pass
    
    
        
        
        
from Pile_File import *
import random

class Carte:
    
    def __init__(self, points, symbol):
        self.point = points
        self.symbol = symbol
        
    def __eq__(self, carte2):
        return self.point == carte2.point
    
    def __gt__(self, carte2):
        return self.point > carte2.point
    
    def __lt__(self, carte2):
        return self.point < carte2.point
            
    def __str__(self):
        return f"La carte à points : {self.point} et pour symbol : {self.symbol}"

class Deck:
    
    def __init__(self):
        self.nb_cartes = 15
        self.tete = ["Valet", "Dame", "Roi", "As"]
        self.symbol = ["♦", "♥", "♠", "♣"]
        self.deck = []
        self.creation_deck()
        
    def creation_deck(self):
        for symbol in self.symbol:
            for point in range(2, self.nb_cartes): 
                self.deck.append(Carte(point, symbol))
        random.shuffle(self.deck)
        
    def partage(self, nb = 2):
        paquet1 = []
        paquet2 = []
        
        for i in range(len(self.deck) // 2):
            paquet1.append(self.deck[i])
        for i in range(len(self.deck) // 2):
            paquet2.append(self.deck[i])
        return paquet1, paquet2
                
    def __str__(self):
        res = ""
        for carte in self.deck:
            res += "\n" + str(carte)
        return res
                
deck = Deck()

            
    
        
        
                
            
            
            
        

        
    

        
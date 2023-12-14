class File:
    
    def __init__(self):
        self.file = []
        
    def est_vide(self):
        return len(self.file) <= 0
        
    def defiller(self):
        if self.est_vide(self.file):
            raise IndexError("La file est vide !")
        return self.file.pop()
    
    def enfile(self,value):
        self.file = [value] + self.file
        
    def vider(self):
        self.file = []
        
    def __str__(self):
        s = 'Sortie'
        for i in range(len(self.file)):
            s = str(self.file[i]) + ' -> ' + s
        s = 'Entrée -> ' + s
        return s
    
class Cellule:
    
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
    
class Pile:
    
    def __init__(self):
        self.contenu = None
        
    def est_vide(self):
        return self.contenu is None
    
    def empile(self, v):
        c = Cellule(v, self.contenu)
        self.contenu = c
    
    def defiller(self):
        if self.est_vide():
            raise IndexError("La pile est vide !")
        tmp = self.contenu = self.contenu.suivante
        self.contenu = self.contenu.suivant
        return v
    
    def __str__(self):
        s = ''
        for i in range(len(self.pile)):
            s = str(self.pile[i]) + "\n" + s
        return s
        
    
        
        
        
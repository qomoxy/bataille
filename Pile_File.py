class File:
    """Classe représentant une file FIFO."""
    
    def __init__(self):
        """Création d'une file vide."""
        self.__file = []

    def get_file(self):
        """Renvoie le contenu de la file."""
        return self.__file
        
    def est_vide(self):
        """Teste si la file est vide."""
        return len(self.__file) <= 0
        
    def defiller(self):
        """Retire l'élément en sortie de file."""
        if self.est_vide():
            raise IndexError("La file est vide !")
        return self.__file.pop()
    
    def enfile(self, value):
        """
        Ajoute l'élément value à file.
        :param value: L'élément à ajouter
        """
        self.__file = [value] + self.__file
        
    def vider(self):
        """Vide la file."""
        self.__file = []
        
    def __str__(self):
        """Affiche la file."""
        s = 'Sortie'
        for i in range(len(self.get_file())):
            s = str(self.__file[i]) + ' -> ' + s
        s = 'Entrée -> ' + s
        return s
    
class Cellule:
    """Classe représentant une cellule d'une pile."""
    
    def __init__(self, v, s):
        """
        Création d'une cellule contenant la valeur v et pointant sur la cellule.
        :param v: la valeur de la cellule
        :param s: la cellule suivante
        """
        self.__valeur = v
        self.__suivante = s

    def get_valeur(self):
        """Renvoie la valeur de la cellule."""
        return self.__valeur

    def get_suivante(self):
        """Renvoie la cellule suivante."""
        return self.__suivante
    
class Pile:
    """Classe représentant une pile LIFO."""
    
    def __init__(self):
        """Création d'une pile vide."""
        self.contenu = None
        
    def est_vide(self):
        """Teste si la pile est vide."""
        return self.contenu is None
    
    def empile(self, v):
        """
        Ajoute la valeur v en sommet de pile.
        :param v: la valeur à ajouter
        """
        c = Cellule(v, self.contenu)
        self.contenu = c
    
    def defiller(self):
        """Retire l'élément en sommet de pile."""
        if self.est_vide():
            raise IndexError("La pile est vide !")
        tmp = self.contenu = self.contenu.suivante
        self.contenu = self.contenu.suivant
        return tmp
    
    def __str__(self):
        """Affiche la pile."""
        s = ''
        for i in range(len(self.contenu)):
            s = str(self.contenu[i]) + "\n" + s
        return s

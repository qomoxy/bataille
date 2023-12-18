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
        
    def defiler(self):
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

    def taille(self):
        """Renvoie la taille de la file."""
        return len(self.__file)
        
    def __str__(self):
        """Affiche la file."""
        s = 'Sortie'
        for i in range(len(self.get_file())):
            s = str(self.__file[i]) + ' -> ' + s
        s = 'Entrée -> ' + s
        return s

    
class Pile:
    """Classe représentant une pile LIFO."""
    
    def __init__(self):
        """Création d'une pile vide."""
        self.contenu = []
        
    def pile_vide(self):
        """Return une pile vide"""
        return []
        
    def est_vide(self):
        """Teste si la pile est vide."""
        return len(self.contenu) == 0
    
    def empile(self, v):
        """
        Ajoute la valeur v en sommet de pile.
        :param v: la valeur à ajouter
        """
        self.contenu.append(v)
    
    def depile(self):
        """Retire l'élément en sommet de pile."""
        if self.est_vide():
            raise IndexError("La pile est vide !")
        return self.contenu.pop()

    def taille(self):
        """Renvoie la taille de la pile."""
        return len(self.contenu)
    
    def __str__(self):
        """Affiche la pile."""
        s = ''
        for i in range(len(self.contenu)):
            s = str(self.contenu[i]) + "\n" + s
        return s

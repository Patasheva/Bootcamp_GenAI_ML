class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)  # Convertir en entier si c'est un float
        self.totalPages = max(1, -(-len(self.items) // self.pageSize))  # Nombre total de pages (arrondi au supérieur)
        self.currentPage = 1  # La numérotation commence à 1

    def getVisibleItems(self):
        """Retourne les éléments visibles de la page actuelle"""
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        """Passe à la page précédente si possible"""
        self.currentPage = max(1, self.currentPage - 1)
        return self  # Permet le chaînage

    def nextPage(self):
        """Passe à la page suivante si possible"""
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        """Va à la première page"""
        self.currentPage = 1
        return self

    def lastPage(self):
        """Va à la dernière page"""
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        """Va à une page spécifique, tout en respectant les limites"""
        pageNum = int(pageNum)  # Convertir en entier si c'est un float
        self.currentPage = max(1, min(self.totalPages, pageNum))
        return self


# Exemple d'utilisation
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ["a", "b", "c", "d"]
p.nextPage()
print(p.getVisibleItems())  # ["e", "f", "g", "h"]
p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]
p.firstPage().nextPage().nextPage()
print(p.getVisibleItems())  # ["i", "j", "k", "l"]
p.goToPage(10)
print(p.getVisibleItems())  # ["y", "z"] (dernière page car il y a 7 pages max)
p.goToPage(-1)
print(p.getVisibleItems())  # ["a", "b", "c", "d"] (revient à la première page)
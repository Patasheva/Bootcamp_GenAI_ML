class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)  
        self.totalPages = max(1, -(-len(self.items) // self.pageSize)) 
        self.currentPage = 1 
        
# Retourne les éléments visibles de la page actuelle
    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

# Passe à la page suivante 
    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum) 
        self.currentPage = max(1, min(self.totalPages, pageNum))
        return self

# Tests
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
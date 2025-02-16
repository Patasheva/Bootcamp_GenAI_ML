import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add another Circle instance.")
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

c1 = Circle(radius=5)
c2 = Circle(radius=8)

print(c1)  
print(c2)  

c3 = c1 + c2
print(c3) 

print(c1 < c2)  
print(c1 == c2) 

circles = [c1, c2, c3]
circles.sort()
print([str(c) for c in circles]) 
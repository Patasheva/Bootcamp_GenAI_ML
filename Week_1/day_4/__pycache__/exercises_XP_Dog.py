# Exercise 1  Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Luna", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Exetcise 2 Dogs
class Dog:
   def __init__(self, name, age, weight):
       self.name = name
       self.age = age
       self.weight=weight

   def bark(self):
       return f"{self.name} is barking"

   def run_speed(self):
       return self.weight/self.age*10
   
   def fight(self, other_dog):
       self_score = self.run_speed() * self.weight
       other_score = other_dog.run_speed() * other_dog.weight
       
       if self_score > other_score:
          return f"{self.name} wins the fight against {other_dog.name}!"
       elif self_score < other_score:
          return f"{other_dog.name} wins the fight against {self.name}!"
       else:
          return "It's a tie!"
           
dog_1 = Dog("Mylo", 2, 15)
dog_2 = Dog("Mikki", 4, 23)
dog_3 = Dog("Richi", 3, 13)

dog_1.bark() 
print(f"{dog_1.name}'s speed: {dog_1.run_speed()}")

dog_2.bark() 
print(f"{dog_2.name}'s speed: {dog_2.run_speed()}")

dog_3.bark() 
print(f"{dog_3.name}'s speed: {dog_3.run_speed()}")

print(dog_1.fight(dog_2))
print(dog_2.fight(dog_3)) 
print(dog_3.fight(dog_1))
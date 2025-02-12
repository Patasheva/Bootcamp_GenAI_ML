# # "hello".upper()

# "hello" est un objet de la classe STR
# cette classe str contient des fonctions
# comme la fonction upper
# une fonction dans une classe est appelee "methode"

class Personnage :
    # fonction __init__ permet d'initialiser les attributs
    def __init__(self, name_personnage, power_personnage):
        # definir les attributs
        self.energy = 100
        self.name = name_personnage
        self.power_type = power_personnage
        self.animals = []

    def talk_with_animals(self, animal):
        self.animals.append(animal)

    def display_animals(self) :
        # for animal in self.animals :
        #     print(f"{self.name} parle avec un {animal}")
        print(f"{self.name} parle avec un {", ".join(self.animals)}")

    # battre 
    # ogre : => 30pt energy
    # magicien => 50pt
    # autre => 10pt
    def fight(self, type_personnage): 
        if type_personnage == "ogre":
            self.energy -= 30
        elif type_personnage == "magicien":
            self.energy -= 50
        else :
            self.energy -= 10

harry_potter = Personnage("Harry", "voler")

print(f"my personnage s'appelle {harry_potter.name} il a {harry_potter.energy} points d'energy")
print(f"my personnage s'appelle {harry_potter.name} il peut {harry_potter.power_type}")

harry_potter.talk_with_animals("loup")
harry_potter.talk_with_animals("chouette")
harry_potter.talk_with_animals("lapin")
harry_potter.display_animals()
print(f"my personnage s'appelle {harry_potter.name} il a {harry_potter.energy} points d'energy")

new_personnage_1 = Personnage("John", "disparaitre")
new_personnage_1.talk_with_animals("serpent")
new_personnage_1.display_animals()
new_personnage_1.energy = 1000
print(f"my personnage s'appelle {new_personnage_1.name} il a {new_personnage_1.energy} points d'energy")

new_personnage_1.fight("magicien")
print(f"my personnage s'appelle {new_personnage_1.name} il a {new_personnage_1.energy} points d'energy")

# Rajout sur la classe personnage
class PersonnageMore :
    # fonction __init__ permet d'initialiser les attributs
    def __init__(self, name_personnage, power_personnage, type_personnage):
        # definir les attributs
        self.energy = 100
        self.name = name_personnage
        self.power_type = power_personnage
        self.type = type_personnage
        self.animals = []

    def talk_with_animals(self, animal):
        self.animals.append(animal)

    def display_animals(self) :
        # for animal in self.animals :
        #     print(f"{self.name} parle avec un {animal}")
        print(f"{self.name} parle avec un {", ".join(self.animals)}")

    def fight(self, other_personnage, type_battle): 
        print(f"{self.name} se bat avec {other_personnage.name}")
        if other_personnage.type == "ogre":
            self.energy -= 30
        elif other_personnage.type == "magicien":
            self.energy -= 50
            other_personnage.energy -= 50
            if type_battle == "poing" :
                self.energy -= 5
        else :
            self.energy -= 10

harry_potter = PersonnageMore("Harry", "voler", "magicien")
voldemort = PersonnageMore("Voldemort", "super pouvoir", "magicien")


print(f"my personnage s'appelle {harry_potter.name} il a {harry_potter.energy} points d'energy")
print(f"my personnage s'appelle {voldemort.name} il a {voldemort.energy} points d'energy")


harry_potter.fight(voldemort, "poing")
print(f"my personnage s'appelle {harry_potter.name} il a {harry_potter.energy} points d'energy")
print(f"my personnage s'appelle {voldemort.name} il a {voldemort.energy} points d'energy")

# INHERITANCE

class Dog:
    def __init__(self, dog_name):
        self.energy = 100
        self.name = dog_name

    def bark (self) :
        print("Ouaf Ouaf")

    def play (self) :
        print("the dog is playing")
        self.energy -= 10

dog_1 = Dog("Rex")

# class GuideDog => herite de a class Dog mais avec un truc en plus
# sous classe de la classe Dog

class GuideDog(Dog):
    def __init__(self, dog_name, age):
        super().__init__(dog_name) # j'appelle le init de la classe mere
        # ces 2 attributs sont uniquement accessible pour un guide
        self.job = True
        self.guide_dog_age = age
    
    def guide_master(self) :
        print("je guide mon maitre")
    

dog_2 = GuideDog("Minnie", 2)
print(dog_2.energy)
dog_2.bark()
print(dog_2.job) # le chien guide a un job
print(dog_2.guide_dog_age) # le chien guide a un age

# print(dog_1.job) # erreur # le chien normal n'a pas de job

dog_2.guide_master() # le chien guide peut appeler cette fonction car c'est un chien guide
# dog_1.guide_master() # erreur
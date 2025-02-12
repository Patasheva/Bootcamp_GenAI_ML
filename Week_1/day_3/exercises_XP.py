# Exercise 1 Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat("Mylo", 2)
cat_2 = Cat("Mika", 4)
cat_3 = Cat("Lisha", 8)

def find_oldest_cat(*cats):  
    return max(cats, key=lambda cat: cat.age)  

oldest_cat = find_oldest_cat(cat_1, cat_2, cat_3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# Exercise 2 Dogs
class Dog: 
   def __init__(self, name, height):
      self.name = name  
      self.height = height
 
   def bark(self):
       print(f"{self.name} goes woof!")

   def jump(self):
       print(f"{self.name} jumps {self.height*2} cm high!")
    
   def show_info(self):  
       print(f"Dog's name is {self.name} and he is {self.height} cm.")

davids_dog = Dog("Rex", 50) 
davids_dog.show_info()
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20) 
sarahs_dog.show_info()
sarahs_dog.bark()
sarahs_dog.jump()

def find_biggest_dog(*dogs):
    return max(dogs, key=lambda dog: dog.height)

biggest_dog = find_biggest_dog(davids_dog, sarahs_dog)
print(f"The biggest dog is {biggest_dog.name}, and is {biggest_dog.height} cm.")

# Exercise 3 Who’s The Song Producer?
class Song:
     def __init__(self, lyrics):
          self.lyrics = lyrics 
     
     def sing_me_a_song(self):  
         for line in self.lyrics:  
            print(line) 
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 Afternoon At The Zoo
class Zoo:
   def __init__(self, zoo_name):
       self.name = zoo_name
       self.animals = []
   
   def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            pass

   def get_animals(self):
        print(f"Zoo {self.name} animals are: {', '.join(self.animals)}")

   def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            pass 
   def sort_animals(self):
        sorted_animals = sorted(self.animals)  
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper() 
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        return grouped_animals

   def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Emu")


ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Giraffe")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
    

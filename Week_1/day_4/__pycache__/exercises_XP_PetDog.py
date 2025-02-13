# Exercise 3 Dogs Domesticated
from exercises_XP_Dog import Dog 
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
       super().__init__(name, age, weight)
       self.trained = False
      
    def train(self):
         print(self.bark)
         self.trained = True
    
    def play(self, *other_dogs):
        all_dogs = ', '.join([dog.name for dog in other_dogs])
        print(f"{self.name}, {all_dogs} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))  # Choisit un tour au hasard
        else:
            print(f"{self.name} is not trained yet!")

dog_1 = PetDog("Mylo", 2, 15)
dog_2 = PetDog("Mikki", 4, 23)
dog_3 = PetDog("Richi", 3, 13)

print(dog_1.bark()) 

dog_1.train()  
dog_1.do_a_trick()  
dog_2.do_a_trick()  
dog_1.play(dog_2, dog_3)


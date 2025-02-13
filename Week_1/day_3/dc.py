class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name  
        self.animals = {}
        # self.all_animals = []

    def add_animal(self, animal_name, animal_number =1):
        if animal_name in self.animals:
           self.animals[animal_name] += animal_number 
        else:
            self.animals[animal_name] = animal_number
        # self.all_animals.append(animal_name) #ajout dans la liste

    def get_info(self):
        message =f"{self.farm_name}'s farm\n"
        for animal, quantity in self.animals.items():
            message += f"{animal} : {quantity}\n"
        message += "\n    E-I-E-I-0!"
        return message
    
    def get_animals_types(self):
        # return sorted(self.all_animals)
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        all_animals_sorted = self.get_animal_types()
        list_animals = []
        for animal in all_animals_sorted :
            if self.animals[animal] > 1 :
                list_animals.append(f"{animal}s")
            else :
                list_animals.append(f"{animal}")
            # ["cows", "sheeps", "rabbits"]
            message = f"{self.name} Farm has {", ".join(list_animals[:-1])} and {list_animals[-1]}"
        return message

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animals_types())
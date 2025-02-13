# Exercise 4 Family
class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations à la famille {self.last_name} pour la naissance de {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return None 

    def family_presentation(self):
        print(f"Famille {self.last_name} :")
        for member in self.members:
            print(f"  - {member['name']}, {member['age']} ans, {member['gender']} {'(enfant)' if member['is_child'] else '(adulte)'}")

my_family = Family("PATASHEVA", [
    {'name': 'Beso', 'age': 42, 'gender': 'Male', 'is_child': False},
    {'name': 'Olga', 'age': 38, 'gender': 'Female', 'is_child': False}
])

my_family.family_presentation()

my_family.born(name="Alexandra", age=0, gender="Female", is_child=True)

print(f"Is Beso an adult? {my_family.is_18('Michael')}")
print(f"Is Alexandra est majeure ? {my_family.is_18('Emma')}")

my_family.family_presentation()

# Exercises 5 TheIncredibles Family 
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] < 18:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power.")
                print(f"{member['incredible_name']} uses their power: {member['power']}")
                return

    def incredible_presentation(self):
        print("\n Here is our powerful family ")
        super().family_presentation()

# Création de la famille des Indestructibles
incredibles_family = TheIncredibles("Incredibles", [
    {'name': 'Beso', 'age': 42, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Olga', 'age': 38, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

incredibles_family.incredible_presentation()

incredibles_family.born(name="Baby Mylo", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="Mylik")

incredibles_family.incredible_presentation()

incredibles_family.use_power("Beso")  
incredibles_family.use_power("Olga")    

try:
    incredibles_family.use_power("Baby Mylo")
except Exception as e:
    print(f"{e}")
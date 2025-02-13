# import Employee 
from employee import Employee 

class Developer(Employee):
    def __init__(self, firstname, lastname, age, job="Developer", salary=15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []  
    
    def add_skills(self, *skills):
        self.coding_skills.extend(skills)
        print(f"{self.firstname} learned: {', '.join(skills)}")
     
    def coding(self):
        if self.coding_skills:
            print(f"{self.firstname} knows: {', '.join(self.coding_skills)}")
        else:
            print(f"{self.firstname} doesn't know any coding languages yet.")

    def coding_with_partner(self, other_developer):
        print(f"{self.firstname} and {other_developer.firstname} know: "
              f"{', '.join(self.coding_skills)} and {', '.join(other_developer.coding_skills)}")

def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount
        print(f"{self.firstname} {self.lastname} got a developer promotion! New salary: {self.salary}")

def get_promotion(self, amount):
        self.salary *= amount

dev1 = Developer("Tom", "Cruiz", 30)
dev2 = Developer("Angelina", "Jolie", 23)
print(dev1.firstname)

dev1.add_skills("Python", "Java")
dev2.add_skills("JavaScript", "C++")
print(dev1.add_skills)

dev1.coding()
dev2.coding()
dev1.coding_with_partner(dev2)
dev1.get_promotion(1.2)  
dev2.get_promotion(1.5) 
dev1.show_info()
dev2.show_info()
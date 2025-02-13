class Employee :
   def __init__(self, firstname, lastname, age, job, salary):
       self.firstname = firstname
       self.lastname = lastname
       self.age = age
       self.job = job
       self.salary = salary

   def get_fullname(self):
        return self.firstname  + self.lastname

   def happy_birthday(self):
        self.age += 1
        return self.age

   def get_promotion(self, amount):
        self.salary += amount

   def show_info(self):
        print(f"Name: {self.get_fullname()}")
        print(f"Age: {self.age} years old")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary} euros")

# Creating two employee objects
employee_1 = Employee("Lea", "Smith", 30, "Developer", 25000)
employee_2 = Employee("David", "Schartz", 20, "Project Manager", 20000)

# Displaying their attributes using the methods
print("Employee 1:")
employee_1.show_info()
print("\nCalling all methods for Lea:")
print(f"Full Name: {employee_1.get_fullname()}")
print(f"Happy Birthday! New Age: {employee_1.happy_birthday()}")
print(f"Promotion Applied! New Salary: {employee_1.get_promotion(5000)}")
employee_1.show_info()

print("\nEmployee 2:")
employee_2.show_info()
print("\nCalling all methods for David:")
print(f"Full Name: {employee_2.get_fullname()}")
print(f"Happy Birthday! New Age: {employee_2.happy_birthday()}")
print(f"Promotion Applied! New Salary: {employee_2.get_promotion(3000)}")
employee_2.show_info()
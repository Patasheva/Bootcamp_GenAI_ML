# Exercise 1 : Basic Classes

# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Add methods to this class:
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# show_info(self) : that will print the information of the employee --> name, age, job, salary
# Create 2 users object and display their attribute
# Lea Smith 30 years old developer 25000 euros
# David Schartz 20 years old project manager 20000 euros
# Call all the methods

class Employee :

    company = "Amazon"
    number_employees = 0

    def __init__(self, fn, ln, age_emp, job_emp, salary_emp) :
        self.first_name = fn
        self.last_name = ln
        self.age = age_emp
        self.job = job_emp
        self.salary = salary_emp
        Employee.number_employees += 1 # des qu'un objet est cree, onaugmente le "class attribute"

    def full_name(self) :
        return self.first_name + " " + self.last_name
    
    def happy_birthday(self) :
        self.age += 1
        return self.age
    
    def get_promotion(self, amount):
        self.salary += amount

    def show_info(self):
        print(f"The employee named {self.full_name()} is {self.age} years old, he is a {self.job}, she/he earns {self.salary} euros")

employee_1 = Employee("Lea", "Smith", 30, "developer", 20000)
#employee_1 c'est un objet de la classe Employee
#employee_1 c'est une instance de la classe Employee

employee_2 = Employee("John", "Vik", 19, "data analyst", 40000)

# employee_1.get_promotion(10000)
# employee_1.show_info()
# employee_1.happy_birthday()
# employee_1.show_info()

# employee_2.show_info()

print(employee_1.company)
print(Employee.company)

print(Employee.number_employees)
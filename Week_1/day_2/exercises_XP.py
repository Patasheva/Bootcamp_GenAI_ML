""" # Exercise 2 Cinemax
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age > 12:
        ticket_price = 15
    elif  age > 3:
        ticket_price = 10
    else:
        ticket_price = 0
    total_cost += ticket_price
    print(f"{name} pay {ticket_price}")
print(total_cost)

# Exercise 4 Some Geography
def describe_city(city, country= "France"):
    print(f"{city} is in {country}.")
describe_city("Paris")

# Exercise 5 Random
import random

def compare_numbers(user_number):
    if not 1 <= user_number <= 100:
        print("Please enter a number between 1 and 100.")
        return

    random_number = random.randint(1, 100)
    if user_number == random_number:
        print(f"Success! Both numbers are {user_number}.")
    else:
        print(f"Fail. Your number: {user_number}, Random number: {random_number}.")
compare_numbers(13) 

# Exercise 6 Let’s Create Some Personalized Shirts!
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt("S", "I love you")

# Exercise 7 Temperature Advice
import random

def get_random_temp(season):
    if season.lower() == 'winter':
        return random.randint(-10, 16)
    elif season.lower() == 'spring':
        return random.randint(5, 25)
    elif season.lower() == 'summer':
        return random.randint(15, 40)
    elif season.lower() in ['autumn', 'fall']:
        return random.randint(5, 25)
    else:
        return random.randint(-10, 40)

def main():
     season = input("Please enter a season: ")
     temp = get_random_temp(season)
     if temp < 0:
          print("Brrr, that’s freezing! Wear some extra layers today!")
     elif temp < 16:
          print("Quite chilly! Don’t forget your coat!")
     elif temp < 23: 
          print("Pleasant temperature! A light jacket will be enough.")
     elif temp < 32: 
          print("It's nice out! Enjoy the good weather.")
     else:
          print("Heatwave! Don't forget to hydrate.")  
main() """

# Exercise 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
# function quiz
def ask_questions(data):
    correct_answers = 0
    incorrect_answers = 0
    for question in data:
        user_answer = input(f"{question['question']}: ").strip()
        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
            incorrect_answers += 1
    return correct_answers, incorrect_answers
# function information 
def display_results(correct, incorrect):
    print(f"\nQuiz Results:")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

correct, incorrect = ask_questions(data)
display_results(correct, incorrect)



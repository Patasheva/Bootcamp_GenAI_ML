# colors = ["red", "pink", "green"]

# first_color =  colors[0]
# last_color = colors[-1]
# counter = 0
# color = colors[counter+1] #color[1] #pink

# dictionnaires

# user = {
#     key : value,
#     key : value,
#     key : value,
# }

# dictionnaire

# liste
# ["a", "b", "c"]

# # tuple
# (0, "red")

# dictionnaire
# user = {
#     "first_name" : "John", 
#     "age" : 30,
#     "is_married" : False,
#     "animals" : ["cat", "dog"]
# }

# print(user["first_name"])
# print(user)
# print(user.items())

# dict_items([
#     ('first_name', 'John'), 
#     ('age', 30),
#     ('is_married', False), 
#     ('animals', ['cat', 'dog'])
#     ])

# for element in user.items() :
#     print(element)

# for clef, valeur in user.items() :
#     print(f"son {clef} est {valeur}")




users = [
    {
        "first_name" : "John", 
        "age" : 30,
         "is_married" : False,
    },
    {
        "first_name" : "Lea", 
        "age" : 35,
        "is_married" : True,
    }
]

# recuperer l'age de la 2e personne
# age_second_person = users[1]["age"]
# print(age_second_person)


# (0, ["cat", "dog"])


# JEU QUIZ
# 30 questions
#     - Instruction
#     - Option 
#     - Reponse


quiz = [
    {
        "instruction": "Quelle est la capitale de la France",
        "options": ["Paris", "Toulouse", "Bordeaux", "Lyon"],
        "reponse" : "Paris",
    },
    {
        "instruction": "Quelle est la superficie de la France",
        "options": [23.4, 45,9, 100, 300],
        "reponse" : 300,
    }
]

# avec les elements de la liste
for question in quiz :
    question_instruction = question["instruction"]
    question_response = question["reponse"]
    print(f" la question est {question_instruction} - la reponse est {question_response}")

#avec des index
for i in range(len(quiz)) :
    # print(i)
    question = quiz[i]
    question_instruction = question["instruction"]
    question_response = question["reponse"]
    print(f" la question est {question_instruction} - la reponse est {question_response}")

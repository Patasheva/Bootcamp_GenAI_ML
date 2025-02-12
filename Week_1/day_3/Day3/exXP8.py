data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
]

# ECRIRE
# DECOMPOSER L'EXERCICE 

# sauvegarder le nombre de reponses correctes -> variable integer
# sauvegarder le nombre de reponses incorrectes -> variable integer
# sauvegarder les reponses incorrectes dans une liste -> Liste de dictionnaire : question, reponse de l'utilisateur

# [
#     {
#         "question" : "...",
#         "answer" : "...",
#         "bad_answer" : "..."
#     }
# ]

# ["...", "dddd"]


# function pour le quiz
# notions : boucle - afficher et poser la question
# notions : fonction input
# notions : condition
# sauvegarder les resultats



def play_quiz():
    incorrect_answers = 0
    correct_answers = 0
    incorrect_answers_details = []

    for quest in data :
        answer_user = input(quest["question"]) #poser la question
        if answer_user.lower() == quest["answer"].lower(): # si correct
            correct_answers += 1
        else : # si incorrect
            incorrect_answers += 1
            dict_question = {
                "question" : quest["question"],
                "good_answer" : quest["answer"],
                "bad_answer" : answer_user
            }
            incorrect_answers_details.append(dict_question)
        
    return (incorrect_answers, correct_answers, incorrect_answers_details) #1er etape



def inform_user() :
    num_incorrect_answers, num_correct_answers, details = play_quiz()

    print("correct_answers", num_correct_answers)
    print("incorrect_answers", num_incorrect_answers)
    print("incorrect_answers_details", details)

inform_user()


# def test ():
#     return (1,2,3)

# a, b, c = test()
# print(a, b, c)
# # => a = 1
# => b = 2
# => c = 3






# fonction pour informer du resultat



def play_quiz_more():
    incorrect_answers = 0
    correct_answers = 0
    incorrect_answers_details = []

    for quest in data :
        answer_user = input(quest["question"]) #poser la question
        if answer_user.lower() == quest["answer"].lower(): # si correct
            correct_answers += 1
        else : # si incorrect
            incorrect_answers += 1
            dict_question = {
                "question" : quest["question"],
                "good_answer" : quest["answer"],
                "bad_answer" : answer_user
            }
            incorrect_answers_details.append(dict_question)
        
    inform_user_more(incorrect_answers, correct_answers, incorrect_answers_details) 

def inform_user_more(num_incorrect_answers, num_correct_answers, details) :
    print("correct_answers", num_correct_answers)
    print("incorrect_answers", num_incorrect_answers)
    print("incorrect_answers_details", details)

play_quiz_more()






# def test ():
#     return "hello"
#     if 1<2 :
#         ...

# a, b, c = test()
# print(a, b, c)
# # => a = 1
# => b = 2
# => c = 3

# def test ():
#     if 1<2 :
#         return "SUPER"
#     else :
#         return "NOOO"
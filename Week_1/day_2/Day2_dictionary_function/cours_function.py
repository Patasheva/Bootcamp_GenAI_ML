
# userA = "John"
# print(f"Hello {userA}")

# userB = "Lea"
# print(f"Hello {userB}")

# creer la fonction
# def welcome_user() :
#     # inside the function
#     print("Hello")

# # executer une fonction  = appeler la fonction
# welcome_user()
# welcome_user()
# welcome_user()
# welcome_user()
# welcome_user()

# creer la fonction
# def nom_function() :
#     '''
#     ici
#     '''

# def calculate() :
#     total = 1+2
    
# calculate()

#   num_function parametre
# def calculate(number)  :
#     for i in range(1, 11) : #boucle de 0 a 9
#         print(f"{number} * {i} = {number*i}")
#         # "5 * 0 = 0"
#         # "5 * 1 = 1"

# # argument
# calculate(5)
# calculate(8)


# function  :
# objectif : verifier que le nombre en entree est superieur a 18
# si superieur a 18 --> personne majeure
# personne mineure

# def check_age(age_user) :
#     if age_user >= 18 :
#         print("personne majeure")
#     else :
#         print("personne mineure")

# check_age(23)
# check_age(2)
# check_age(42)


# def check_age(age_user) :
#     if age_user >= 18 :
#         print("personne majeure")
#     else :
#         print("personne mineure")

# reponse_user = int(input("what is your age ?"))
# check_age(reponse_user)

# creer une fonction qui recupere en entree 
# le numero de ma table
# la liste des prix des plats
# et renvoie la sum a payer
# une phrase d'indication
# def pay_restaurant(num_table, list_price, first_name) :
#     total = sum(list_price)
#     print(f"la table {num_table} doit payer {total} euros")

# pay_restaurant(1, [34,76,12], "John")
# pay_restaurant(2, [23,56,34], "John")
# pay_restaurant(3, [34,36,12], "John")

#annotation = indication
# def check_user(name : str, age : int) :
#     print(f"hello {name} - {age}")

# check_user(16, "Lea")
# check_user(age=16, name="John")

# calculate_average

# def calculate_average(list_number) :
#     average = sum(list_number) / len(list_number)
#     return average

# my_average = average

# # my_average = calculate_average([3,7,9,10])

# # print(my_average) #meme
# # print(calculate_average([3,7,9,10])) #meme

# global variable
# variable locale

# user = "John" #globale

# def test() : # local #bloc
#     print(user)

# test()



# def testA() : # local #bloc
#     user_website = "Lea"
#     return user_website

# # pour que la valeur de cette variable qui a ete cree localement
# # puisse etre utilise globalement
# # il faut utiliser return

# my_user = testA() # my_user = "Lea"
# print(my_user)


# UNE FONCTION = UNE ACTION
# UNE FONCTION QUI CALCULE LA SOMME DE MON REPAS
# UNE FONCTION QUI CALCULE TTC

def calculate_total_ht(liste_price) :
    total = sum(liste_price)
    return total #1er etape

# 1. recuperer la somme HT
# 2. multiplier par la taxe
# 3. afficher le resultat
def calculate_price_ttc() :
    total_ht = calculate_total_ht([3,7,9,10])
    # total_ht devient egal a ce que la fonction calculate_total_ht([3,7,9,10]) me renvoie
    total_ttc = total_ht*1.2
    print(f"le prix est {total_ttc}")

calculate_price_ttc()
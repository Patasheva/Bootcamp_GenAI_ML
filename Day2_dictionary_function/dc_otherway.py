
word = "ppoeemm"

word_second =  word[0] #"p"

for index, letter in enumerate(word) :
    print(f"{index} - {letter}") 
    last_letter = word_second[-1]
    if index <= len(word)-2 and word[index+1] != last_letter:
        word_second += word[index+1]

print(word_second)




# colors = ["red", "pink", "green"]

# list(enumerate(colors)) #converti l'object cree par la fonction enumerate en liste
# [
#     (0, 'red'), 
#     (1, 'pink'), 
#     (2, 'green')
# ]

# colors = ["red", "pink", "green"]

# for color in colors :
#     print(color)

# for index, color in enumerate(colors) :
#     print(f"{index} - {color}") 


# 1er boucle
#  index : 0
#  color : "red"

# 2e boucle
#  element = (1, "pink")


# 1er boucle
#  element = (0, "red")

# 2e boucle
#  element = (1, "pink")




# user = ("John", "Smith")
# # print(user)

# variableA, variableB = tuple
# variableA = tuple[0]
# variableB = tuple[1]

# first_name, last_name = user #("John", "Smith")
# print(first_name)
# print(last_name)

# # liste 
# colorA, colorB = ["red", "pink"]
# print(colorA)
# print(colorB)
# print(f"{colorA} - {colorB}")
# print(colorA, colorB)

# # chaine de caractere
# letterA, letterB = "He"
# print(letterA)
# print(letterB)

#destructuration
# city, country = "Paris","France"
# print(city)
# print(country)
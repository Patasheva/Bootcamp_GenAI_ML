# Write a program that asks a string to the user, 
# and display a new string with any duplicate consecutive letters removed.

word = "ppoeemm"

word_second =  word[0] #on commence avec la premiere lettre

# ajout
# on boucle pour parcourir la variable word
for letter in word :
    last_letter = word_second[-1] #"o"
    if letter != last_letter :
        word_second += letter
        # word_second = word_second + letter

print(word_second)


# 1er boucle
#     word_second = "p"
#     letter = "p"
#     last_letter = "p" --> je ne rentre pas dans le if

# 2e boucle
#     word_second = "p"
#     letter = "p"
#     last_letter = "p" --> je ne rentre pas dans le if

# 3e boucle
#     word_second = "p"
#     letter = "o"
#     last_letter = "p" 
#     --> je ne rentre pas dans le if et je rajoute la lettre
#     word_second = "po"

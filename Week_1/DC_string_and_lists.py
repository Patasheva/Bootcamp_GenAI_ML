# Challenge 1
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))
# Generate the list of multiples
multiples_list = [number * i for i in range(1, length + 1)]
print(multiples_list) 

# Challenge 2
word = input("Enter a word: ")

def remove_consecutive_duplicates(word):
    resultat = ""
    for i in range(len(word)):
        if i == 0 or word[i] != word[i - 1]:
            resultat += word[i]
    return resultat

word_after_removing = remove_consecutive_duplicates(word)
print(word_after_removing)
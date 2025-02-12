def create_letter_index_dict(word):
    letter_dict = {}
    for index, letter in enumerate(word.lower()):
        if letter not in letter_dict:
            letter_dict[letter] = [index]
        else:
            letter_dict[letter].append(index)
    return letter_dict

user_word = input("Please enter a word : ")

result = create_letter_index_dict(user_word)

print("Dictionary :")
for letter, indexes in result.items():
    print(f"'{letter}': {indexes}")
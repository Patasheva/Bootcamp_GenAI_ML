
# Create a function average_length_of_words which 
# takes a string as an argument and 
# returns the average length of the words in the string

# verb
def calculate_average(sentence) :
    # convert the string into list
    list_of_word = sentence.split(" ") #converti la chaine de mot en liste de mot
    print(list_of_word) #['hello', 'how', 'are', 'you']

    # calculate the number of letter of the word
    total = 0
    for word in list_of_word:
        total += len(word)
    
    average = total/len(list_of_word)
    # print(average)
    return average

calculate_average("hello how are you")

                     #parametre
# def calculate_average(sentence) :
#     length_word = len(sentence) #nombre de caracteres
#     return length_word

# calculate_average("hello how are you")
                    #argument
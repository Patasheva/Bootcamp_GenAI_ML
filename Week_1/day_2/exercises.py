# Exercise 1
user = {
    'first_name' : 'John', 
    'last_name' : 'Doe', 
    'favorite_hobby' : 'Python',
    'sports_hobby' : 'gym',
    'age' : 82}
print(user)

# Exercise 2
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

total = 0
for music in playlist['songs']:
    music_duration = music["duration"]
    total += music_duration 
print(music["duration"])
print(f"Je vais écouter de  la musique pendant total {total} minutes")

total_duration = sum(song['duration'] for song in playlist ['songs']) 

# Exercise 3
def calculate_average(sentence) :
    # convert the string into list
    list_of_words = sentence.split(" ")
    print(list_of_words)
    
    # calculate the number of letters of the word
    total = 0
    for word in list_of_words:
        total += len(word)
    
    average = total/len(list_of_words)
    print(average)
    return average
calculate_average('hello how are you')

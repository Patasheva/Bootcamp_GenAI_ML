# Print the total duration of the playlist
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
liste_musique = playlist["songs"]
duration_first_music = playlist["songs"][0]["duration"]

for music in playlist["songs"] :
    music_duration = music["duration"]
    total += music_duration

print(f"je vais ecouter de la musique pendant {total} minutes")

# Print the total duration of the playlist
# 1. ou se trouve la duration
# 2. ou boucler

all_durations = []

for music in playlist["songs"] :
    music_duration = music["duration"]
    all_durations.append(music_duration)

total = sum(all_durations) # on utilise la fonction sum

print(f"je vais ecouter de la musique pendant {total} minutes")

# list comprehension
total_duration = sum(song['duration'] for song in playlist['songs'])
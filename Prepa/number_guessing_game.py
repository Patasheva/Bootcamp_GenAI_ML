import random
def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7 

    for i in range(1, max_attempts+1):
        try: 
            player_guess = int(input('Enter a number between 1 et 100: '))
            if player_guess < random_number:
               print('Too low!')
            elif player_guess > random_number:
               print('Too high!')
            else:
               print('Congratulations! You got it!')
               break 
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    else:
        print(f"Sorry, you failed to guess the number. The number was {random_number}.")

number_guessing_game()
        
    
    

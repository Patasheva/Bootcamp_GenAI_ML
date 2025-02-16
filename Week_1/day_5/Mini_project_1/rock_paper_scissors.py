from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print(" (g) Play a new game")
    print(" (x) Show scores and exit")

    valid_choices = ["g", "x"]
    while True:
        choice = input("Do you want to play? (g to play, x to exit): ").strip().lower()
        if choice in valid_choices:
           return choice 
        print("Invalid choice. Please select 'g' to play or 'x' to exit.")
        
def print_results(results):
    print("\nGame Results Summary:")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("\nThank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    choice = get_user_menu_choice()
    while choice == "g":  
        game = Game()  
        result = game.play()  
        results[result] += 1 
          
        choice = get_user_menu_choice()
    print_results(results)
    
if __name__ == "__main__":
    main()
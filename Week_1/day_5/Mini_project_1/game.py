import random 
class Game:
    def get_user_item(self):
        choices = ["r", "p", "s"]
        while True:
            user_item = input("Please choose 'r' for rock or 'p' for paper or 's' for scissors: ").lower()
            if user_item in choices:
                return user_item
            else: 
                print("Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
    
    def get_computer_item(self):
        computer_item = random.choice(["r", "p", "s"])
        return  computer_item 
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "r" and computer_item == "s") or \
             (user_item == "s" and computer_item == "p") or \
             (user_item == "p" and computer_item == "r"):
            return "win"
        else:
            return "loss"
    
    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)
        
        print(f"You selected {user_choice}. The computer selected {computer_choice}. You {result}!")
        return result

game = Game()
game.play()
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    
  
    while player_choice not in options:
        print("Invalid choice. Please try again.")
        player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

def play_game():
    while True:
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()

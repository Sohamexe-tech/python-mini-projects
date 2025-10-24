import random

# Define possible choices
CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
    """Prompts the user for their choice and validates the input."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower().strip()
        
        if user_input == 'q':
            return 'quit'
        
        if user_input in CHOICES:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of a single round."""
    
    # Check for a tie
    if user_choice == computer_choice:
        return "tie"
    
    # Check all possible winning conditions for the user
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        # If it wasn't a tie and the user didn't win, the computer wins
        return "computer"

def main():
    """Main function to run the game loop and manage the score."""
    user_score = 0
    computer_score = 0
    
    print("\n--- Rock, Paper, Scissors Game ---")
    
    # Main game loop
    while True:
        print("\n" + "="*30)
        print(f"Current Score: You {user_score} - Computer {computer_score}")
        
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            break

        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        # Update score and display result
        if winner == "user":
            user_score += 1
            print("🎉 You Win this round!")
        elif winner == "computer":
            computer_score += 1
            print("💻 Computer wins this round!")
        else:
            print("🤝 It's a Tie!")
            
    # Game over
    print("\n" + "="*30)
    print("GAME OVER!")
    print(f"FINAL SCORE: You {user_score} - Computer {computer_score}")
    
    if user_score > computer_score:
        print("🏆 Congratulations! You won the match!")
    elif computer_score > user_score:
        print("Better luck next time. The Computer won the match.")
    else:
        print("The match ended in a draw!")
    print("="*30)

if __name__ == "__main__":
    main()
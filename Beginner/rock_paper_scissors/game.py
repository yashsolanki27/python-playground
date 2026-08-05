"""
Rock Paper Scissors Game
A classic hand game to learn conditionals, random module, and user input.

How to Play:
1. Choose rock, paper, or scissors
2. Computer makes a random choice
3. Winner is determined by classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
4. Play multiple rounds and track your score!

Python Concepts:
- If-else statements
- Random module
- String comparison
- Loops
- Score tracking
- Input validation
"""

import random


def display_welcome():
    """Display welcome message and game rules."""
    print("=" * 50)
    print(" Rock Paper Scissors!")
    print("=" * 50)
    print("\nRules:")
    print("  Rock crushes Scissors")
    print("  Scissors cuts Paper")
    print("  Paper covers Rock")
    print("\nType 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.\n")


def get_player_choice() -> str:
    """
    Get and validate player's choice.
    
    Returns:
        Valid choice string (rock, paper, scissors) or 'quit'
    """
    valid_choices = ['rock', 'paper', 'scissors', 'quit']
    
    while True:
        choice = input("Enter your choice: ").lower().strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please enter 'rock', 'paper', 'scissors', or 'quit'.")


def get_computer_choice() -> str:
    """
    Generate computer's random choice.
    
    Returns:
        Random choice from rock, paper, scissors
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(player: str, computer: str) -> str:
    """
    Determine the winner based on game rules.
    
    Args:
        player: Player's choice
        computer: Computer's choice
        
    Returns:
        'player', 'computer', or 'tie'
    """
    if player == computer:
        return 'tie'
    
    # Winning conditions for player
    winning_conditions = {
        'rock': 'scissors',      # Rock crushes Scissors
        'scissors': 'paper',     # Scissors cuts Paper
        'paper': 'rock'          # Paper covers Rock
    }
    
    if winning_conditions[player] == computer:
        return 'player'
    else:
        return 'computer'


def display_result(player: str, computer: str, result: str):
    """
    Display the round result.
    
    Args:
        player: Player's choice
        computer: Computer's choice
        result: 'player', 'computer', or 'tie'
    """
    # Display choices with emoji representations
    choice_display = {
        'rock': '🪨 Rock',
        'paper': '📄 Paper',
        'scissors': '✂️  Scissors'
    }
    
    print(f"\nYou chose: {choice_display[player]}")
    print(f"Computer chose: {choice_display[computer]}")
    print("-" * 30)
    
    if result == 'tie':
        print(" It's a tie!")
    elif result == 'player':
        print(" You win this round!")
    else:
        print(" Computer wins this round!")


def display_score(player_wins: int, computer_wins: int, ties: int):
    """
    Display current score.
    
    Args:
        player_wins: Number of player wins
        computer_wins: Number of computer wins
        ties: Number of ties
    """
    total_games = player_wins + computer_wins + ties
    
    print(f"\n{'=' * 30}")
    print(f" SCOREBOARD (Games: {total_games})")
    print(f"{'=' * 30}")
    print(f" Player:    {player_wins} wins")
    print(f" Computer:  {computer_wins} wins")
    print(f" Ties:      {ties}")
    print(f"{'=' * 30}")


def play_game():
    """Main game function."""
    display_welcome()
    
    # Score tracking
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    # Game loop
    while True:
        # Get player choice
        player_choice = get_player_choice()
        
        # Check for quit
        if player_choice == 'quit':
            break
        
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Update score
        if result == 'player':
            player_wins += 1
        elif result == 'computer':
            computer_wins += 1
        else:
            ties += 1
        
        # Display result
        display_result(player_choice, computer_choice, result)
        
        # Display updated score
        display_score(player_wins, computer_wins, ties)
        
        print()  # Empty line for readability
    
    # Final score
    print("\n" + "=" * 50)
    print(" FINAL SCORE")
    print("=" * 50)
    display_score(player_wins, computer_wins, ties)
    
    # Determine overall winner
    if player_wins > computer_wins:
        print("\n🏆 Congratulations! You are the overall winner!")
    elif computer_wins > player_wins:
        print("\n🤖 Computer is the overall winner!")
    else:
        print("\n🤝 It's a draw overall!")
    
    print("\nThanks for playing! Goodbye!")


def main():
    """Main entry point with play again functionality."""
    while True:
        play_game()
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print("\nSee you next time!")
            break
        
        print("\n" + "=" * 50)
        print(" Starting a new game...")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
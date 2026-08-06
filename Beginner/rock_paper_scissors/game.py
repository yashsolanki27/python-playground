"""
Rock Paper Scissors Game
A classic game to learn random choices, dictionaries, and game logic.

How to Play:
1. Choose Rock, Paper, or Scissors
2. Computer randomly picks its choice
3. Winner is decided by classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
4. Play multiple rounds and track your score!

Python Concepts:
- Random module for computer choices
- Dictionaries for storing choices and results
- Loops for multiple rounds
- Conditionals for win/lose logic
- String formatting and output
- Score tracking with variables
"""

import random


# Game choices and their symbols
CHOICES = {
    '1': ('Rock', '🪨'),
    '2': ('Paper', '📄'),
    '3': ('Scissors', '✂️')
}

# Win conditions: key beats value
WIN_CONDITIONS = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}


def display_menu() -> str:
    """Display the game menu and get player choice.
    
    Returns:
        Player's choice as string (Rock/Paper/Scissors)
    """
    print("\n  Make your choice:")
    print("  1. 🪨  Rock")
    print("  2. 📄  Paper")
    print("  3. ✂️  Scissors")
    print("  4. 🚪  Quit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in CHOICES:
            return CHOICES[choice][0]
        elif choice == '4':
            return 'Quit'
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_computer_choice() -> str:
    """Randomly select computer's choice.
    
    Returns:
        Computer's choice as string
    """
    return random.choice(list(CHOICES.values()))[0]


def determine_winner(player: str, computer: str) -> str:
    """Determine the winner of the round.
    
    Args:
        player: Player's choice
        computer: Computer's choice
        
    Returns:
        'player', 'computer', or 'tie'
    """
    if player == computer:
        return 'tie'
    elif WIN_CONDITIONS[player] == computer:
        return 'player'
    else:
        return 'computer'


def display_result(player: str, computer: str, result: str) -> None:
    """Display the round result.
    
    Args:
        player: Player's choice
        computer: Computer's choice
        result: 'player', 'computer', or 'tie'
    """
    player_emoji = dict(CHOICES.values())[player]
    computer_emoji = dict(CHOICES.values())[computer]
    
    print(f"\n  You chose:      {player} {player_emoji}")
    print(f"  Computer chose: {computer} {computer_emoji}")
    print("  " + "-" * 30)
    
    if result == 'tie':
        print("  🤝 It's a TIE!")
    elif result == 'player':
        print("  🎉 You WIN this round!")
    else:
        print("  💻 Computer WINS this round!")


def display_score(wins: int, losses: int, ties: int) -> None:
    """Display current score.
    
    Args:
        wins: Number of player wins
        losses: Number of computer wins
        ties: Number of ties
    """
    total = wins + losses + ties
    print(f"\n  📊 SCOREBOARD (after {total} round(s))")
    print(f"  {'='*30}")
    print(f"  Player Wins:   {wins} 🎉")
    print(f"  Computer Wins: {losses} 💻")
    print(f"  Ties:          {ties} 🤝")
    
    if total > 0:
        win_rate = (wins / total) * 100
        print(f"  Win Rate:      {win_rate:.1f}%")


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  ROCK PAPER SCISSORS")
    print("="*50)
    print("\nWelcome to Rock Paper Scissors!")
    print("\nRules:")
    print("  🪨 Rock     → beats ✂️  Scissors")
    print("  📄 Paper    → beats 🪨 Rock")
    print("  ✂️  Scissors → beats 📄 Paper")
    print("\nPython Concepts: Random, Dictionaries, Conditionals")


def play_game() -> None:
    """Main game loop with score tracking."""
    display_welcome()
    
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        player_choice = display_menu()
        
        if player_choice == 'Quit':
            break
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        display_result(player_choice, computer_choice, result)
        
        if result == 'player':
            wins += 1
        elif result == 'computer':
            losses += 1
        else:
            ties += 1
        
        display_score(wins, losses, ties)
    
    # Final summary
    print("\n" + "="*50)
    print("  FINAL RESULTS")
    print("="*50)
    display_score(wins, losses, ties)
    
    total = wins + losses + ties
    if total == 0:
        print("\n  You didn't play any rounds!")
    elif wins > losses:
        print("\n  🏆 Great job! You beat the computer!")
    elif losses > wins:
        print("\n  💻 Computer won this time. Try again!")
    else:
        print("\n  🤝 It's a draw overall!")
    
    print("\nThanks for playing Rock Paper Scissors!")
    print("See you next time!")


def main() -> None:
    """Main entry point."""
    play_game()


if __name__ == "__main__":
    main()

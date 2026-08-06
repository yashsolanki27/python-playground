"""
Number Guessing Game
A simple game to learn variables, loops, conditionals, and user input.

How to Play:
1. The computer picks a random number between 1 and 100
2. You have 7 attempts to guess the number
3. After each guess, you get a hint: "Too high!" or "Too low!"
4. Win by guessing the correct number!

Python Concepts:
- Variables and data types
- Random module
- While loops
- If/elif/else conditionals
- User input and type conversion
- Game state tracking
- f-strings for formatting
"""

import random


def get_difficulty() -> tuple[str, int]:
    """Get difficulty level from user and return range tuple.
    
    Returns:
        Tuple of (difficulty_name, max_attempts)
    """
    print("\nSelect Difficulty:")
    print("1. Easy   (1-50,  10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")
    
    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice == '1':
            return "Easy", 10
        elif choice == '2':
            return "Medium", 7
        elif choice == '3':
            return "Hard", 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_range(difficulty: str) -> tuple[int, int]:
    """Get number range based on difficulty.
    
    Args:
        difficulty: Difficulty level name
        
    Returns:
        Tuple of (min_number, max_number)
    """
    ranges = {
        "Easy": (1, 50),
        "Medium": (1, 100),
        "Hard": (1, 200)
    }
    return ranges.get(difficulty, (1, 100))


def get_guess(min_num: int, max_num: int) -> int | None:
    """Get and validate user's guess.
    
    Args:
        min_num: Minimum possible number
        max_num: Maximum possible number
        
    Returns:
        Valid guess as integer, or None for quit command
    """
    while True:
        user_input = input(f"\nEnter your guess ({min_num}-{max_num}) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            guess = int(user_input)
            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}.")
                continue
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_round() -> bool:
    """Play one round of the number guessing game.
    
    Returns:
        True if player wants to play again, False otherwise
    """
    difficulty, max_attempts = get_difficulty()
    min_num, max_num = get_range(difficulty)
    
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    guessed = False
    
    print(f"\n{'='*50}")
    print(f"  NUMBER GUESSING GAME - {difficulty.upper()}")
    print(f"{'='*50}")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!")
    
    while attempts < max_attempts and not guessed:
        remaining = max_attempts - attempts
        print(f"\n--- Attempts remaining: {remaining} ---")
        
        guess = get_guess(min_num, max_num)
        
        if guess is None:
            print(f"\nGame quit! The number was {secret_number}.")
            return False
        
        attempts += 1
        
        if guess == secret_number:
            guessed = True
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    
    if guessed:
        print(f"\n{'*'*50}")
        print(f"  CONGRATULATIONS! You guessed it!")
        print(f"  The number was {secret_number}")
        print(f"  You took {attempts} attempt(s)")
        
        if attempts == 1:
            print("  INCREDIBLE! First try!")
        elif attempts <= 3:
            print("  Excellent work!")
        elif attempts <= 5:
            print("  Good job!")
        else:
            print("  Close call!")
        print(f"{'*'*50}")
    else:
        print(f"\n{'='*50}")
        print(f"  GAME OVER! You ran out of attempts.")
        print(f"  The number was {secret_number}")
        print(f"{'='*50}")
    
    return False


def display_welcome() -> None:
    """Display welcome message and game rules."""
    print("\n" + "="*50)
    print("  NUMBER GUESSING GAME")
    print("="*50)
    print("\nWelcome to the Number Guessing Game!")
    print("\nRules:")
    print("  1. The computer picks a random number")
    print("  2. You try to guess it within limited attempts")
    print("  3. You'll get hints after each guess")
    print("  4. Choose your difficulty level")
    print("\nPython Concepts: Variables, Loops, Conditionals, Input")


def main() -> None:
    """Main game loop."""
    display_welcome()
    
    while True:
        play_round()
        
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Number Guessing Game!")
            print("See you next time!")
            break


if __name__ == "__main__":
    main()

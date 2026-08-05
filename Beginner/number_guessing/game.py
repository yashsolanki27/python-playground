"""
Number Guessing Game
A beginner Python game to learn variables, loops, conditionals, and the random module.

How to Play:
1. The computer generates a random number between 1 and 100
2. You have 7 attempts to guess the number
3. After each guess, you'll get a hint (too high/too low)
4. Win by guessing the correct number!

Python Concepts:
- Variables and data types
- Loops (while)
- Conditionals (if/elif/else)
- Random module
- User input/output
- Error handling
"""

import random


def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 50)
    print(" Welcome to the Number Guessing Game!")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it.")
    print("After each guess, I'll tell you if it's too high or too low.\n")


def get_user_guess(attempt: int) -> int:
    """
    Get and validate user input.
    
    Args:
        attempt: Current attempt number
        
    Returns:
        Valid integer guess
    """
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/7 - Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def check_guess(guess: int, target: int) -> str:
    """
    Compare guess with target number.
    
    Args:
        guess: User's guess
        target: Secret number
        
    Returns:
        Hint string
    """
    if guess < target:
        return "too low"
    elif guess > target:
        return "too high"
    else:
        return "correct"


def play_game():
    """Main game function."""
    display_welcome()
    
    # Generate random number
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        guess = get_user_guess(attempts)
        
        # Check the guess
        result = check_guess(guess, secret_number)
        
        if result == "correct":
            print(f"\n{'=' * 50}")
            print(f" Congratulations! You guessed it!")
            print(f" The number was {secret_number}")
            print(f" You got it in {attempts} attempt{'s' if attempts > 1 else ''}!")
            print(f"{'=' * 50}")
            return True
        else:
            remaining = max_attempts - attempts
            print(f"Your guess is {result}!")
            if remaining > 0:
                print(f"You have {remaining} attempt{'s' if remaining > 1 else ''} remaining.\n")
    
    # Out of attempts
    print(f"\n{'=' * 50}")
    print(f" Game Over!")
    print(f" You ran out of attempts.")
    print(f" The number was {secret_number}")
    print(f"{'=' * 50}")
    return False


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
            print("\nThanks for playing! Goodbye!")
            break
        
        print("\n" + "=" * 50)
        print(" Starting a new game...")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
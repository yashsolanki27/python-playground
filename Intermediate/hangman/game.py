"""
Hangman Game
A word guessing game to learn lists, strings, loops, and conditionals.

How to Play:
1. The computer selects a random word
2. You have 6 attempts to guess the word
3. Guess one letter at a time
4. Correct letters are revealed in the word
5. Wrong guesses add to the hangman drawing
6. Win by guessing the word before running out of attempts!

Python Concepts:
- Lists and list operations
- String manipulation
- Loops (while, for)
- Conditionals
- Random module
- Set operations
- ASCII art
"""

import random
from typing import List, Set


# Hangman ASCII art stages
HANGMAN_STAGES = [
    """
      ------
      |    |
      |
      |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    """
]

# Word categories
WORD_CATEGORIES = {
    "animals": ["elephant", "giraffe", "penguin", "dolphin", "cheetah", "kangaroo", "flamingo"],
    "fruits": ["strawberry", "blueberry", "pineapple", "watermelon", "raspberry", "blackberry"],
    "countries": ["australia", "brazil", "canada", "denmark", "egypt", "france", "germany"],
    "colors": ["scarlet", "turquoise", "magenta", "crimson", "emerald", "sapphire", "amethyst"],
    "sports": ["basketball", "volleyball", "badminton", "swimming", "cycling", "football"]
}


def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 60)
    print(" HANGMAN GAME")
    print("=" * 60)
    print("\nGuess the word before the hangman is complete!")
    print("You have 6 incorrect guesses allowed.")
    print("Type a single letter to guess.")
    print("Type 'quit' to exit the game.\n")


def display_hangman(wrong_guesses: int):
    """
    Display the hangman drawing based on wrong guesses.
    
    Args:
        wrong_guesses: Number of wrong guesses (0-6)
    """
    print(HANGMAN_STAGES[wrong_guesses])


def display_word_state(word: str, guessed_letters: Set[str]) -> str:
    """
    Display the current state of the word with guessed letters.
    
    Args:
        word: The secret word
        guessed_letters: Set of letters guessed so far
        
    Returns:
        Formatted word string
    """
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_random_word() -> str:
    """
    Select a random word from a random category.
    
    Returns:
        Random word string
    """
    category = random.choice(list(WORD_CATEGORIES.keys()))
    word = random.choice(WORD_CATEGORIES[category])
    return word, category


def get_valid_guess(guessed_letters: Set[str]) -> str:
    """
    Get a valid letter guess from the user.
    
    Args:
        guessed_letters: Set of letters already guessed
        
    Returns:
        Valid lowercase letter
    """
    while True:
        guess = input("\nEnter your guess: ").lower().strip()
        
        if guess == 'quit':
            return 'quit'
        
        if len(guess) != 1:
            print("Please enter a single letter!")
            continue
        
        if not guess.isalpha():
            print("Please enter a letter (A-Z)!")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try a different letter.")
            continue
        
        return guess


def play_game():
    """Main game function."""
    display_welcome()
    
    # Game statistics
    games_played = 0
    games_won = 0
    
    while True:
        # Select random word
        secret_word, category = get_random_word()
        guessed_letters: Set[str] = set()
        wrong_guesses = 0
        max_wrong = 6
        
        print(f"\nCategory: {category.upper()}")
        print(f"Word has {len(secret_word)} letters")
        display_hangman(wrong_guesses)
        print(f"\nWord: {display_word_state(secret_word, guessed_letters)}")
        
        # Game loop
        while wrong_guesses < max_wrong:
            # Get player's guess
            guess = get_valid_guess(guessed_letters)
            
            if guess == 'quit':
                print("\nThanks for playing! Goodbye!")
                return
            
            guessed_letters.add(guess)
            
            # Check if guess is in word
            if guess in secret_word.lower():
                print(f"✓ Good guess! '{guess}' is in the word!")
                
                # Check if player won
                if all(letter.lower() in guessed_letters for letter in secret_word):
                    games_played += 1
                    games_won += 1
                    print(f"\n{'=' * 60}")
                    print(f" CONGRATULATIONS!")
                    print(f" You guessed the word: {secret_word.upper()}")
                    print(f"{'=' * 60}")
                    display_hangman(wrong_guesses)
                    break
            else:
                wrong_guesses += 1
                print(f"✗ Sorry, '{guess}' is not in the word!")
                display_hangman(wrong_guesses)
            
            # Display current state
            print(f"\nWord: {display_word_state(secret_word, guessed_letters)}")
            print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Check if player lost
        if wrong_guesses >= max_wrong:
            games_played += 1
            print(f"\n{'=' * 60}")
            print(f" GAME OVER!")
            print(f" The word was: {secret_word.upper()}")
            print(f"{'=' * 60}")
        
        # Display statistics
        print(f"\n--- Statistics ---")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"Win rate: {win_rate:.1f}%")
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            break
        
        print("\n" + "=" * 60)
        print(" Starting new game...")
        print("=" * 60 + "\n")


def main():
    """Main entry point."""
    play_game()


if __name__ == "__main__":
    main()
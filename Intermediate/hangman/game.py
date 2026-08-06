"""
Hangman Game
A word guessing game to learn lists, sets, and string manipulation.

How to Play:
1. Choose a word category (Animals, Fruits, Countries, Colors, Sports)
2. Guess one letter at a time
3. You have 6 incorrect guesses before the hangman is complete
4. Guess the word before running out of attempts!

Python Concepts:
- Lists for tracking guessed letters
- Sets for unique letter tracking
- Strings and string methods
- Random module for word selection
- While loops and conditionals
- ASCII art display
- Game state management
"""

import random


# Word categories with sample words
WORD_CATEGORIES = {
    'Animals': [
        'elephant', 'giraffe', 'penguin', 'dolphin', 'butterfly',
        'kangaroo', 'octopus', 'cheetah', 'flamingo', 'hedgehog'
    ],
    'Fruits': [
        'strawberry', 'watermelon', 'pineapple', 'blueberry', 'raspberry',
        'pomegranate', 'cranberry', 'blackberry', 'tangerine', 'grapefruit'
    ],
    'Countries': [
        'australia', 'brazil', 'canada', 'denmark', 'ethiopia',
        'finland', 'germany', 'hungary', 'iceland', 'jamaica'
    ],
    'Colors': [
        'crimson', 'turquoise', 'magenta', 'lavender', 'scarlet',
        'emerald', 'sapphire', 'amethyst', 'ivory', 'bronze'
    ],
    'Sports': [
        'basketball', 'volleyball', 'badminton', 'swimming', 'cycling',
        'archery', 'fencing', 'bowling', 'curling', 'kayaking'
    ]
}

# Hangman ASCII stages
HANGMAN_STAGES = [
    """
      ------
      |    |
      |
      |
      |
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |
      |
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    ==========""",
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    =========="""
]


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  HANGMAN")
    print("="*50)
    print("\nWelcome to Hangman!")
    print("\nRules:")
    print("  1. Guess one letter at a time")
    print("  2. You have 6 wrong guesses allowed")
    print("  3. Each wrong guess adds to the hangman")
    print("  4. Guess the word before the hangman is complete!")
    print("\nPython Concepts: Lists, Sets, Strings, ASCII Art")


def select_category() -> str:
    """Let player choose a word category.
    
    Returns:
        Selected category name
    """
    print("\n  Choose a category:")
    categories = list(WORD_CATEGORIES.keys())
    
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    while True:
        choice = input(f"\nEnter choice (1-{len(categories)}): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")


def select_word(category: str) -> str:
    """Randomly select a word from the category.
    
    Args:
        category: Word category name
        
    Returns:
        Selected word in lowercase
    """
    words = WORD_CATEGORIES[category]
    return random.choice(words)


def display_game_state(word: str, guessed_letters: set[str], wrong_guesses: int) -> None:
    """Display current game state.
    
    Args:
        word: The secret word
        guessed_letters: Set of guessed letters
        wrong_guesses: Number of wrong guesses
    """
    # Display hangman
    print(HANGMAN_STAGES[wrong_guesses])
    
    # Display word with blanks
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\n  Word: {display_word}")
    print(f"  Wrong guesses: {wrong_guesses}/6")
    
    # Show guessed letters
    if guessed_letters:
        sorted_guessed = sorted(guessed_letters)
        print(f"  Guessed: {', '.join(sorted_guessed)}")


def get_guess(guessed_letters: set[str]) -> str | None:
    """Get a valid letter guess from the player.
    
    Args:
        guessed_letters: Set of already guessed letters
        
    Returns:
        Valid letter guess or None for quit
    """
    while True:
        guess = input("\nEnter a letter (or 'q' to quit): ").strip().lower()
        
        if guess == 'q':
            return None
        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        return guess


def check_win(word: str, guessed_letters: set[str]) -> bool:
    """Check if player has won.
    
    Args:
        word: The secret word
        guessed_letters: Set of guessed letters
        
    Returns:
        True if all letters guessed, False otherwise
    """
    return all(letter in guessed_letters for letter in word)


def play_round() -> bool:
    """Play one round of Hangman.
    
    Returns:
        True if player wants to play again
    """
    category = select_category()
    word = select_word(category)
    guessed_letters: set[str] = set()
    wrong_guesses = 0
    
    print(f"\n  Category: {category}")
    print(f"  Word has {len(word)} letters. Good luck!")
    
    while wrong_guesses < 6:
        display_game_state(word, guessed_letters, wrong_guesses)
        
        guess = get_guess(guessed_letters)
        
        if guess is None:
            print(f"\n  Game quit! The word was: {word}")
            return False
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"\n  ✅ '{guess}' is in the word!")
            
            if check_win(word, guessed_letters):
                display_game_state(word, guessed_letters, wrong_guesses)
                print("\n" + "*"*50)
                print("  🎉 CONGRATULATIONS! You guessed the word!")
                print(f"  The word was: {word.upper()}")
                print(f"  Wrong guesses: {wrong_guesses}/6")
                print("*"*50)
                return False
        else:
            wrong_guesses += 1
            print(f"\n  ❌ '{guess}' is not in the word!")
    
    # Game over - lost
    display_game_state(word, guessed_letters, wrong_guesses)
    print("\n" + "="*50)
    print("  💀 GAME OVER! The hangman is complete!")
    print(f"  The word was: {word.upper()}")
    print("="*50)
    
    return False


def main() -> None:
    """Main game loop."""
    display_welcome()
    
    while True:
        play_round()
        
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Hangman!")
            print("See you next time!")
            break


if __name__ == "__main__":
    main()

"""
Word Scramble Game
A word unscrambling game to learn string manipulation and list operations.

How to Play:
1. See a scrambled word
2. Try to unscramble it by guessing the original word
3. Get hints if needed (reveal letters)
4. Score points based on speed and hints used

Python Concepts:
- String manipulation and slicing
- Lists for letter tracking
- Random module for word selection
- Timer for scoring
- Sets for unique characters
- Game state management
"""

import random
import time


# Word lists by difficulty
WORD_LISTS = {
    'Easy': [
        'python', 'coding', 'loop', 'array', 'debug',
        'input', 'print', 'class', 'float', 'index',
        'pixel', 'stack', 'cache', 'query', 'merge'
    ],
    'Medium': [
        'algorithm', 'function', 'variable', 'compiler', 'database',
        'interface', 'keyboard', 'monitor', 'network', 'server',
        'terminal', 'runtime', 'package', 'module', 'boolean'
    ],
    'Hard': [
        'polymorphism', 'inheritance', 'abstraction', 'recursion', 'iteration',
        'asynchronous', 'encapsulation', 'dependency', 'microservice', 'refactoring',
        'serialization', 'multithreading', 'documentation', 'optimization', 'exception'
    ]
}


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  WORD SCRAMBLE")
    print("="*50)
    print("\nWelcome to Word Scramble!")
    print("\nRules:")
    print("  1. Unscramble the letters to find the word")
    print("  2. Get hints by revealing letters")
    print("  3. Fewer hints = more points")
    print("  4. Choose your difficulty level")
    print("\nPython Concepts: Strings, Lists, Random, Timer")


def select_difficulty() -> str:
    """Let player choose difficulty.
    
    Returns:
        Selected difficulty name
    """
    print("\n  Choose difficulty:")
    difficulties = list(WORD_LISTS.keys())
    
    for i, diff in enumerate(difficulties, 1):
        print(f"  {i}. {diff}")
    
    while True:
        choice = input(f"\nEnter choice (1-{len(difficulties)}): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(difficulties):
                return difficulties[idx]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")


def scramble_word(word: str) -> str:
    """Scramble the letters of a word.
    
    Args:
        word: Original word
        
    Returns:
        Scrambled version of the word
    """
    letters = list(word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    
    # Make sure scrambled is different from original
    while scrambled == word and len(word) > 1:
        random.shuffle(letters)
        scrambled = ''.join(letters)
    
    return scrambled


def reveal_hint(word: str, revealed: list[bool]) -> str:
    """Reveal an unrevealed letter as hint.
    
    Args:
        word: Original word
        revealed: List tracking which positions are revealed
        
    Returns:
        Hint message
    """
    unrevealed = [i for i, r in enumerate(revealed) if not r]
    
    if not unrevealed:
        return "No more hints available!"
    
    pos = random.choice(unrevealed)
    revealed[pos] = True
    
    return f"Hint: Position {pos + 1} is '{word[pos]}'"


def display_word_progress(word: str, revealed: list[bool]) -> str:
    """Display word with revealed and hidden letters.
    
    Args:
        word: Original word
        revealed: List tracking which positions are revealed
        
    Returns:
        Formatted word string
    """
    display = ""
    for i, letter in enumerate(word):
        if revealed[i]:
            display += letter.upper() + " "
        else:
            display += "_ "
    return display


def play_round(difficulty: str) -> tuple[int, str]:
    """Play one round of Word Scramble.
    
    Args:
        difficulty: Selected difficulty level
        
    Returns:
        Tuple of (points earned, original word)
    """
    word = random.choice(WORD_LISTS[difficulty])
    scrambled = scramble_word(word)
    revealed = [False] * len(word)
    hints_used = 0
    guesses = 0
    
    print(f"\n  Difficulty: {difficulty}")
    print(f"  Word length: {len(word)} letters")
    print(f"\n  Scrambled: {scrambled.upper()}")
    print(f"  Progress:  {display_word_progress(word, revealed)}")
    
    start_time = time.time()
    
    while True:
        print(f"\n  Options:")
        print("  1. Guess the word")
        print("  2. Get a hint")
        print("  3. Give up")
        
        choice = input("\nYour choice (1/2/3): ").strip()
        
        if choice == '1':
            guess = input("Enter your guess: ").strip().lower()
            guesses += 1
            
            if guess == word:
                elapsed = time.time() - start_time
                points = calculate_points(difficulty, hints_used, elapsed, guesses)
                
                print(f"\n  🎉 CORRECT! The word was: {word.upper()}")
                print(f"  ⏱️  Time: {elapsed:.1f} seconds")
                print(f"  💡 Hints used: {hints_used}")
                print(f"  🎯 Points earned: {points}")
                
                return points, word
            
            else:
                print(f"  ❌ Wrong! Try again.")
        
        elif choice == '2':
            hint = reveal_hint(word, revealed)
            hints_used += 1
            print(f"\n  {hint}")
            print(f"  Progress: {display_word_progress(word, revealed)}")
        
        elif choice == '3':
            print(f"\n  The word was: {word.upper()}")
            return 0, word
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def calculate_points(difficulty: str, hints: int, time_taken: float, guesses: int) -> int:
    """Calculate points based on performance.
    
    Args:
        difficulty: Difficulty level
        hints: Number of hints used
        time_taken: Time in seconds
        guesses: Number of guesses made
        
    Returns:
        Points earned
    """
    # Base points by difficulty
    base_points = {'Easy': 10, 'Medium': 20, 'Hard': 30}
    points = base_points.get(difficulty, 10)
    
    # Penalty for hints
    points -= hints * 3
    
    # Bonus for speed (under 10 seconds)
    if time_taken < 10:
        points += 10
    elif time_taken < 20:
        points += 5
    
    # Penalty for multiple guesses
    if guesses > 1:
        points -= (guesses - 1) * 2
    
    return max(points, 1)  # Minimum 1 point


def main() -> None:
    """Main game loop."""
    display_welcome()
    
    total_points = 0
    words_played = []
    
    while True:
        difficulty = select_difficulty()
        points, word = play_round(difficulty)
        
        total_points += points
        words_played.append({'word': word, 'difficulty': difficulty, 'points': points})
        
        print(f"\n  📊 Total Points: {total_points}")
        
        play_again = input("\nPlay another word? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            break
    
    # Final summary
    print("\n" + "="*50)
    print("  FINAL RESULTS")
    print("="*50)
    print(f"\n  Words played: {len(words_played)}")
    print(f"  Total points: {total_points}")
    
    if words_played:
        best = max(words_played, key=lambda x: x['points'])
        print(f"  Best word: {best['word'].upper()} ({best['points']} points)")
    
    print("\nThanks for playing Word Scramble!")
    print("See you next time!")


if __name__ == "__main__":
    main()

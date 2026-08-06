# Hangman Game

## Description
The classic word-guessing game! Choose a category, guess letters one at a time, and try to reveal the hidden word before the hangman is complete. Features multiple word categories and ASCII art!

## How to Play
1. Run the game: `python game.py`
2. Choose a word category (Animals, Fruits, Countries, Colors, Sports)
3. Guess one letter at a time
4. Correct guesses reveal letters in the word
5. Wrong guesses build the hangman (6 max)
6. Guess the word before the hangman is complete!

## Python Concepts Learned
- **Lists**: Storing word collections
- **Sets**: Tracking unique guessed letters
- **Strings**: String manipulation and methods
- **Random Module**: Selecting random words
- **While Loops**: Game loop and input validation
- **ASCII Art**: Visual hangman display
- **Game State**: Managing game progress

## Word Categories
| Category | Example Words |
|----------|---------------|
| Animals | elephant, penguin, dolphin |
| Fruits | strawberry, pineapple, mango |
| Countries | australia, finland, iceland |
| Colors | crimson, turquoise, emerald |
| Sports | basketball, swimming, cycling |

## Sample Output
```
==================================================
  HANGMAN
==================================================

Welcome to Hangman!

Rules:
  1. Guess one letter at a time
  2. You have 6 wrong guesses allowed
  3. Each wrong guess adds to the hangman
  4. Guess the word before the hangman is complete!

  Choose a category:
  1. Animals
  2. Fruits
  3. Countries
  4. Colors
  5. Sports

Enter choice (1-5): 1

  Category: Animals
  Word has 8 letters. Good luck!

      ------
      |    |
      |
      |
      |
      |
    =========

  Word: _ _ _ _ _ _ _ _
  Wrong guesses: 0/6
  Guessed: 

Enter a letter (or 'q' to quit): e

  ✅ 'e' is in the word!

      ------
      |    |
      |
      |
      |
      |
    =========

  Word: _ _ _ _ _ _ _ _
  Wrong guesses: 0/6
  Guessed: e

Enter a letter (or 'q' to quit): x

  ❌ 'x' is not in the word!

      ------
      |    |
      |    O
      |
      |
      |
    =========

  Word: _ _ _ _ _ _ _ _
  Wrong guesses: 1/6
  Guessed: e, x

Enter a letter (or 'q' to quit): l

  ✅ 'l' is in the word!

      ------
      |    |
      |    O
      |
      |
      |
    =========

  Word: _ _ _ l _ _ _ _
  Wrong guesses: 1/6
  Guessed: e, l, x

  ... (continues until word is guessed) ...

**************************************************
  🎉 CONGRATULATIONS! You guessed the word!
  The word was: ELEPHANT
  Wrong guesses: 2/6
**************************************************
```

## Code Structure
```
hangman/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Show game rules
- `select_category()`: Let player choose word category
- `select_word(category)`: Randomly select a word
- `display_game_state(word, guessed, wrong)`: Show hangman and progress
- `get_guess(guessed_letters)`: Get valid letter guess
- `check_win(word, guessed)`: Check if player won
- `play_round()`: Play one complete round
- `main()`: Main game loop

## Error Handling
- Validates category selection input
- Validates letter input (single character, a-z)
- Prevents duplicate letter guesses
- Handles quit command at any prompt

## Future Enhancements
- [ ] Add more word categories
- [ ] Implement difficulty levels (more/fewer guesses)
- [ ] Add hint system (reveal a letter)
- [ ] Track wins/losses across rounds
- [ ] Add timed mode
- [ ] Create multiplayer mode
- [ ] Add custom word lists

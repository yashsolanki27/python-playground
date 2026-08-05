# Hangman Game

## Description
The classic Hangman word guessing game. Guess letters to reveal the hidden word before the hangman is complete!

## How to Play
1. Run the game: `python game.py`
2. The computer selects a random word from a category
3. Guess one letter at a time
4. Correct letters are revealed in the word
5. Wrong guesses add to the hangman drawing
6. Win by guessing the word before 6 wrong guesses!

## Python Concepts Learned
- **Lists**: Storing characters and tracking guesses
- **Strings**: String manipulation and formatting
- **Sets**: Tracking unique guessed letters
- **Loops**: Game loop and input validation
- **Conditionals**: Win/lose conditions
- **Random Module**: Selecting random words
- **ASCII Art**: Visual hangman display
- **Dictionaries**: Word categories organization

## Word Categories
- Animals (elephant, giraffe, penguin, etc.)
- Fruits (strawberry, blueberry, pineapple, etc.)
- Countries (australia, brazil, canada, etc.)
- Colors (scarlet, turquoise, magenta, etc.)
- Sports (basketball, volleyball, badminton, etc.)

## Sample Output
```
============================================================
 HANGMAN GAME
============================================================

Guess the word before the hangman is complete!
You have 6 incorrect guesses allowed.
Type a single letter to guess.
Type 'quit' to exit the game.

Category: ANIMALS
Word has 8 letters

      ------
      |    |
      |
      |
      |
      |

Word: _ _ _ _ _ _ _ _

Enter your guess: e
✓ Good guess! 'e' is in the word!

Word: _ _ _ _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: e

Enter your guess: a
✗ Sorry, 'a' is not in the word!

      ------
      |    |
      |    O
      |
      |
      |

Word: _ _ _ _ _ _ _ _
Wrong guesses: 1/6
Guessed letters: a, e

Enter your guess: l
✓ Good guess! 'l' is in the word!

Word: _ _ _ _ _ _ l _
Wrong guesses: 1/6
Guessed letters: a, e, l

... (continues until word is guessed or hangman complete)

============================================================
 CONGRATULATIONS!
 You guessed the word: ELEPHANT
============================================================

      ------
      |    |
      |    O
      |   /|\
      |   /
      |

--- Statistics ---
Games played: 1
Games won: 1
Win rate: 100.0%

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye!
```

## Code Structure
```
hangman/
├── game.py           # Main game file (180 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Shows game instructions
- `display_hangman(wrong_guesses)`: Shows ASCII art
- `display_word_state(word, guessed_letters)`: Shows word progress
- `get_random_word()`: Selects random word and category
- `get_valid_guess(guessed_letters)`: Gets valid letter input
- `play_game()`: Main game loop
- `main()`: Entry point

## Game Features
- 6 hangman stages (progressive drawing)
- 5 word categories with 7 words each
- Win/loss tracking
- Win rate calculation
- Input validation
- Graceful exit with 'quit'

## Error Handling
- Validates single letter input
- Checks for already guessed letters
- Ensures alphabetic input only
- Handles 'quit' command

## Future Enhancements
- [ ] Add more word categories
- [ ] Implement hint system
- [ ] Add difficulty levels (more/fewer guesses)
- [ ] Create GUI version
- [ ] Add sound effects
- [ ] Implement multiplayer mode
- [ ] Add custom word lists
- [ ] Track best times
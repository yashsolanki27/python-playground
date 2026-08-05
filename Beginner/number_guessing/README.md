# Number Guessing Game

## Description
A classic number guessing game where the computer generates a random number and the player tries to guess it within a limited number of attempts.

## How to Play
1. Run the game: `python game.py`
2. The computer picks a random number between 1 and 100
3. Enter your guess when prompted
4. Receive hints: "too high" or "too low"
5. You have 7 attempts to guess correctly
6. Win by guessing the number!

## Python Concepts Learned
- **Variables**: Storing numbers, strings, and user input
- **Loops**: Using `while` loops for game loop and input validation
- **Conditionals**: `if/elif/else` statements for game logic
- **Random Module**: Generating random numbers with `random.randint()`
- **Functions**: Breaking code into reusable functions
- **Error Handling**: Using `try/except` for input validation
- **Type Conversion**: Converting string input to integers

## Sample Output
```
==================================================
 Welcome to the Number Guessing Game!
==================================================

I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.
After each guess, I'll tell you if it's too high or too low.

Attempt 1/7 - Enter your guess: 50
Your guess is too low!
You have 6 attempts remaining.

Attempt 2/7 - Enter your guess: 75
Your guess is too high!
You have 5 attempts remaining.

Attempt 3/7 - Enter your guess: 62
Your guess is too low!
You have 4 attempts remaining.

Attempt 4/7 - Enter your guess: 68
Your guess is too high!
You have 3 attempts remaining.

Attempt 5/7 - Enter your guess: 65

==================================================
 Congratulations! You guessed it!
 The number was 65
 You got it in 5 attempts!
==================================================

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye!
```

## Code Structure
```
number_guessing/
├── game.py           # Main game file (80 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Shows game instructions
- `get_user_guess(attempt)`: Gets and validates user input
- `check_guess(guess, target)`: Compares guess with secret number
- `play_game()`: Main game logic
- `main()`: Entry point with play again loop

## Error Handling
- Validates input is a number
- Ensures input is between 1-100
- Handles invalid input gracefully
- Provides clear error messages

## Future Enhancements
- [ ] Add difficulty levels (Easy: 1-50, Medium: 1-100, Hard: 1-200)
- [ ] Track high scores across sessions
- [ ] Add a hint system (divisible by X, even/odd, etc.)
- [ ] Create GUI version with tkinter
- [ ] Add sound effects
- [ ] Implement adaptive difficulty based on player performance
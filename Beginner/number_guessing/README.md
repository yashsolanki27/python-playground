# Number Guessing Game

## Description
A simple number guessing game where you try to guess a randomly generated number within a limited number of attempts. Choose your difficulty level and test your guessing skills!

## How to Play
1. Run the game: `python game.py`
2. Select a difficulty level (Easy/Medium/Hard)
3. Guess numbers within the given range
4. Use hints ("Too high!" / "Too low!") to narrow down
5. Try to guess the number before running out of attempts

## Python Concepts Learned
- **Variables**: Storing game state (secret number, attempts, difficulty)
- **Random Module**: Generating random numbers
- **While Loops**: Game loop and input validation
- **If/Elif/Else**: Comparing guesses and controlling flow
- **User Input**: Getting and validating player input
- **f-strings**: formatted output messages
- **Functions**: Modular code organization

## Difficulty Levels
| Level | Range | Attempts |
|-------|-------|----------|
| Easy | 1-50 | 10 |
| Medium | 1-100 | 7 |
| Hard | 1-200 | 5 |

## Sample Output
```
==================================================
  NUMBER GUESSING GAME
==================================================

Welcome to the Number Guessing Game!

Rules:
  1. The computer picks a random number
  2. You try to guess it within limited attempts
  3. You'll get hints after each guess
  4. Choose your difficulty level

Select Difficulty:
1. Easy   (1-50,  10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-200, 5 attempts)

Enter choice (1/2/3): 2

==================================================
  NUMBER GUESSING GAME - MEDIUM
==================================================
I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

--- Attempts remaining: 7 ---

Enter your guess (1-100) or 'q' to quit: 50
Too low! Try a higher number.

--- Attempts remaining: 6 ---

Enter your guess (1-100) or 'q' to quit: 75
Too high! Try a lower number.

--- Attempts remaining: 5 ---

Enter your guess (1-100) or 'q' to quit: 62
Too low! Try a higher number.

--- Attempts remaining: 4 ---

Enter your guess (1-100) or 'q' to quit: 68
Too high! Try a lower number.

--- Attempts remaining: 3 ---

Enter your guess (1-100) or 'q' to quit: 65
Too low! Try a higher number.

--- Attempts remaining: 2 ---

Enter your guess (1-100) or 'q' to quit: 67

**************************************************
  CONGRATULATIONS! You guessed it!
  The number was 67
  You took 6 attempt(s)
  Good job!
**************************************************
```

## Code Structure
```
number_guessing/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `get_difficulty()`: Get player's difficulty choice
- `get_range(difficulty)`: Return number range for difficulty
- `get_guess(min, max)`: Get and validate player's guess
- `play_round()`: Play one complete round
- `display_welcome()`: Show game rules
- `main()`: Main game loop

## Error Handling
- Validates difficulty menu input
- Validates guess is a number within range
- Handles non-numeric input gracefully
- Allows player to quit anytime with 'q'

## Future Enhancements
- [ ] Add score tracking across rounds
- [ ] Implement hint system showing range
- [ ] Add time-based scoring
- [ ] Create multiplayer mode
- [ ] Add sound effects
- [ ] Implement persistent high scores

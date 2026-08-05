# Rock Paper Scissors Game

## Description
The classic Rock Paper Scissors hand game where you play against the computer. Track your wins and see who comes out on top!

## How to Play
1. Run the game: `python game.py`
2. Type 'rock', 'paper', or 'scissors' when prompted
3. Computer makes a random choice
4. Winner is determined by classic rules
5. Track your score across multiple rounds
6. Type 'quit' to exit

## Python Concepts Learned
- **If-Else Statements**: Game logic and win conditions
- **Random Module**: Computer's random choice with `random.choice()`
- **String Comparison**: Comparing user input with valid choices
- **Loops**: Game loop and input validation loop
- **Score Tracking**: Using variables to track wins/losses
- **Input Validation**: Ensuring valid user input
- **Dictionaries**: Mapping choices to display text

## Sample Output
```
==================================================
 Rock Paper Scissors!
==================================================

Rules:
  Rock crushes Scissors
  Scissors cuts Paper
  Paper covers Rock

Type 'rock', 'paper', or 'scissors' to play.
Type 'quit' to exit the game.

Enter your choice: rock

You chose: 🪨 Rock
Computer chose: ✂️  Scissors
------------------------------
 You win this round!

==============================
 SCOREBOARD (Games: 1)
==============================
 Player:    1 wins
 Computer:  0 wins
 Ties:      0
==============================

Enter your choice: paper

You chose: 📄 Paper
Computer chose: 📄 Paper
------------------------------
 It's a tie!

==============================
 SCOREBOARD (Games: 2)
==============================
 Player:    1 wins
 Computer:  0 wins
 Ties:      1
==============================

Enter your choice: quit

==================================================
 FINAL SCORE
==================================================
==============================
 SCOREBOARD (Games: 2)
==============================
 Player:    1 wins
 Computer:  0 wins
 Ties:      1
==============================

🏆 Congratulations! You are the overall winner!

Thanks for playing! Goodbye!
```

## Code Structure
```
rock_paper_scissors/
├── game.py           # Main game file (120 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Shows game rules
- `get_player_choice()`: Gets and validates player input
- `get_computer_choice()`: Generates random computer choice
- `determine_winner(player, computer)`: Implements win logic
- `display_result(player, computer, result)`: Shows round outcome
- `display_score(player_wins, computer_wins, ties)`: Shows scoreboard
- `play_game()`: Main game loop
- `main()`: Entry point with play again loop

## Win Conditions
- **Rock** crushes **Scissors**
- **Scissors** cuts **Paper**
- **Paper** covers **Rock**

## Error Handling
- Validates input is a valid choice
- Handles case-insensitive input
- Provides clear error messages
- Graceful exit with 'quit' command

## Future Enhancements
- [ ] Add best-of-N matches mode
- [ ] Add Lizard and Spock variations
- [ ] Track win streaks
- [ ] Add difficulty levels (smarter AI)
- [ ] Create GUI version
- [ ] Add animated hand gestures
- [ ] Implement online multiplayer
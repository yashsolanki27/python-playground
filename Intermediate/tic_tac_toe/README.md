# Tic-Tac-Toe Game

## Description
The classic two-player Tic-Tac-Toe game! Take turns with a friend to place X and O on a 3x3 grid. First to get three in a row wins!

## How to Play
1. Run the game: `python game.py`
2. Players take turns (X always goes first)
3. Enter row and column numbers (1-3) to place your mark
4. First to get 3 in a row (horizontal, vertical, or diagonal) wins
5. If all 9 squares fill with no winner, it's a draw

## Python Concepts Learned
- **2D Lists**: Representing the 3x3 game board
- **Nested Loops**: Displaying the board grid
- **Win Detection**: Checking rows, columns, and diagonals
- **Turn Management**: Switching between X and O players
- **Input Validation**: Ensuring valid moves
- **Game State**: Tracking moves and board status

## Board Layout
```
     1   2   3
   +---+---+---+
 1 |   |   |   |
   +---+---+---+
 2 |   |   |   |
   +---+---+---+
 3 |   |   |   |
   +---+---+---+
```

## Win Conditions
- **Rows**: Any complete horizontal line
- **Columns**: Any complete vertical line
- **Diagonals**: Either diagonal line

## Sample Output
```
==================================================
  TIC-TAC-TOE
==================================================

Welcome to Tic-Tac-Toe!

Rules:
  1. Players take turns (X goes first)
  2. Enter row and column (1-3)
  3. First to get 3 in a row wins!
  4. Rows, columns, and diagonals count

     1   2   3
   +---+---+---+
 1 |   |   |   |
   +---+---+---+
 2 |   |   |   |
   +---+---+---+
 3 |   |   |   |
   +---+---+---+

Player X's turn - Enter row and column (e.g., 1 2): 2 2

     1   2   3
   +---+---+---+
 1 |   |   |   |
   +---+---+---+
 2 |   | X |   |
   +---+---+---+
 3 |   |   |   |
   +---+---+---+

Player O's turn - Enter row and column (e.g., 1 2): 1 1

     1   2   3
   +---+---+---+
 1 | O |   |   |
   +---+---+---+
 2 |   | X |   |
   +---+---+---+
 3 |   |   |   |
   +---+---+---+

  ... (game continues) ...

  🎉 Player X WINS! Congratulations!
  Won in 5 moves!
```

## Code Structure
```
tic_tac_toe/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `create_board()`: Initialize empty 3x3 board
- `display_board(board)`: Print the board with grid lines
- `display_welcome()`: Show game rules
- `get_move(board, player)`: Get valid move from player
- `check_winner(board, player)`: Check all win conditions
- `is_board_full(board)`: Check for draw condition
- `play_round()`: Play one complete game
- `main()`: Main game loop

## Error Handling
- Validates row/column input is numeric
- Validates numbers are between 1-3
- Prevents placing on occupied squares
- Handles invalid input formats

## Future Enhancements
- [ ] Add computer AI opponent
- [ ] Implement 4x4 or 5x5 boards
- [ ] Add score tracking across rounds
- [ ] Create network multiplayer
- [ ] Add animation effects
- [ ] Implement undo move feature

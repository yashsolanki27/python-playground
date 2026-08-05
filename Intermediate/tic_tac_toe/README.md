# Tic-Tac-Toe Game

## Description
The classic Tic-Tac-Toe board game for 2 players. Take turns placing X's and O's on a 3x3 grid to get three in a row!

## How to Play
1. Run the game: `python game.py`
2. Player 1 uses X, Player 2 uses O
3. Take turns entering a position number (1-9)
4. First to get 3 marks in a row wins!
5. If all spaces are filled with no winner, it's a draw

## Python Concepts Learned
- **2D Lists**: Representing the game board as nested lists
- **Functions**: Breaking code into modular functions
- **Game State Management**: Tracking current player and board state
- **Win Condition Checking**: Logic to detect rows, columns, diagonals
- **Input Validation**: Ensuring valid position choices
- **Display Formatting**: Creating visual board representation

## Position Guide
```
  1 | 2 | 3 
 ---+---+---
  4 | 5 | 6 
 ---+---+---
  7 | 8 | 9 
```

## Sample Output
```
==================================================
 TIC-TAC-TOE
==================================================

Player 1: X | Player 2: O
Take turns placing your mark on the board.
Enter a number (1-9) to place your mark.
Type 'quit' to exit the game.

Position Guide:
  1 | 2 | 3 
 ---+---+---
  4 | 5 | 6 
 ---+---+---
  7 | 8 | 9 

==================================================
 NEW GAME
==================================================


     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
     |     |     


Player X's turn
Enter position (1-9): 5


     |     |     
     |     |     
_____|_____|_____
     |     |     
  X  |     |     
_____|_____|_____
     |     |     
     |     |     
     |     |     

Player O's turn
Enter position (1-9): 1


  O  |     |     
     |     |     
_____|_____|_____
     |     |     
  X  |     |     
_____|_____|_____
     |     |     
     |     |     
     |     |     

... (continues until win or draw)

==================================================
 PLAYER X WINS!
==================================================

--- Statistics ---
Games played: 1
X wins: 1
O wins: 0
Draws: 0

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye!
```

## Code Structure
```
tic_tac_toe/
├── game.py           # Main game file (200 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `create_board()`: Initializes empty 3x3 board
- `display_board(board)`: Shows current board state
- `display_position_guide()`: Shows position numbers
- `get_position_choice(board)`: Gets valid position input
- `make_move(board, position, player)`: Places mark on board
- `check_winner(board)`: Checks for win conditions
- `is_board_full(board)`: Checks for draw condition
- `play_game()`: Main game loop
- `main()`: Entry point

## Win Conditions
- **Rows**: Three matching marks in any row
- **Columns**: Three matching marks in any column
- **Diagonals**: Three matching marks on either diagonal

## Error Handling
- Validates position is a number (1-9)
- Checks if position is already taken
- Handles 'quit' command at any time
- Prevents invalid moves

## Future Enhancements
- [ ] Add AI opponent (easy/medium/hard)
- [ ] Add score tracking across sessions
- [ ] Create GUI version with tkinter
- [ ] Add 4x4 and 5x5 board options
- [ ] Implement online multiplayer
- [ ] Add animation effects
- [ ] Create tournament mode
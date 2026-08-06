"""
Tic-Tac-Toe Game
A classic two-player game to learn 2D lists, game logic, and win detection.

How to Play:
1. Players take turns placing X or O on a 3x3 grid
2. First to get 3 in a row (horizontal, vertical, or diagonal) wins
3. If all 9 squares are filled with no winner, it's a draw

Python Concepts:
- 2D lists for the game board
- Nested loops for board display
- Win condition checking
- Player turn management
- Input validation
- Game state tracking
"""

import os


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_board() -> list[list[str]]:
    """Create an empty 3x3 game board.
    
    Returns:
        3x3 list with empty spaces
    """
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board: list[list[str]]) -> None:
    """Display the game board with grid lines.
    
    Args:
        board: 3x3 game board
    """
    print("\n")
    print("     1   2   3")
    print("   +---+---+---+")
    
    for i, row in enumerate(board):
        print(f" {i+1} | {row[0]} | {row[1]} | {row[2]} |")
        print("   +---+---+---+")
    
    print()


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  TIC-TAC-TOE")
    print("="*50)
    print("\nWelcome to Tic-Tac-Toe!")
    print("\nRules:")
    print("  1. Players take turns (X goes first)")
    print("  2. Enter row and column (1-3)")
    print("  3. First to get 3 in a row wins!")
    print("  4. Rows, columns, and diagonals count")
    print("\nPython Concepts: 2D Lists, Win Detection, Game Logic")


def get_move(board: list[list[str]], player: str) -> tuple[int, int]:
    """Get a valid move from the current player.
    
    Args:
        board: Current game board
        player: Current player symbol (X or O)
        
    Returns:
        Tuple of (row, column) indices
    """
    while True:
        move = input(f"Player {player}'s turn - Enter row and column (e.g., 1 2): ").strip()
        
        parts = move.split()
        if len(parts) != 2:
            print("Invalid input. Enter two numbers separated by space.")
            continue
        
        try:
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Numbers must be between 1 and 3.")
                continue
            
            if board[row][col] != ' ':
                print("That spot is already taken! Try again.")
                continue
            
            return row, col
            
        except ValueError:
            print("Invalid input. Please enter numbers.")


def check_winner(board: list[list[str]], player: str) -> bool:
    """Check if the given player has won.
    
    Args:
        board: Current game board
        player: Player symbol to check
        
    Returns:
        True if player has won, False otherwise
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def is_board_full(board: list[list[str]]) -> bool:
    """Check if the board is completely filled.
    
    Args:
        board: Current game board
        
    Returns:
        True if no empty spaces, False otherwise
    """
    return all(cell != ' ' for row in board for cell in row)


def play_round() -> bool:
    """Play one round of Tic-Tac-Toe.
    
    Returns:
        True if player wants to play again
    """
    board = create_board()
    current_player = 'X'
    moves = 0
    
    clear_screen()
    display_welcome()
    display_board(board)
    
    while True:
        row, col = get_move(board, current_player)
        
        board[row][col] = current_player
        moves += 1
        
        clear_screen()
        display_board(board)
        
        if check_winner(board, current_player):
            print(f"  🎉 Player {current_player} WINS! Congratulations!")
            print(f"  Won in {moves} moves!")
            return False
        
        if is_board_full(board):
            print("  🤝 It's a DRAW! Good game!")
            return False
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


def main() -> None:
    """Main game loop."""
    while True:
        play_round()
        
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Tic-Tac-Toe!")
            print("See you next time!")
            break


if __name__ == "__main__":
    main()

"""
Tic-Tac-Toe Game
A classic 2-player board game to learn 2D lists and game logic.

How to Play:
1. Player 1 is X, Player 2 is O
2. Players take turns placing their mark on a 3x3 grid
3. Enter a number (1-9) to place your mark
4. First to get 3 in a row wins!
5. If all spaces are filled with no winner, it's a draw!

Python Concepts:
- 2D lists (nested lists)
- Functions with return values
- Game state management
- Win condition checking
- Input validation
- Display formatting
"""

from typing import List, Optional, Tuple


def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 50)
    print(" TIC-TAC-TOE")
    print("=" * 50)
    print("\nPlayer 1: X | Player 2: O")
    print("Take turns placing your mark on the board.")
    print("Enter a number (1-9) to place your mark.")
    print("Type 'quit' to exit the game.\n")


def create_board() -> List[List[str]]:
    """
    Create an empty 3x3 game board.
    
    Returns:
        3x3 list with empty spaces
    """
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board: List[List[str]]):
    """
    Display the current game board.
    
    Args:
        board: 3x3 game board
    """
    print("\n")
    print("     |     |     ")
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")
    print("     |     |     ")
    print("\n")


def display_position_guide():
    """Display the position numbers for the board."""
    print("\nPosition Guide:")
    print("  1 | 2 | 3  ")
    print(" ---+---+---")
    print("  4 | 5 | 6  ")
    print(" ---+---+---")
    print("  7 | 8 | 9  ")
    print("\n")


def get_position_choice(board: List[List[str]]) -> Optional[int]:
    """
    Get valid position choice from player.
    
    Args:
        board: Current game board
        
    Returns:
        Position number (1-9) or None to quit
    """
    while True:
        choice = input("Enter position (1-9): ").strip()
        
        if choice.lower() == 'quit':
            return None
        
        try:
            pos = int(choice)
            if 1 <= pos <= 9:
                # Convert to row, col
                row = (pos - 1) // 3
                col = (pos - 1) % 3
                
                # Check if position is available
                if board[row][col] == ' ':
                    return pos
                else:
                    print("That position is already taken! Try again.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def make_move(board: List[List[str]], position: int, player: str) -> List[List[str]]:
    """
    Place a player's mark on the board.
    
    Args:
        board: Current game board
        position: Position number (1-9)
        player: 'X' or 'O'
        
    Returns:
        Updated game board
    """
    row = (position - 1) // 3
    col = (position - 1) % 3
    board[row][col] = player
    return board


def check_winner(board: List[List[str]]) -> Optional[str]:
    """
    Check if there's a winner.
    
    Args:
        board: Current game board
        
    Returns:
        'X', 'O', or None if no winner yet
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None


def is_board_full(board: List[List[str]]) -> bool:
    """
    Check if the board is completely filled.
    
    Args:
        board: Current game board
        
    Returns:
        True if board is full, False otherwise
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game():
    """Main game function."""
    display_welcome()
    display_position_guide()
    
    # Game statistics
    games_played = 0
    x_wins = 0
    o_wins = 0
    draws = 0
    
    while True:
        # Initialize game
        board = create_board()
        current_player = 'X'
        game_over = False
        
        print(f"\n{'=' * 50}")
        print(f" NEW GAME")
        print(f"{'=' * 50}")
        
        display_board(board)
        
        # Game loop
        while not game_over:
            print(f"Player {current_player}'s turn")
            
            # Get position choice
            position = get_position_choice(board)
            
            if position is None:
                print("\nThanks for playing! Goodbye!")
                return
            
            # Make the move
            board = make_move(board, position, current_player)
            display_board(board)
            
            # Check for winner
            winner = check_winner(board)
            if winner:
                games_played += 1
                if winner == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
                
                print(f"\n{'=' * 50}")
                print(f" PLAYER {winner} WINS!")
                print(f"{'=' * 50}")
                game_over = True
            elif is_board_full(board):
                games_played += 1
                draws += 1
                
                print(f"\n{'=' * 50}")
                print(f" IT'S A DRAW!")
                print(f"{'=' * 50}")
                game_over = True
            else:
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
        
        # Display statistics
        print(f"\n--- Statistics ---")
        print(f"Games played: {games_played}")
        print(f"X wins: {x_wins}")
        print(f"O wins: {o_wins}")
        print(f"Draws: {draws}")
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            break
        
        print("\n" + "=" * 50)
        print(" Starting new game...")
        print("=" * 50 + "\n")


def main():
    """Main entry point."""
    play_game()


if __name__ == "__main__":
    main()
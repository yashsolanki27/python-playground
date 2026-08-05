import streamlit as st
import random

st.set_page_config(
    page_title="Python Learning Games",
    page_icon="🎮",
    layout="wide"
)

WORD_CATEGORIES = {
    "animals": ["elephant", "giraffe", "penguin", "dolphin", "cheetah", "kangaroo", "flamingo"],
    "fruits": ["strawberry", "blueberry", "pineapple", "watermelon", "raspberry", "blackberry"],
    "countries": ["australia", "brazil", "canada", "denmark", "egypt", "france", "germany"],
    "colors": ["scarlet", "turquoise", "magenta", "crimson", "emerald", "sapphire", "amethyst"],
    "sports": ["basketball", "volleyball", "badminton", "swimming", "cycling", "football"]
}

HANGMAN_STAGES = [
    """
      ------
      |    |
      |
      |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    """
]

def main():
    st.title("Python Learning Games")
    st.markdown("---")

    game = st.sidebar.selectbox(
        "Select a Game",
        ["Home", "Hangman", "Tic-Tac-Toe"]
    )

    if game == "Home":
        show_home()
    elif game == "Hangman":
        show_hangman()
    elif game == "Tic-Tac-Toe":
        show_tic_tac_toe()

def show_home():
    st.header("Welcome!")
    st.write("Choose a game from the sidebar to start playing.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hangman")
        st.write("Guess the word letter by letter before the hangman is complete!")
        st.write("**Concepts:** Lists, strings, loops, conditionals")
        st.write("**Difficulty:** Intermediate")

    with col2:
        st.subheader("Tic-Tac-Toe")
        st.write("Classic 2-player board game on a 3x3 grid!")
        st.write("**Concepts:** 2D lists, game logic, functions")
        st.write("**Difficulty:** Intermediate")

def show_hangman():
    st.header("Hangman Game")

    if 'hangman_word' not in st.session_state:
        category = random.choice(list(WORD_CATEGORIES.keys()))
        st.session_state.hangman_word = random.choice(WORD_CATEGORIES[category])
        st.session_state.hangman_category = category
        st.session_state.hangman_guessed = set()
        st.session_state.hangman_wrong = 0
        st.session_state.hangman_won = False
        st.session_state.hangman_lost = False

    col1, col2 = st.columns([2, 1])

    with col2:
        st.write(f"**Category:** {st.session_state.hangman_category.upper()}")
        st.write(f"**Wrong guesses:** {st.session_state.hangman_wrong}/6")
        st.code(HANGMAN_STAGES[st.session_state.hangman_wrong], language=None)

    with col1:
        display_word = ""
        for letter in st.session_state.hangman_word:
            if letter.lower() in st.session_state.hangman_guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        st.write(f"**Word:** {display_word}")

        if st.session_state.hangman_wrong >= 6:
            st.error(f"Game Over! The word was: **{st.session_state.hangman_word.upper()}**")
        elif all(l.lower() in st.session_state.hangman_guessed for l in st.session_state.hangman_word):
            st.success(f"Congratulations! You guessed: **{st.session_state.hangman_word.upper()}**")
            st.session_state.hangman_won = True
        else:
            guess = st.text_input("Enter a letter:", max_chars=1, key="hangman_input")
            if st.button("Guess", key="hangman_guess"):
                if guess:
                    guess = guess.lower()
                    if guess in st.session_state.hangman_guessed:
                        st.warning("Already guessed that letter!")
                    elif guess in st.session_state.hangman_word.lower():
                        st.session_state.hangman_guessed.add(guess)
                        st.rerun()
                    else:
                        st.session_state.hangman_guessed.add(guess)
                        st.session_state.hangman_wrong += 1
                        st.rerun()

        if st.button("New Game", key="hangman_new"):
            category = random.choice(list(WORD_CATEGORIES.keys()))
            st.session_state.hangman_word = random.choice(WORD_CATEGORIES[category])
            st.session_state.hangman_category = category
            st.session_state.hangman_guessed = set()
            st.session_state.hangman_wrong = 0
            st.session_state.hangman_won = False
            st.session_state.hangman_lost = False
            st.rerun()

def show_tic_tac_toe():
    st.header("Tic-Tac-Toe")

    if 'ttb_board' not in st.session_state:
        init_tic_tac_toe()

    col1, col2 = st.columns([2, 1])

    with col2:
        st.write(f"**Current Player:** {st.session_state.ttb_player}")
        if st.button("New Game", key="ttb_new"):
            init_tic_tac_toe()
            st.rerun()

    with col1:
        display_tic_tac_toe_board()

        winner = check_ttt_winner(st.session_state.ttb_board)
        if winner:
            st.success(f"Player {winner} wins!")
        elif is_ttt_full(st.session_state.ttb_board):
            st.info("It's a draw!")
        else:
            st.write(f"Player {st.session_state.ttb_player}'s turn")
            position = st.number_input(
                "Enter position (1-9):",
                min_value=1,
                max_value=9,
                step=1,
                key="ttb_pos"
            )
            if st.button("Make Move", key="ttb_move"):
                row = (position - 1) // 3
                col = (position - 1) % 3
                if st.session_state.ttb_board[row][col] == ' ':
                    st.session_state.ttb_board[row][col] = st.session_state.ttb_player
                    st.session_state.ttb_player = 'O' if st.session_state.ttb_player == 'X' else 'X'
                    st.rerun()
                else:
                    st.warning("Position taken!")

def init_tic_tac_toe():
    st.session_state.ttb_board = [[' ' for _ in range(3)] for _ in range(3)]
    st.session_state.ttb_player = 'X'

def display_tic_tac_toe_board():
    board = st.session_state.ttb_board
    st.write("---+---+---")
    for i, row in enumerate(board):
        display = " | ".join(cell if cell != ' ' else str(i*3+j+1) for j, cell in enumerate(row))
        st.write(f" {display} ")
        if i < 2:
            st.write("---+---+---")

def check_ttt_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_ttt_full(board):
    return all(cell != ' ' for row in board for cell in row)

if __name__ == "__main__":
    main()

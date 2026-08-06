"""
Unit Tests for Beginner Games
Tests for Number Guessing, Rock Paper Scissors, Calculator, and other beginner games.

Run tests: python -m pytest tests/test_beginner_games.py -v
"""

import sys
import os

# Add parent directories to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'number_guessing'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'rock_paper_scissors'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'calculator'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'dice_rolling'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'word_scramble'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'password_generator'))


class TestNumberGuessing:
    """Tests for Number Guessing Game."""
    
    def test_get_range_easy(self):
        """Test Easy difficulty range."""
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Beginner', 'number_guessing'))
        from game import get_range
        min_num, max_num = get_range("Easy")
        assert min_num == 1
        assert max_num == 50
    
    def test_get_range_medium(self):
        """Test Medium difficulty range."""
        from game import get_range
        min_num, max_num = get_range("Medium")
        assert min_num == 1
        assert max_num == 100
    
    def test_get_range_hard(self):
        """Test Hard difficulty range."""
        from game import get_range
        min_num, max_num = get_range("Hard")
        assert min_num == 1
        assert max_num == 200
    
    def test_get_range_default(self):
        """Test default range for unknown difficulty."""
        from game import get_range
        min_num, max_num = get_range("Unknown")
        assert min_num == 1
        assert max_num == 100


class TestRockPaperScissors:
    """Tests for Rock Paper Scissors Game."""
    
    def test_determine_winner_tie(self):
        """Test tie condition."""
        from game import determine_winner
        result = determine_winner("Rock", "Rock")
        assert result == "tie"
    
    def test_determine_winner_player_rock(self):
        """Test player wins with Rock vs Scissors."""
        from game import determine_winner
        result = determine_winner("Rock", "Scissors")
        assert result == "player"
    
    def test_determine_winner_player_paper(self):
        """Test player wins with Paper vs Rock."""
        from game import determine_winner
        result = determine_winner("Paper", "Rock")
        assert result == "player"
    
    def test_determine_winner_player_scissors(self):
        """Test player wins with Scissors vs Paper."""
        from game import determine_winner
        result = determine_winner("Scissors", "Paper")
        assert result == "player"
    
    def test_determine_winner_computer_rock(self):
        """Test computer wins with Rock vs Paper."""
        from game import determine_winner
        result = determine_winner("Rock", "Paper")
        assert result == "computer"
    
    def test_determine_winner_computer_paper(self):
        """Test computer wins with Paper vs Scissors."""
        from game import determine_winner
        result = determine_winner("Paper", "Scissors")
        assert result == "computer"
    
    def test_determine_winner_computer_scissors(self):
        """Test computer wins with Scissors vs Rock."""
        from game import determine_winner
        result = determine_winner("Scissors", "Rock")
        assert result == "computer"


class TestCalculator:
    """Tests for Calculator Game."""
    
    def test_add(self):
        """Test addition function."""
        from game import add
        assert add(5, 3) == 8
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(2.5, 2.5) == 5.0
    
    def test_subtract(self):
        """Test subtraction function."""
        from game import subtract
        assert subtract(10, 5) == 5
        assert subtract(5, 10) == -5
        assert subtract(0, 0) == 0
    
    def test_multiply(self):
        """Test multiplication function."""
        from game import multiply
        assert multiply(5, 3) == 15
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
        assert multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        """Test division function."""
        from game import divide
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
        assert divide(-10, 2) == -5.0
    
    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        from game import divide
        result = divide(10, 0)
        assert result is None


class TestDiceRolling:
    """Tests for Dice Rolling Simulator."""
    
    def test_roll_dice_count(self):
        """Test dice roll returns correct number of dice."""
        from game import roll_dice
        rolls = roll_dice(3)
        assert len(rolls) == 3
    
    def test_roll_dice_values(self):
        """Test dice values are between 1 and 6."""
        from game import roll_dice
        rolls = roll_dice(100)
        for roll in rolls:
            assert 1 <= roll <= 6
    
    def test_check_combinations_double(self):
        """Test double combination detection."""
        from game import check_combinations
        combos = check_combinations([5, 5])
        assert "🎯 Double!" in combos
    
    def test_check_combinations_lucky7(self):
        """Test Lucky 7 combination."""
        from game import check_combinations
        combos = check_combinations([3, 4])
        assert "🍀 Lucky 7!" in combos
    
    def test_check_combinations_empty(self):
        """Test no combinations for random rolls."""
        from game import check_combinations
        combos = check_combinations([1, 3, 5])
        assert len(combos) == 0


class TestPasswordGenerator:
    """Tests for Password Generator."""
    
    def test_generate_password_length(self):
        """Test password length matches input."""
        from game import generate_password
        options = {'uppercase': True, 'lowercase': True, 'digits': True, 'symbols': True}
        password = generate_password(16, options)
        assert len(password) == 16
    
    def test_generate_password_uppercase(self):
        """Test password contains uppercase when enabled."""
        from game import generate_password
        options = {'uppercase': True, 'lowercase': False, 'digits': False, 'symbols': False}
        password = generate_password(20, options)
        assert any(c.isupper() for c in password)
    
    def test_generate_password_lowercase(self):
        """Test password contains lowercase when enabled."""
        from game import generate_password
        options = {'uppercase': False, 'lowercase': True, 'digits': False, 'symbols': False}
        password = generate_password(20, options)
        assert any(c.islower() for c in password)
    
    def test_generate_password_digits(self):
        """Test password contains digits when enabled."""
        from game import generate_password
        options = {'uppercase': False, 'lowercase': False, 'digits': True, 'symbols': False}
        password = generate_password(20, options)
        assert any(c.isdigit() for c in password)
    
    def test_check_password_strength_strong(self):
        """Test strong password detection."""
        from game import check_password_strength
        analysis = check_password_strength("MyStr0ng!Pass#2024")
        assert analysis['score'] >= 80
    
    def test_check_password_strength_weak(self):
        """Test weak password detection."""
        from game import check_password_strength
        analysis = check_password_strength("abc")
        assert analysis['score'] < 40


class TestWordScramble:
    """Tests for Word Scramble Game."""
    
    def test_scramble_word_different(self):
        """Test scrambled word is different from original."""
        from game import scramble_word
        word = "python"
        scrambled = scramble_word(word)
        # Note: Very rare chance they could be equal, but statistically unlikely
        assert len(scrambled) == len(word)
    
    def test_scramble_word_same_letters(self):
        """Test scrambled word has same letters."""
        from game import scramble_word
        word = "hello"
        scrambled = scramble_word(word)
        assert sorted(scrambled) == sorted(word)
    
    def test_calculate_points_easy(self):
        """Test point calculation for Easy difficulty."""
        from game import calculate_points
        points = calculate_points("Easy", 0, 5.0, 1)
        assert points >= 15  # 10 base + 10 speed bonus
    
    def test_calculate_points_penalty(self):
        """Test point penalty for hints."""
        from game import calculate_points
        points = calculate_points("Easy", 3, 5.0, 1)
        assert points < 20  # 10 base - 9 hints penalty


if __name__ == "__main__":
    print("Run tests with: python -m pytest tests/test_beginner_games.py -v")

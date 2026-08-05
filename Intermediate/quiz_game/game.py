"""
Quiz Game
A multiple choice quiz game to learn dictionaries and score tracking.

How to Play:
1. Answer multiple choice questions
2. Type the letter (A, B, C, or D) for your answer
3. Get immediate feedback on correct/wrong answers
4. See your final score at the end
5. Play multiple rounds to improve your score!

Python Concepts:
- Dictionaries for question storage
- Lists for answer choices
- Score tracking
- Random question selection
- Input validation
- String formatting
- Loop control
"""

import random
from typing import List, Dict, Tuple


# Quiz questions organized by category
QUIZ_QUESTIONS = {
    "python_basics": [
        {
            "question": "What is the output of print(2 ** 3)?",
            "choices": ["A) 6", "B) 8", "C) 9", "D) 5"],
            "correct": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "choices": ["A) function", "B) define", "C) def", "D) func"],
            "correct": "C"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "choices": ["A) .python", "B) .py", "C) .pt", "D) .pyt"],
            "correct": "B"
        },
        {
            "question": "Which of these is a valid variable name?",
            "choices": ["A) 2name", "B) my-var", "C) _my_var", "D) my var"],
            "correct": "C"
        },
        {
            "question": "What does 'len()' function do?",
            "choices": ["A) Returns length", "B) Creates list", "C) Adds numbers", "D) Prints text"],
            "correct": "A"
        }
    ],
    "data_types": [
        {
            "question": "What type is the value: 'Hello'?",
            "choices": ["A) int", "B) float", "C) str", "D) bool"],
            "correct": "C"
        },
        {
            "question": "What is [1, 2, 3] in Python?",
            "choices": ["A) Tuple", "B) List", "C) Dictionary", "D) Set"],
            "correct": "B"
        },
        {
            "question": "What is the output of type(True)?",
            "choices": ["A) str", "B) int", "C) bool", "D) NoneType"],
            "correct": "C"
        },
        {
            "question": "Which is a dictionary?",
            "choices": ["A) [1, 2, 3]", "B) (1, 2, 3)", "C) {1: 'a', 2: 'b'}", "D) {1, 2, 3}"],
            "correct": "C"
        },
        {
            "question": "What is 3.14?",
            "choices": ["A) int", "B) float", "C) str", "D) complex"],
            "correct": "B"
        }
    ],
    "control_flow": [
        {
            "question": "Which is used for conditional statements?",
            "choices": ["A) for", "B) while", "C) if", "D) switch"],
            "correct": "C"
        },
        {
            "question": "What is the output of: x = 5; print(x if x > 3 else 'small')?",
            "choices": ["A) small", "B) 5", "C) True", "D) Error"],
            "correct": "B"
        },
        {
            "question": "Which loop is used for iterating over a sequence?",
            "choices": ["A) for loop", "B) while loop", "C) do loop", "D) repeat loop"],
            "correct": "A"
        },
        {
            "question": "What does 'break' do in a loop?",
            "choices": ["A) Pauses", "B) Exits", "C) Restarts", "D) Skips"],
            "correct": "B"
        },
        {
            "question": "Which is NOT a comparison operator?",
            "choices": ["A) ==", "B) !=", "C) <>", "D) >="],
            "correct": "C"
        }
    ]
}


def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 60)
    print(" QUIZ GAME")
    print("=" * 60)
    print("\nTest your Python knowledge!")
    print("Answer multiple choice questions (A, B, C, or D).")
    print("Get instant feedback on your answers.")
    print("See your final score at the end!\n")


def display_categories():
    """Display available quiz categories."""
    print("\nAvailable Categories:")
    print("-" * 40)
    categories = list(QUIZ_QUESTIONS.keys())
    for i, category in enumerate(categories, 1):
        # Format category name for display
        display_name = category.replace("_", " ").title()
        print(f"  {i}. {display_name}")
    print("-" * 40)
    return categories


def get_category_choice(categories: List[str]) -> str:
    """
    Get category choice from user.
    
    Args:
        categories: List of available categories
        
    Returns:
        Selected category key
    """
    while True:
        choice = input(f"\nEnter category number (1-{len(categories)}): ").strip()
        
        if choice.lower() == 'quit':
            return 'quit'
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(categories):
                return categories[index]
            else:
                print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_answer_choice() -> str:
    """
    Get answer choice from user.
    
    Returns:
        Answer letter (A, B, C, or D) or 'quit'
    """
    while True:
        answer = input("\nEnter your answer (A, B, C, or D): ").upper().strip()
        
        if answer == 'QUIT':
            return 'quit'
        
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        
        print("Invalid choice! Please enter A, B, C, or D.")


def display_question(question_num: int, total_questions: int, question: Dict):
    """
    Display a quiz question.
    
    Args:
        question_num: Current question number
        total_questions: Total questions in quiz
        question: Question dictionary
    """
    print(f"\n{'=' * 60}")
    print(f" Question {question_num}/{total_questions}")
    print(f"{'=' * 60}")
    print(f"\n{question['question']}\n")
    
    for choice in question['choices']:
        print(f"  {choice}")
    print()


def check_answer(selected: str, correct: str) -> bool:
    """
    Check if the selected answer is correct.
    
    Args:
        selected: User's selected answer
        correct: Correct answer
        
    Returns:
        True if correct, False otherwise
    """
    return selected == correct


def display_feedback(is_correct: bool, correct_answer: str):
    """
    Display answer feedback.
    
    Args:
        is_correct: Whether answer was correct
        correct_answer: The correct answer letter
    """
    if is_correct:
        print("\n✓ Correct! Well done!")
    else:
        print(f"\n✗ Incorrect! The correct answer was: {correct_answer}")


def display_results(score: int, total: int, category: str):
    """
    Display final quiz results.
    
    Args:
        score: Number of correct answers
        total: Total questions answered
        category: Quiz category
    """
    percentage = (score / total) * 100 if total > 0 else 0
    
    print(f"\n{'=' * 60}")
    print(f" QUIZ RESULTS")
    print(f"{'=' * 60}")
    print(f"\nCategory: {category.replace('_', ' ').title()}")
    print(f"Questions Answered: {total}")
    print(f"Correct Answers: {score}")
    print(f"Percentage: {percentage:.1f}%")
    
    # Performance message
    if percentage == 100:
        print("\n🏆 PERFECT SCORE! Excellent work!")
    elif percentage >= 80:
        print("\n🌟 Great job! You know your Python!")
    elif percentage >= 60:
        print("\n👍 Good effort! Keep practicing!")
    elif percentage >= 40:
        print("\n📚 Not bad! Room for improvement!")
    else:
        print("\n💪 Keep learning! You'll get better!")
    
    print(f"{'=' * 60}")


def play_quiz(category: str) -> Tuple[int, int]:
    """
    Play a quiz round.
    
    Args:
        category: Selected quiz category
        
    Returns:
        Tuple of (score, total_questions)
    """
    questions = QUIZ_QUESTIONS[category]
    score = 0
    total = len(questions)
    
    # Shuffle questions for variety
    shuffled_questions = random.sample(questions, total)
    
    print(f"\nStarting {category.replace('_', ' ').title()} Quiz!")
    print(f"You'll answer {total} questions.")
    input("Press Enter to start...")
    
    for i, question in enumerate(shuffled_questions, 1):
        # Display question
        display_question(i, total, question)
        
        # Get answer
        answer = get_answer_choice()
        
        if answer == 'quit':
            print(f"\nQuiz ended early. You answered {i-1} questions.")
            return score, i - 1
        
        # Check answer
        is_correct = check_answer(answer, question['correct'])
        
        # Update score
        if is_correct:
            score += 1
        
        # Display feedback
        display_feedback(is_correct, question['correct'])
        
        # Pause before next question
        if i < total:
            input("\nPress Enter for next question...")
    
    return score, total


def play_game():
    """Main quiz function."""
    display_welcome()
    
    # Game statistics
    total_games = 0
    total_correct = 0
    total_answered = 0
    
    while True:
        # Display categories
        categories = display_categories()
        
        # Get category choice
        category = get_category_choice(categories)
        
        if category == 'quit':
            break
        
        # Play quiz
        score, total = play_quiz(category)
        
        # Update statistics
        total_games += 1
        total_correct += score
        total_answered += total
        
        # Display results
        display_results(score, total, category)
        
        # Display overall statistics
        print(f"\n--- Overall Statistics ---")
        print(f"Quizzes completed: {total_games}")
        print(f"Total correct: {total_correct}/{total_answered}")
        if total_answered > 0:
            overall_percentage = (total_correct / total_answered) * 100
            print(f"Overall accuracy: {overall_percentage:.1f}%")
        
        # Ask to continue
        while True:
            continue_game = input("\nDo you want to take another quiz? (yes/no): ").lower().strip()
            if continue_game in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if continue_game in ['no', 'n']:
            break
        
        print("\n" + "=" * 60)
        print(" Starting new quiz...")
        print("=" * 60 + "\n")
    
    # Final summary
    print(f"\n{'=' * 60}")
    print(f" FINAL SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total quizzes completed: {total_games}")
    print(f"Total correct answers: {total_correct}")
    print(f"Total questions answered: {total_answered}")
    if total_answered > 0:
        final_percentage = (total_correct / total_answered) * 100
        print(f"Final accuracy: {final_percentage:.1f}%")
    print(f"{'=' * 60}")
    print("\nThanks for playing! Keep learning Python!")


def main():
    """Main entry point."""
    play_game()


if __name__ == "__main__":
    main()
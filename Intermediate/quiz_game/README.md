# Quiz Game

## Description
A multiple choice quiz game to test your Python knowledge! Choose from different categories and see how well you know Python basics.

## How to Play
1. Run the game: `python game.py`
2. Select a quiz category (Python Basics, Data Types, or Control Flow)
3. Answer 5 multiple choice questions per category
4. Type A, B, C, or D for your answer
5. Get immediate feedback on each answer
6. See your final score and accuracy percentage

## Python Concepts Learned
- **Dictionaries**: Storing questions and answers
- **Lists**: Managing answer choices
- **Random Module**: Shuffling questions
- **Score Tracking**: Using variables to track progress
- **Input Validation**: Ensuring valid answer choices
- **String Formatting**: Displaying results nicely
- **Loop Control**: Managing quiz flow

## Quiz Categories

### Python Basics
- Operators and expressions
- Function definitions
- File extensions
- Variable naming rules
- Built-in functions

### Data Types
- String, integer, float, boolean
- Lists vs tuples vs dictionaries
- Type checking
- Data type identification

### Control Flow
- Conditional statements
- Loops (for, while)
- Break and continue
- Comparison operators

## Sample Output
```
============================================================
 QUIZ GAME
============================================================

Test your Python knowledge!
Answer multiple choice questions (A, B, C, or D).
Get instant feedback on your answers.
See your final score at the end!

Available Categories:
----------------------------------------
  1. Python Basics
  2. Data Types
  3. Control Flow
----------------------------------------

Enter category number (1-3): 1

Starting Python Basics Quiz!
You'll answer 5 questions.
Press Enter to start...

============================================================
 Question 1/5
============================================================

What is the output of print(2 ** 3)?

  A) 6
  B) 8
  C) 9
  D) 5

Enter your answer (A, B, C, or D): B

✓ Correct! Well done!

Press Enter for next question...

============================================================
 Question 2/5
============================================================

Which keyword is used to define a function in Python?

  A) function
  B) define
  C) def
  D) func

Enter your answer (A, B, C, or D): C

✓ Correct! Well done!

... (continues for all questions)

============================================================
 QUIZ RESULTS
============================================================

Category: Python Basics
Questions Answered: 5
Correct Answers: 4
Percentage: 80.0%

🌟 Great job! You know your Python!
============================================================

--- Overall Statistics ---
Quizzes completed: 1
Total correct: 4/5
Overall accuracy: 80.0%

Do you want to take another quiz? (yes/no): no

============================================================
 FINAL SUMMARY
============================================================
Total quizzes completed: 1
Total correct answers: 4
Total questions answered: 5
Final accuracy: 80.0%
============================================================

Thanks for playing! Keep learning Python!
```

## Code Structure
```
quiz_game/
├── game.py           # Main game file (250 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Shows game instructions
- `display_categories()`: Lists available categories
- `get_category_choice(categories)`: Gets category selection
- `get_answer_choice()`: Gets answer input (A-D)
- `display_question(num, total, question)`: Shows question
- `check_answer(selected, correct)`: Validates answer
- `display_feedback(is_correct, correct)`: Shows feedback
- `display_results(score, total, category)`: Shows final results
- `play_quiz(category)`: Runs a quiz round
- `play_game()`: Main game loop
- `main()`: Entry point

## Question Format
Each question is a dictionary with:
```python
{
    "question": "Question text",
    "choices": ["A) Choice 1", "B) Choice 2", ...],
    "correct": "A"
}
```

## Features
- 3 categories with 5 questions each (15 total)
- Random question shuffling
- Immediate feedback
- Score tracking per category
- Overall statistics
- Performance messages based on score

## Error Handling
- Validates category selection (1-3)
- Validates answer choice (A-D)
- Handles 'quit' command
- Prevents invalid inputs

## Future Enhancements
- [ ] Add more categories (OOP, File I/O, etc.)
- [ ] Add difficulty levels (Easy, Medium, Hard)
- [ ] Load questions from external JSON file
- [ ] Add timer for each question
- [ ] Create GUI version
- [ ] Add multiplayer mode
- [ ] Track high scores
- [ ] Add question explanations
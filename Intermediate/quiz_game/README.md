# Quiz Game

## Description
A trivia quiz game with multiple categories! Test your knowledge in Science, History, Geography, and Technology. Answer multiple-choice questions and learn new facts!

## How to Play
1. Run the game: `python game.py`
2. Choose a quiz category
3. Answer 5 multiple-choice questions (A, B, C, or D)
4. Get immediate feedback with explanations
5. See your final score and review missed questions

## Python Concepts Learned
- **Dictionaries**: Organizing questions and answers
- **Lists**: Storing answer options
- **Random Module**: Shuffling question order
- **Loops**: Iterating through questions
- **Score Tracking**: Calculating and displaying results
- **Data Structures**: Nested dictionaries for quiz data

## Quiz Categories
| Category | Topics |
|----------|--------|
| Science | Chemistry, Biology, Physics |
| History | World Events, Famous People |
| Geography | Countries, Rivers, Oceans |
| Technology | Computers, Internet, Gadgets |

## Sample Output
```
==================================================
  QUIZ GAME
==================================================

Welcome to the Quiz Game!

Rules:
  1. Choose a category
  2. Answer 5 multiple-choice questions
  3. Get 1 point for each correct answer
  4. See your score and correct answers at the end

  Choose a category:
  1. Science (5 questions)
  2. History (5 questions)
  3. Geography (5 questions)
  4. Technology (5 questions)

Enter choice (1-4): 1

  Category: Science
  Questions: 5
  Let's begin!

  Question 1:
  What is the chemical symbol for water?
    A) H2O
    B) CO2
    C) NaCl
    D) O2

  Your answer (A/B/C/D): A

  ✅ Correct!
  📚 Water is H2O - two hydrogen atoms and one oxygen atom.

  📊 Score so far: 1/1

  Question 2:
  What planet is known as the Red Planet?
    A) Venus
    B) Mars
    C) Jupiter
    D) Saturn

  Your answer (A/B/C/D): B

  ✅ Correct!
  📚 Mars appears red due to iron oxide (rust) on its surface.

  📊 Score so far: 2/2

  ... (continues for all questions) ...

==================================================
  QUIZ RESULTS
==================================================

  Category: Science
  Score: 4/5 (80.0%)

  🌟 Excellent! You really know your stuff!

  📋 Questions you missed (1):

  Q: What gas do plants absorb from the atmosphere?
  A: C) Plants use CO2 for photosynthesis to make glucose.
```

## Code Structure
```
quiz_game/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Show game rules
- `select_category()`: Let player choose quiz topic
- `ask_question(data, num)`: Ask single question with feedback
- `play_quiz(category)`: Run through all questions
- `display_results(score, total, missed)`: Show final results
- `main()`: Main quiz loop

## Question Data Structure
```python
{
    'question': 'Question text here?',
    'options': ['A) Option 1', 'B) Option 2', 'C) Option 3', 'D) Option 4'],
    'answer': 'A',
    'explanation': 'Explanation of the correct answer.'
}
```

## Error Handling
- Validates category selection input
- Validates answer input (A-D only)
- Handles invalid menu choices
- Graceful quit option

## Future Enhancements
- [ ] Add more categories (Sports, Movies, Music)
- [ ] Implement difficulty levels
- [ ] Add timer for each question
- [ ] Create high score system
- [ ] Add multiplayer quiz mode
- [ ] Implement question weighting
- [ ] Add image-based questions

# Flashcard App

## Description
Create and study digital flashcards! Perfect for learning new concepts, vocabulary, or any subject. Track your progress and study in random order.

## How to Play
1. Run the game: `python game.py`
2. Add flashcards with question and answer
3. Study in random order
4. Track correct/incorrect answers
5. Data saves automatically

## Python Concepts Learned
- **Lists and Dictionaries**: Storing flashcard data
- **File I/O**: JSON persistence
- **Random Module**: Shuffling cards
- **Score Tracking**: Accuracy statistics

## Sample Output
```
==================================================
  📚 FLASHCARD APP
==================================================

  Options:
  1. Add flashcard
  2. View all flashcards
  3. Study mode
  4. Delete flashcard
  5. Quit

  Your choice (1-5): 1

  Add New Flashcard
  ------------------------------
  Front (question/term): What is Python?
  Back (answer/definition): A programming language
  Category (optional): Programming

  ✅ Flashcard added!

  Your choice (1-5): 3

  📖 STUDY MODE
  ------------------------------
  Press Enter to reveal answer
  Type 'y' if correct, 'n' if incorrect

  Card 1/5
  Category: Programming

  Q: What is Python?

  Press Enter to reveal answer...
  A: A programming language

  Correct? (y/n/q): y

  📊 Study Results:
  Correct: 5
  Incorrect: 0
  Accuracy: 100.0%
```

## Code Structure
```
flashcard_app/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add import/export feature
- [ ] Create flashcard decks
- [ ] Add spaced repetition
- [ ] Create image flashcards

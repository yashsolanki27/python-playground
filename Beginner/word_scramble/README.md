# Word Scramble Game

## Description
Unscramble letters to find the original word! Choose your difficulty level, use hints wisely, and score points based on your performance. A fun way to improve vocabulary and problem-solving!

## How to Play
1. Run the game: `python game.py`
2. Choose a difficulty level (Easy/Medium/Hard)
3. Try to unscramble the letters
4. Use hints to reveal letters if needed
5. Score points based on speed and fewer hints

## Python Concepts Learned
- **String Manipulation**: Working with characters and slices
- **Lists**: Tracking revealed letters
- **Random Module**: Scrambling words and selecting randomly
- **Timer**: Tracking time for scoring
- **Sets**: Understanding unique characters
- **Game State**: Managing hints and progress

## Difficulty Levels
| Level | Word Length | Example Words |
|-------|-------------|---------------|
| Easy | 4-6 letters | python, coding, debug |
| Medium | 7-9 letters | algorithm, function, database |
| Hard | 10+ letters | polymorphism, inheritance, recursion |

## Scoring System
- **Base Points**: Easy (10), Medium (20), Hard (30)
- **Speed Bonus**: +10 (under 10s), +5 (under 20s)
- **Hint Penalty**: -3 per hint used
- **Guess Penalty**: -2 per extra guess

## Sample Output
```
==================================================
  WORD SCRAMBLE
==================================================

Welcome to Word Scramble!

Rules:
  1. Unscramble the letters to find the word
  2. Get hints by revealing letters
  3. Fewer hints = more points
  4. Choose your difficulty level

  Choose difficulty:
  1. Easy
  2. Medium
  3. Hard

Enter choice (1-3): 2

  Difficulty: Medium
  Word length: 8 letters

  Scrambled: NOCPIRETU
  Progress:  _ _ _ _ _ _ _ _

  Options:
  1. Guess the word
  2. Get a hint
  3. Give up

Your choice (1/2/3): 2

  Hint: Position 1 is 'T'
  Progress:  T _ _ _ _ _ _ _

  Options:
  1. Guess the word
  2. Get a hint
  3. Give up

Your choice (1/2/3): 1

Enter your guess: terminal

  🎉 CORRECT! The word was: TERMINAL
  ⏱️  Time: 12.3 seconds
  💡 Hints used: 1
  🎯 Points earned: 17

  📊 Total Points: 17

Play another word? (yes/no): y

  ... (continues) ...

==================================================
  FINAL RESULTS
==================================================

  Words played: 5
  Total points: 85
  Best word: POLYMORPHISM (30 points)

Thanks for playing Word Scramble!
See you next time!
```

## Code Structure
```
word_scramble/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `select_difficulty()`: Get player's difficulty choice
- `scramble_word(word)`: Shuffle letters randomly
- `reveal_hint(word, revealed)`: Show an unrevealed letter
- `display_word_progress(word, revealed)`: Show current progress
- `play_round(difficulty)`: Play one word round
- `calculate_points(...)`: Score based on performance
- `display_welcome()`: Show game rules
- `main()`: Main game loop

## Error Handling
- Validates difficulty selection
- Validates menu choices
- Handles invalid guess input
- Graceful give-up option

## Future Enhancements
- [ ] Add more word categories
- [ ] Implement timed mode
- [ ] Add multiplayer race mode
- [ ] Create word definitions on completion
- [ ] Add streak bonuses
- [ ] Implement daily challenges

# Rock Paper Scissors Game

## Description
The classic Rock Paper Scissors game! Play against the computer in this timeless game of chance and strategy. Track your wins, losses, and ties across multiple rounds.

## How to Play
1. Run the game: `python game.py`
2. Choose Rock, Paper, or Scissors each round
3. See if you beat the computer
4. Track your score across all rounds
5. Quit anytime to see final results

## Python Concepts Learned
- **Random Module**: Computer makes random choices
- **Dictionaries**: Mapping choices to emojis and win conditions
- **While Loops**: Playing multiple rounds
- **If/Elif/Else**: Determining the winner
- **String Formatting**: f-strings for display
- **Variables**: Tracking score across rounds
- **Functions**: Breaking code into reusable pieces

## Game Rules
| You Choose | Computer Chooses | Result |
|------------|------------------|--------|
| Rock | Scissors | You Win |
| Rock | Paper | You Lose |
| Paper | Rock | You Win |
| Paper | Scissors | You Lose |
| Scissors | Paper | You Win |
| Scissors | Rock | You Lose |
| Same | Same | Tie |

## Sample Output
```
==================================================
  ROCK PAPER SCISSORS
==================================================

Welcome to Rock Paper Scissors!

Rules:
  🪨 Rock     → beats ✂️  Scissors
  📄 Paper    → beats 🪨 Rock
  ✂️  Scissors → beats 📄 Paper

  Make your choice:
  1. 🪨  Rock
  2. 📄  Paper
  3. ✂️  Scissors
  4. 🚪  Quit

Enter your choice (1-4): 1

  You chose:      Rock 🪨
  Computer chose: Scissors ✂️
  ------------------------------
  🎉 You WIN this round!

  📊 SCOREBOARD (after 1 round(s))
  ==============================
  Player Wins:   1 🎉
  Computer Wins: 0 💻
  Ties:          0 🤝
  Win Rate:      100.0%

  Make your choice:
  1. 🪨  Rock
  2. 📄  Paper
  3. ✂️  Scissors
  4. 🚪  Quit

Enter your choice (1-4): 4

==================================================
  FINAL RESULTS
==================================================

  📊 SCOREBOARD (after 1 round(s))
  ==============================
  Player Wins:   1 🎉
  Computer Wins: 0 💻
  Ties:          0 🤝
  Win Rate:      100.0%

  🏆 Great job! You beat the computer!

Thanks for playing Rock Paper Scissors!
See you next time!
```

## Code Structure
```
rock_paper_scissors/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_menu()`: Show choices and get player input
- `get_computer_choice()`: Generate random computer choice
- `determine_winner(player, computer)`: Decide round winner
- `display_result(player, computer, result)`: Show round outcome
- `display_score(wins, losses, ties)`: Show current scoreboard
- `display_welcome()`: Show game rules
- `play_game()`: Main game loop with score tracking

## Error Handling
- Validates menu input (1-4)
- Handles invalid menu choices
- Graceful exit with quit option

## Future Enhancements
- [ ] Add best-of-N series mode
- [ ] Implement Lizard-Spock variant
- [ ] Add streak tracking
- [ ] Create AI difficulty levels
- [ ] Add sound effects
- [ ] Implement multiplayer mode

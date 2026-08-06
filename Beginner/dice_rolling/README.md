# Dice Rolling Simulator

## Description
Roll virtual dice with beautiful ASCII art! Track your rolls, discover special combinations, and see detailed statistics. Perfect for tabletop gaming or learning about probability!

## How to Play
1. Run the game: `python game.py`
2. Choose how many dice to roll (1-6)
3. See ASCII art of your dice rolls
4. Discover special combinations
5. Track your statistics over time

## Python Concepts Learned
- **Random Module**: Generating random dice values
- **Lists**: Storing roll history
- **Dictionaries**: Mapping dice values to ASCII art
- **ASCII Art**: Visual dice representation
- **Statistics**: Calculating averages and frequencies
- **Collections**: Using Counter for frequency analysis

## Dice Combinations
| Combination | Condition |
|-------------|-----------|
| 🎯 Double | Two matching dice |
| 🔥 Triple | Three matching dice |
| 💎 Four of a Kind | Four matching dice |
| 👑 Five of a Kind | Five matching dice |
| 🏆 Six of a Kind | Six matching dice |
| 🍀 Lucky 7 | Total equals 7 |
| ⚡ Lucky 11 | Total equals 11 |
| 🌟 Maximum | All dice show 6 |
| 🎯 Minimum | All dice show 1 |
| 🌈 Straight | Rolling 1-2-3-4-5-6 |

## Sample Output
```
==================================================
  DICE ROLLING SIMULATOR
==================================================

Welcome to the Dice Rolling Simulator!

Rules:
  1. Choose how many dice to roll (1-6)
  2. See ASCII art of each die
  3. Track your roll history and stats
  4. Try to roll specific combinations!

How many dice to roll? (1-6): 3

  Your rolls:

  ┌─────────┐  ┌─────────┐  ┌─────────┐
  │  ●   ●  │  │  ●      │  │  ●   ●  │
  │    ●    │  │    ●    │  │  ●   ●  │
  │  ●   ●  │  │      ●  │  │  ●   ●  │
  └─────────┘  └─────────┘  └─────────┘

  Die 1: 5    Die 2: 3    Die 3: 6

  Total: 14

  (Total rolls: 1)

Roll again? (yes/no): y

How many dice to roll? (1-6): 2

  Your rolls:

  ┌─────────┐  ┌─────────┐
  │  ●      │  │  ●      │
  │    ●    │  │    ●    │
  │      ●  │  │      ●  │
  └─────────┘  └─────────┘

  Die 1: 3    Die 2: 3

  Total: 6

  🎉 COMBINATIONS:
    🎯 Double!

  (Total rolls: 2)

Roll again? (yes/no): n

  📊 ROLL STATISTICS
  ===================================
  Total dice rolled:  5
  Total sum:          20
  Average:            4.00
  Highest single:     6
  Lowest single:      3
  Number of rolls:    2

  Frequency:
    1:  (0)
    2:  (0)
    3: ███ (3)
    4:  (0)
    5: █ (1)
    6: █ (1)

==================================================
  FINAL SUMMARY
==================================================
  Total rolls: 2
  Total dice rolled: 5
  Grand total: 20

Thanks for playing Dice Rolling Simulator!
See you next time!
```

## Code Structure
```
dice_rolling/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `roll_dice(count)`: Generate random dice values
- `display_dice(rolls)`: Show ASCII art dice
- `get_dice_count()`: Get number of dice from player
- `check_combinations(rolls)`: Detect special combinations
- `display_statistics(history)`: Show roll statistics
- `display_welcome()`: Show game rules
- `main()`: Main game loop

## Error Handling
- Validates dice count input (1-6)
- Handles non-numeric input
- Graceful exit option

## Future Enhancements
- [ ] Add custom dice (d4, d8, d10, d12, d20)
- [ ] Implement Yahtzee-style scoring
- [ ] Add dice rolling animations
- [ ] Create dice probability calculator
- [ ] Add multiplayer dice games
- [ ] Implement roll history export

# Pomodoro Timer

## Description
A productivity timer using the Pomodoro technique! Work in focused intervals with scheduled breaks to maximize your productivity.

## How to Play
1. Run the game: `python game.py`
2. Use default settings or customize
3. Work during the 25-minute timer
4. Take breaks between sessions
5. After 4 pomodoros, take a long break

## Python Concepts Learned
- **time Module**: Sleep and countdown
- **While Loops**: Timer loops
- **Counters**: Tracking pomodoros
- **ASCII Animation**: Progress bar
- **Keyboard Handling**: Ctrl+C interrupt

## Pomodoro Technique
- **Work**: 25 minutes of focused work
- **Short Break**: 5 minutes rest
- **Long Break**: 15 minutes after 4 pomodoros
- **Repeat**: Continue the cycle

## Sample Output
```
==================================================
  🍅 POMODORO TIMER
==================================================

  🍅 WORK - Pomodoro #1

  Time: 24:35

  [████████░░░░░░░░░░░░]

==================================================
  Press Ctrl+C to skip
==================================================
```

## Code Structure
```
pomodoro_timer/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add task tracking
- [ ] Save session history
- [ ] Add notification sounds
- [ ] Create daily goals

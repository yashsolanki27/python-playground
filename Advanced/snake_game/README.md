# Snake Game (Terminal Version)

## Description
The classic Snake game! Control a snake to eat food and grow longer while avoiding walls and yourself. This is a terminal-based version that works on any system.

## How to Play
1. Run the game: `python game.py`
2. Use WASD or Arrow Keys to control the snake
3. Eat the food (@) to grow and score points
4. Avoid hitting walls or your own tail
5. Try to get the highest score!
6. Press 'q' to quit

## Python Concepts Learned
- **Object-Oriented Programming**: Snake, Point, and Game classes
- **2D Lists**: Game grid representation
- **Game Loop**: Continuous game updates
- **Input Handling**: Keyboard controls
- **Collision Detection**: Walls, food, and self-collision
- **Score Tracking**: Points and statistics
- **Terminal UI**: Screen clearing and display

## Game Features
- Smooth snake movement
- Growing snake when eating food
- Score tracking
- Game over detection
- Statistics tracking
- Terminal-based graphics

## Sample Output
```
==================================================
 SNAKE GAME
==================================================
 Score: 30
 Length: 4
--------------------------------------------------
┌────────────────────┐
│                    │
│    ████            │
│              @     │
│                    │
│                    │
│                    │
└────────────────────┘
--------------------------------------------------
 Controls: WASD or Arrow Keys
 Quit: 'q'
==================================================
```

## Code Structure
```
snake_game/
├── game.py           # Main game file (300 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Classes

### Point Class
- `x`: X coordinate
- `y`: Y coordinate
- `__eq__()`: Compare points
- `__hash__()`: Hash for sets

### Snake Class
- `body`: List of Point objects
- `direction`: Current movement direction
- `move()`: Move the snake
- `grow()`: Grow the snake
- `check_collision()`: Check self-collision
- `change_direction()`: Change direction

### SnakeGame Class
- `width/height`: Game grid size
- `snake`: Snake object
- `food`: Food position
- `score`: Current score
- `game_over`: Game state

## Key Functions
- `clear_screen()`: Clears terminal
- `create_grid()`: Creates game grid
- `display()`: Shows game state
- `spawn_food()`: Places food randomly
- `process_input(key)`: Handles keyboard input
- `update()`: Updates game state
- `check_wall_collision()`: Wall collision detection
- `check_food_collision()`: Food collision detection

## Controls
| Key | Action |
|-----|--------|
| W / ↑ | Move Up |
| S / ↓ | Move Down |
| A / ← | Move Left |
| D / → | Move Right |
| Q | Quit Game |

## Scoring System
- Eating food: +10 points
- Bonus points for longer snake

## Error Handling
- Handles invalid input
- Prevents snake from reversing
- Validates game boundaries
- Handles terminal input gracefully

## Platform Compatibility
- **Windows**: Uses `msvcrt` for keyboard input
- **Linux/Mac**: Uses `tty` and `termios` for keyboard input
- **Cross-platform**: Clears screen appropriately

## Future Enhancements
- [ ] Add pygame version with graphics
- [ ] Add power-ups and special food
- [ ] Add multiple difficulty levels
- [ ] Add sound effects
- [ ] Create multiplayer mode
- [ ] Add leaderboard system
- [ ] Implement snake skins
- [ ] Add obstacles and maze mode
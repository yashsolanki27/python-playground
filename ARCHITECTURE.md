# Project Architecture

## Directory Structure
```
Basics_games/
│
├── AGENTS.md                    # AI agent guidelines
├── ARCHITECTURE.md              # This file
├── README.md                    # Project overview
├── CONTRIBUTING.md              # Contribution guidelines
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Global dependencies
│
├── Beginner/                    # Level 1: Core Python Concepts
│   ├── number_guessing/         # Variables, loops, conditionals
│   │   ├── README.md
│   │   ├── game.py
│   │   └── requirements.txt
│   │
│   ├── rock_paper_scissors/     # If-else, random module
│   │   ├── README.md
│   │   ├── game.py
│   │   └── requirements.txt
│   │
│   └── calculator/              # Functions, arithmetic ops
│       ├── README.md
│       ├── game.py
│       └── requirements.txt
│
├── Intermediate/                # Level 2: Data Structures & Logic
│   ├── hangman/                 # Lists, strings, loops
│   │   ├── README.md
│   │   ├── game.py
│   │   └── requirements.txt
│   │
│   ├── tic_tac_toe/             # 2D lists, game logic
│   │   ├── README.md
│   │   ├── game.py
│   │   └── requirements.txt
│   │
│   └── quiz_game/               # Dictionaries, score tracking
│       ├── README.md
│       ├── game.py
│       └── requirements.txt
│
└── Advanced/                    # Level 3: OOP & Complex Logic
    ├── blackjack/               # OOP, complex game rules
    │   ├── README.md
    │   ├── game.py
    │   └── requirements.txt
    │
    ├── snake_game/              # OOP, pygame, animations
    │   ├── README.md
    │   ├── game.py
    │   └── requirements.txt
    │
    └── inventory_system/        # OOP, file persistence
        ├── README.md
        ├── game.py
        └── requirements.txt
```

## Game Complexity Progression

### Beginner Games
| Game | Concepts | Difficulty | Est. Lines |
|------|----------|------------|------------|
| Number Guessing | Variables, loops, conditionals, random | ⭐ | 50-80 |
| Rock Paper Scissors | If-else, loops, user input | ⭐ | 60-100 |
| Calculator | Functions, arithmetic, error handling | ⭐⭐ | 80-120 |

### Intermediate Games
| Game | Concepts | Difficulty | Est. Lines |
|------|----------|------------|------------|
| Hangman | Lists, strings, loops, conditionals | ⭐⭐ | 100-150 |
| Tic-Tac-Toe | 2D lists, functions, game logic | ⭐⭐⭐ | 150-200 |
| Quiz Game | Dictionaries, loops, score tracking | ⭐⭐ | 120-180 |

### Advanced Games
| Game | Concepts | Difficulty | Est. Lines |
|------|----------|------------|------------|
| Blackjack | OOP, lists, complex logic | ⭐⭐⭐⭐ | 200-300 |
| Snake Game | OOP, pygame, animations | ⭐⭐⭐⭐⭐ | 250-400 |
| Inventory System | OOP, file I/O, data management | ⭐⭐⭐⭐ | 200-350 |

## Data Flow Architecture

### User Input Flow
```
User Input → Validation → Game Logic → Output → Display
     ↓
Error Handling → Retry/Exit
```

### Game State Management
```
Game Start → Initialize State → Game Loop → Update State → Check Win/Loss → End
     ↓
Play Again? → Yes: Reset State → Game Loop
           → No: Exit
```

## Module Dependencies

### Standard Library Only (No External Dependencies)
- `random` - Random number generation
- `os` - System operations
- `time` - Time-related functions
- `json` - Data serialization (for save/load)
- `datetime` - Date and time operations

### Optional External Dependencies
- `pygame` - For Snake Game GUI
- `colorama` - For colored terminal output
- `typing` - For type hints (built-in in Python 3.5+)

## Git Branch Strategy

### Branch Flow
```
main (production)
  └── feature/beginner-games (development)
        └── feature/number-guessing (feature)
        └── feature/rock-paper-scissors (feature)
        └── feature/calculator (feature)
  └── feature/intermediate-games (development)
        └── feature/hangman (feature)
        └── feature/tic-tac-toe (feature)
        └── feature/quiz-game (feature)
  └── feature/advanced-games (development)
        └── feature/blackjack (feature)
        └── feature/snake-game (feature)
        └── feature/inventory-system (feature)
```

### Merge Strategy
1. Complete game development on feature branch
2. Test thoroughly
3. Create pull request to phase branch
4. Review and merge
5. When phase complete, merge phase branch to main

## Testing Strategy

### Manual Testing
- Run each game manually
- Test all user inputs
- Verify error handling
- Check edge cases

### Automated Testing (Future)
- Unit tests for game logic
- Integration tests for game flow
- Performance tests for complex games

## Deployment Options

### Local Execution
```bash
# Run any game
python game.py

# Run with specific Python version
python3.11 game.py
```

### Web Deployment (Future)
- Convert terminal games to web apps using Flask/Django
- Deploy to Heroku, Vercel, or Railway

### Desktop Application (Future)
- Package with PyInstaller for standalone executables
- Create安装ers for Windows/macOS/Linux
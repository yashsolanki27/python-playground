# AI Agent Guidelines for Python Learning Games

## Project Overview
This project is a collection of Python games designed to teach programming fundamentals through hands-on practice.

## Agent Instructions

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions under 30 lines when possible
- Use type hints for function parameters and return values

### File Structure
Each game should follow this structure:
```
game_name/
├── README.md          # Game documentation
├── game.py           # Main game file
├── requirements.txt  # Game-specific dependencies (if any)
└── tests/            # Optional test files
    └── test_game.py
```

### Commit Messages
Use conventional commit format:
- `feat: add new game [game_name]`
- `fix: resolve issue in [game_name]`
- `docs: update README for [game_name]`
- `refactor: improve [game_name] code structure`

### Branch Strategy
- `main` - Production-ready code
- `feature/beginner-games` - Beginner level games
- `feature/intermediate-games` - Intermediate level games
- `feature/advanced-games` - Advanced level games

### Testing Requirements
- Each game should be testable via command line
- Include error handling for user input
- Validate all inputs
- Provide clear error messages

### Documentation Requirements
- Each game must have a README.md with:
  - Game description
  - How to play
  - Python concepts learned
  - Sample output
  - Future enhancements

### Code Quality Checklist
- [ ] No hardcoded values (use constants)
- [ ] Error handling implemented
- [ ] User input validated
- [ ] Comments explain complex logic
- [ ] Code is modular and reusable
- [ ] Follows Python naming conventions

### Learning Objectives
Each game should teach specific Python concepts:
- **Beginner**: Variables, loops, conditionals, functions
- **Intermediate**: Lists, dictionaries, file I/O, OOP basics
- **Advanced**: Full OOP, algorithms, data structures, GUI/terminal UI

### Deployment Guidelines
- Games should run with `python game.py`
- No external dependencies required (unless specified)
- Compatible with Python 3.11+
- Cross-platform compatible (Windows, macOS, Linux)
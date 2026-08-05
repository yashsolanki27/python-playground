# Contributing to Python Learning Games

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## How to Contribute

### 1. Fork the Repository
```bash
# Fork on GitHub, then clone
git clone https://github.com/yourusername/Basics_games.git
cd Basics_games
```

### 2. Create a Branch
```bash
# For new features
git checkout -b feature/your-game-name

# For bug fixes
git checkout -b fix/issue-description
```

### 3. Make Changes
- Follow the code style guidelines in AGENTS.md
- Add documentation for new games
- Test your changes thoroughly

### 4. Commit Changes
```bash
# Use conventional commit messages
git commit -m "feat: add new game [game_name]"
git commit -m "fix: resolve issue in [game_name]"
git commit -m "docs: update README for [game_name]"
```

### 5. Push and Create Pull Request
```bash
git push origin feature/your-game-name
```

## Code Style Guidelines

### Python Code
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions under 30 lines
- Use type hints where appropriate

### File Structure
Each game should have:
```
game_name/
├── README.md          # Game documentation
├── game.py           # Main game file
├── requirements.txt  # Dependencies (if any)
└── tests/            # Optional tests
    └── test_game.py
```

### Commit Messages
Use the format: `type: description`

Types:
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style changes
- `refactor` - Code refactoring
- `test` - Adding tests
- `chore` - Maintenance

## Game Requirements

### Documentation
Each game must include:
1. **README.md** with:
   - Game description
   - How to play
   - Python concepts learned
   - Sample output
   - Future enhancements

2. **Code Comments**:
   - Explain complex logic
   - Document function parameters
   - Note any assumptions

### Code Quality
- No hardcoded values (use constants)
- Proper error handling
- Input validation
- Clear error messages
- Modular code structure

### Testing
- Test all user inputs
- Verify error handling
- Check edge cases
- Ensure cross-platform compatibility

## Game Categories

### Beginner Games
- Teach basic Python concepts
- Use only standard library
- Simple input/output
- Basic control structures

### Intermediate Games
- Introduce data structures
- More complex logic
- File I/O operations
- Basic algorithms

### Advanced Games
- Object-oriented programming
- Complex algorithms
- External libraries (pygame, etc.)
- Data persistence

## Review Process

### Before Submitting
1. Test your game thoroughly
2. Check for code style compliance
3. Update documentation
4. Ensure no secrets or keys are committed

### Pull Request Requirements
1. Clear description of changes
2. Screenshots/videos if applicable
3. Test instructions
4. Related issue links

## Reporting Issues

### Bug Reports
Include:
- Game name
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version
- Operating system

### Feature Requests
Include:
- Game name
- Description of feature
- Use case
- Implementation ideas

## Code of Conduct

### Our Pledge
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn
- Share knowledge

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## Questions?

If you have questions:
1. Check existing documentation
2. Search existing issues
3. Create a new issue with the "question" label

Thank you for contributing!
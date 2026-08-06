# Password Generator

## Description
A secure password generation utility that creates strong, random passwords. Customize character types, check password strength, and generate multiple passwords at once!

## How to Play
1. Run the game: `python game.py`
2. Choose to generate a password or check strength
3. Select password length and character types
4. Get your secure password instantly
5. See strength analysis and score

## Python Concepts Learned
- **secrets Module**: Cryptographically secure random generation
- **String Constants**: Using pre-defined character sets
- **List Comprehensions**: Efficient password construction
- **Boolean Logic**: Character type options
- **Password Analysis**: Strength checking algorithms
- **Security Best Practices**: Understanding password entropy

## Character Types
| Type | Characters | Example |
|------|------------|---------|
| Uppercase | A-Z | ABCDEF |
| Lowercase | a-z | abcdef |
| Digits | 0-9 | 123456 |
| Symbols | !@#$%^&* | !@#$%^ |

## Strength Score
- **80-100**: 🔴 STRONG - Excellent security
- **60-79**: 🟠 MODERATE - Good for most uses
- **40-59**: 🟡 FAIR - Consider improving
- **0-39**: 🟢 WEAK - Not recommended

## Sample Output
```
==================================================
  PASSWORD GENERATOR
==================================================

Welcome to the Password Generator!

Features:
  1. Generate secure random passwords
  2. Customize character types
  3. Check password strength
  4. Generate multiple passwords at once

  Options:
  1. Generate a password
  2. Generate multiple passwords
  3. Check password strength
  4. Quit

Your choice (1-4): 1

Enter password length (8-64): 16

  Select character types:
  Include Uppercase letters (A-Z)? (yes/no) [Yes]: y
  Include Lowercase letters (a-z)? (yes/no) [Yes]: y
  Include Digits (0-9)? (yes/no) [Yes]: y
  Include Symbols (!@#$%^&*)? (yes/no) [Yes]: y

  🔐 Generated Password:
  k7#Lp2$mR9@nX4qW

  📊 PASSWORD STRENGTH
  ===================================
  Length:        16 characters
  Uppercase:     ✅
  Lowercase:     ✅
  Digits:        ✅
  Symbols:       ✅
  Unique chars:  16
  Score:         100/100
  Strength:      🔴 STRONG

Your choice (1-4): 3

Enter password to check: MyPassword123

  📊 PASSWORD STRENGTH
  ===================================
  Length:        13 characters
  Uppercase:     ✅
  Lowercase:     ✅
  Digits:        ✅
  Symbols:       ❌
  Unique chars:  10
  Score:         70/100
  Strength:      🟠 MODERATE

Your choice (1-4): 4

Thanks for using Password Generator!
Stay secure! 🔒
```

## Code Structure
```
password_generator/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `display_welcome()`: Show generator instructions
- `get_password_length()`: Get desired length from user
- `get_character_options()`: Get character type preferences
- `generate_password(length, options)`: Create secure password
- `check_password_strength(password)`: Analyze password security
- `display_strength(analysis)`: Show strength results
- `generate_multiple(length, options, count)`: Batch generation
- `main()`: Main generator loop

## Security Notes
- Uses `secrets` module (not `random`) for cryptographic security
- Generated passwords are cryptographically random
- No passwords are stored or logged
- Entropy increases with length and character variety

## Future Enhancements
- [ ] Add passphrase generation
- [ ] Implement password storage (encrypted)
- [ ] Add password expiration tracking
- [ ] Create password history
- [ ] Add copy-to-clipboard feature
- [ ] Implement password sharing (encrypted)

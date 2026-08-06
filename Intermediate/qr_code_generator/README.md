# QR Code Generator

## Description
Generate ASCII art QR codes from text! A fun way to learn about encoding and patterns.

## How to Play
1. Run the game: `python game.py`
2. Enter text or URL
3. See the ASCII QR pattern
4. Copy or use as needed

## Python Concepts Learned
- **String Encoding**: Converting text to hash
- **Hash Functions**: MD5 for pattern generation
- **ASCII Art**: Visual representation
- **2D Arrays**: Grid manipulation

## Sample Output
```
==================================================
  📱 QR CODE GENERATOR
==================================================

  Enter text or URL: https://example.com

  📱 QR Code for: https://example.com...
  ==============================================
  ██████████████████████████████
  ██  ████  ██  ██████  ██  ████  ██
  ██████████████████████████████
  ████  ████████████  ████████████
  ██████████████████████████████
  ██  ██  ██  ████████████  ██  ██
  ██████████████████████████████
  ==============================================
```

## Code Structure
```
qr_code_generator/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add real QR code library
- [ ] Support color output
- [ ] Add error correction
- [ ] Create image export

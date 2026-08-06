# Number To Word Converter

## Description
Convert any number (0 to 999,999,999) to English words. A great way to learn string manipulation, mathematical operations, and modular code design!

## How to Play
1. Run the game: `python game.py`
2. Enter a number when prompted
3. See the number written in English words
4. Continue converting or quit

## Python Concepts Learned
- **String Concatenation**: Building words from parts
- **Mathematical Operations**: Modulo and integer division
- **Lists**: Word mappings for ones, teens, tens
- **Functions**: Breaking code into reusable pieces
- **Input Validation**: Handling invalid inputs

## Sample Output
```
==================================================
  NUMBER TO WORD CONVERTER
==================================================

Convert numbers to English words!

Range: 0 to 999,999,999

Enter a number (0-999,999,999) or 'q' to quit: 123

  📝 Result:
  Number: 123
  Words:  one hundred and twenty-three

Enter a number (0-999,999,999) or 'q' to quit: 1000000

  📝 Result:
  Number: 1,000,000
  Words:  one million

Enter a number (0-999,999,999) or 'q' to quit: 42

  📝 Result:
  Number: 42
  Words:  forty-two
```

## Code Structure
```
number_to_words/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add decimal numbers
- [ ] Add currency conversion
- [ ] Support more languages
- [ ] Add Roman numeral conversion

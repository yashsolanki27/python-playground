# Calculator Game

## Description
An interactive command-line calculator that performs basic arithmetic operations. Practice working with functions, operators, and user input while performing real calculations!

## How to Play
1. Run the game: `python game.py`
2. Select an operation (+, -, *, /)
3. Enter two numbers when prompted
4. See the result immediately
5. Continue calculating or quit to see history

## Python Concepts Learned
- **Arithmetic Operators**: +, -, *, / for calculations
- **Functions**: Each operation is a separate function
- **User Input**: Getting numbers and operations from player
- **Type Conversion**: Converting string input to floats
- **Error Handling**: Division by zero protection
- **While Loops**: Continuous calculation mode
- **Lists**: Storing calculation history
- **Dictionaries**: Organizing calculation data

## Operations
| Symbol | Operation | Example |
|--------|-----------|---------|
| + | Addition | 5 + 3 = 8 |
| - | Subtraction | 5 - 3 = 2 |
| * | Multiplication | 5 * 3 = 15 |
| / | Division | 6 / 3 = 2 |

## Sample Output
```
==================================================
  CALCULATOR
==================================================

Welcome to the Calculator!

Instructions:
  1. Choose an operation
  2. Enter two numbers
  3. See the result
  4. Continue or quit

  Operations:
  + : Addition
  - : Subtraction
  * : Multiplication
  / : Division
  q : Quit

Enter operation (+, -, *, /, q): +

Enter first number (or 'q' to quit): 15
Enter second number (or 'q' to quit): 7

  ✅ Result: 15.0 + 7.0 = 22.0

  (Total calculations: 1)

Enter operation (+, -, *, /, q): *

Enter first number (or 'q' to quit): 6
Enter second number (or 'q' to quit): 9

  ✅ Result: 6.0 * 9.0 = 54.0

  (Total calculations: 2)

Enter operation (+, -, *, /, q): /

Enter first number (or 'q' to quit): 10
Enter second number (or 'q' to quit): 0

  ❌ Error: Division by zero!

  (Total calculations: 2)

Enter operation (+, -, *, /, q): q

  📜 CALCULATION HISTORY
  ===================================
  1. 15.0 + 7.0 = 22.0
  2. 6.0 * 9.0 = 54.0

==================================================
  FINAL SUMMARY
==================================================
  Total calculations: 2
  Last calculation: 6.0 * 9.0 = 54.0

Thanks for using Calculator!
See you next time!
```

## Code Structure
```
calculator/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `add(a, b)`: Addition operation
- `subtract(a, b)`: Subtraction operation
- `multiply(a, b)`: Multiplication operation
- `divide(a, b)`: Division with zero check
- `get_number(prompt)`: Get validated number input
- `get_operation()`: Get operation choice from menu
- `calculate(a, b, op)`: Perform calculation
- `display_history(history)`: Show calculation history
- `display_welcome()`: Show instructions
- `main()`: Main calculator loop

## Error Handling
- Validates number input (catches non-numeric)
- Prevents division by zero
- Handles invalid operation choices
- Graceful quit at any prompt

## Future Enhancements
- [ ] Add modulus (%) operation
- [ ] Add exponentiation (**) operation
- [ ] Add square root function
- [ ] Implement memory storage (M+, M-, MR, MC)
- [ ] Add parentheses support for expressions
- [ ] Create GUI version
- [ ] Add unit conversion mode

# Calculator Game

## Description
A simple but powerful calculator that demonstrates functions, arithmetic operations, and error handling in Python.

## How to Play
1. Run the game: `python game.py`
2. Enter the first number
3. Choose an operation (+, -, *, /, **, %)
4. Enter the second number
5. See the result
6. Continue calculating or exit

## Python Concepts Learned
- **Functions**: Creating reusable functions for each operation
- **Arithmetic Operators**: +, -, *, /, **, %
- **Error Handling**: Division by zero and invalid input
- **Type Hints**: Function parameter and return type annotations
- **Input Validation**: Ensuring valid numbers and operations
- **Loops**: Continuous calculation loop
- **Dictionaries**: Mapping operations to functions

## Available Operations
| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 5 - 3 | 2 |
| * | Multiplication | 5 * 3 | 15 |
| / | Division | 6 / 3 | 2 |
| ** | Power | 2 ** 3 | 8 |
| % | Modulus | 7 % 3 | 1 |

## Sample Output
```
==================================================
 Simple Calculator
==================================================

Available Operations:
  +  Addition
  -  Subtraction
  *  Multiplication
  /  Division
  ** Power
  %  Modulus (Remainder)

Enter 'quit' at any time to exit.
--------------------------------------------------

Enter first number: 10
Enter operation (+, -, *, /, **, %): *
Enter second number: 5

========================================
 10.0 * 5.0 = 50.0
========================================

Do another calculation? (yes/no): yes

Enter first number: 100
Enter operation (+, -, *, /, **, %): /
Enter second number: 0

========================================
 100.0 / 0.0 = Error: Division by zero!
========================================

Do another calculation? (yes/no): no

==================================================
 Calculator Summary
==================================================
 You performed 2 calculations
==================================================

Thanks for using the calculator! Goodbye!
```

## Code Structure
```
calculator/
├── game.py           # Main game file (150 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Key Functions
- `add(a, b)`: Addition operation
- `subtract(a, b)`: Subtraction operation
- `multiply(a, b)`: Multiplication operation
- `divide(a, b)`: Division with zero check
- `power(a, b)`: Exponentiation
- `modulus(a, b)`: Modulus with zero check
- `get_number(prompt)`: Get and validate number input
- `get_operation()`: Get and validate operation input
- `calculate(a, b, operation)`: Perform calculation
- `display_result(a, b, operation, result)`: Show result
- `play_game()`: Main calculator loop
- `main()`: Entry point

## Error Handling
- **Division by Zero**: Checks before division operations
- **Invalid Numbers**: Validates numeric input
- **Invalid Operations**: Ensures operation is supported
- **Graceful Exit**: 'quit' command at any prompt

## Type Hints Used
```python
def add(a: float, b: float) -> float:
def divide(a: float, b: float) -> Union[float, str]:
def get_number(prompt: str) -> Union[float, None]:
```

## Future Enhancements
- [ ] Add memory function (MR, MC, M+, M-)
- [ ] Add history of calculations
- [ ] Support parentheses in expressions
- [ ] Add scientific functions (sin, cos, log)
- [ ] Create GUI version with tkinter
- [ ] Add unit conversion
- [ ] Implement keyboard shortcuts
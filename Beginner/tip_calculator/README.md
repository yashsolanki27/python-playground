# Tip Calculator

## Description
Quickly calculate tips and split bills with friends. A practical utility that teaches arithmetic operations and formatted output!

## How to Play
1. Run the game: `python game.py`
2. Enter the bill amount
3. Choose tip percentage
4. Enter number of people splitting
5. See the breakdown

## Python Concepts Learned
- **Arithmetic Operations**: Multiplication and division
- **String Formatting**: Aligned dollar amounts
- **Functions**: Modular calculation functions
- **Input Validation**: Handling edge cases

## Sample Output
```
==================================================
  TIP CALCULATOR
==================================================

Calculate tips and split bills!

Enter bill amount (or 'q' to quit): $85.50

  Tip suggestions:
  15% - Good service
  18% - Great service
  20% - Excellent service
  25% - Outstanding service

Enter tip percentage (1-100): 20

How many people splitting? (1-20): 4

========================================
  📊 BILL SUMMARY
========================================
  Bill Amount:    $     85.50
  Tip (20%):      $     17.10
  ----------------------------------
  Total:          $    102.60

  Split between 4 people:
  Per Person:     $     25.65
========================================
```

## Code Structure
```
tip_calculator/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add tax calculation
- [ ] Save bill history
- [ ] Add currency conversion
- [ ] Create receipt export

# Expense Tracker

## Description
Track your daily expenses and see where your money goes! Add expenses by category, view all transactions, and get spending summaries.

## How to Play
1. Run the game: `python game.py`
2. Add expenses with category and amount
3. View all expenses
4. See spending summary by category
5. Data is saved automatically

## Python Concepts Learned
- **Lists and Dictionaries**: Storing expense data
- **File I/O**: Saving/loading from JSON
- **Data Persistence**: Maintaining state between runs
- **Summarization**: Calculating totals by category
- **Sorting**: Ordering expenses by amount

## Sample Output
```
==================================================
  EXPENSE TRACKER
==================================================

  Options:
  1. Add expense
  2. View all expenses
  3. View summary
  4. Quit

  Your choice (1-4): 1

  Add New Expense
  ------------------------------
  Categories:
    1. Food
    2. Transport
    3. Entertainment
    4. Shopping
    5. Bills
    6. Other

  Select category (1-6): 1
  Enter amount: $25.50
  Enter description (optional): Lunch

  ✅ Expense added: Food - $25.50

  Your choice (1-4): 3

  📊 SPENDING SUMMARY
  ========================================
  Food            $    25.50 ( 50.5%) ██████
  Transport       $    25.00 ( 49.5%) █████
  ----------------------------------------
  TOTAL           $    50.50
  ========================================
```

## Code Structure
```
expense_tracker/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add monthly budgets
- [ ] Export to CSV
- [ ] Add charts/graphs
- [ ] Set spending alerts

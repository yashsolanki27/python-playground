"""
Expense Tracker
Track your expenses and see spending summaries. Learn file I/O and data structures.

How to Play:
1. Add expenses with category and amount
2. View all expenses
3. See spending summary by category
4. Save and load expenses from file

Python Concepts:
- Lists and dictionaries
- File I/O (JSON)
- Data persistence
- Summarization
"""

import json
import os
from datetime import datetime


EXPENSES_FILE = "expenses.json"


def load_expenses() -> list[dict]:
    """Load expenses from file.
    
    Returns:
        List of expense dictionaries
    """
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_expenses(expenses: list[dict]) -> None:
    """Save expenses to file.
    
    Args:
        expenses: List of expense dictionaries
    """
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  EXPENSE TRACKER")
    print("="*50)
    print("\nTrack your spending!")
    print("\nPython Concepts: Lists, File I/O, JSON")


def add_expense(expenses: list[dict]) -> None:
    """Add a new expense.
    
    Args:
        expenses: List to add to
    """
    print("\n  Add New Expense")
    print("  " + "-"*30)
    
    categories = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Bills', 'Other']
    
    print("  Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"    {i}. {cat}")
    
    while True:
        try:
            choice = int(input("\n  Select category (1-6): ").strip())
            if 1 <= choice <= 6:
                category = categories[choice - 1]
                break
        except ValueError:
            pass
        print("  Invalid choice!")
    
    while True:
        try:
            amount = float(input("  Enter amount: $").strip())
            if amount > 0:
                break
        except ValueError:
            pass
        print("  Invalid amount!")
    
    description = input("  Enter description (optional): ").strip()
    
    expense = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'category': category,
        'amount': amount,
        'description': description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    
    print(f"\n  ✅ Expense added: {category} - ${amount:.2f}")


def view_expenses(expenses: list[dict]) -> None:
    """Display all expenses.
    
    Args:
        expenses: List of expenses
    """
    if not expenses:
        print("\n  No expenses recorded yet!")
        return
    
    print("\n  📋 ALL EXPENSES")
    print("  " + "="*60)
    print(f"  {'Date':<16} {'Category':<15} {'Amount':>10} {'Description'}")
    print("  " + "-"*60)
    
    for exp in expenses:
        desc = exp.get('description', '')[:20]
        print(f"  {exp['date']:<16} {exp['category']:<15} ${exp['amount']:>9.2f} {desc}")
    
    total = sum(exp['amount'] for exp in expenses)
    print("  " + "-"*60)
    print(f"  {'TOTAL':<32} ${total:>9.2f}")
    print("  " + "="*60)


def view_summary(expenses: list[dict]) -> None:
    """Display spending summary by category.
    
    Args:
        expenses: List of expenses
    """
    if not expenses:
        print("\n  No expenses to summarize!")
        return
    
    print("\n  📊 SPENDING SUMMARY")
    print("  " + "="*40)
    
    # Group by category
    categories = {}
    for exp in expenses:
        cat = exp['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += exp['amount']
    
    total = sum(categories.values())
    
    # Sort by amount (highest first)
    sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    
    for cat, amount in sorted_cats:
        pct = (amount / total) * 100
        bar = "█" * int(pct / 5)
        print(f"  {cat:<15} ${amount:>9.2f} ({pct:>5.1f}%) {bar}")
    
    print("  " + "-"*40)
    print(f"  {'TOTAL':<15} ${total:>9.2f}")
    print("  " + "="*40)


def main() -> None:
    """Main tracker loop."""
    display_welcome()
    
    expenses = load_expenses()
    
    while True:
        print("\n  Options:")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. View summary")
        print("  4. Quit")
        
        choice = input("\n  Your choice (1-4): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            break
        else:
            print("  Invalid choice!")
    
    print(f"\n  Total expenses tracked: {len(expenses)}")
    print("\nThanks for using Expense Tracker!")
    print("See you next time!")


if __name__ == "__main__":
    main()

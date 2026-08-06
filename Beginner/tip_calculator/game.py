"""
Tip Calculator
Calculate tips and split bills easily. Learn arithmetic and formatting.

How to Play:
1. Enter the bill amount
2. Enter tip percentage
3. Enter number of people splitting
4. See the tip and total per person

Python Concepts:
- Arithmetic operations
- String formatting
- User input validation
- Functions
"""

def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  TIP CALCULATOR")
    print("="*50)
    print("\nCalculate tips and split bills!")
    print("\nPython Concepts: Arithmetic, Formatting, Functions")


def get_bill_amount() -> float | None:
    """Get bill amount from user.
    
    Returns:
        Bill amount or None for quit
    """
    while True:
        user_input = input("\nEnter bill amount (or 'q' to quit): $").strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            amount = float(user_input)
            if amount > 0:
                return amount
            print("Please enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_tip_percentage() -> float:
    """Get tip percentage from user.
    
    Returns:
        Tip percentage as decimal
    """
    print("\n  Tip suggestions:")
    print("  15% - Good service")
    print("  18% - Great service")
    print("  20% - Excellent service")
    print("  25% - Outstanding service")
    
    while True:
        try:
            tip = float(input("\nEnter tip percentage (1-100): ").strip())
            if 1 <= tip <= 100:
                return tip / 100
            print("Please enter a percentage between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_split_count() -> int:
    """Get number of people splitting the bill.
    
    Returns:
        Number of people
    """
    while True:
        try:
            count = int(input("\nHow many people splitting? (1-20): ").strip())
            if 1 <= count <= 20:
                return count
            print("Please enter 1-20.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_tip(bill: float, tip_pct: float) -> float:
    """Calculate tip amount.
    
    Args:
        bill: Bill amount
        tip_pct: Tip percentage as decimal
        
    Returns:
        Tip amount
    """
    return bill * tip_pct


def calculate_total(bill: float, tip: float) -> float:
    """Calculate total with tip.
    
    Args:
        bill: Bill amount
        tip: Tip amount
        
    Returns:
        Total amount
    """
    return bill + tip


def calculate_per_person(total: float, people: int) -> float:
    """Calculate amount per person.
    
    Args:
        total: Total amount
        people: Number of people
        
    Returns:
        Amount per person
    """
    return total / people


def display_results(bill: float, tip: float, total: float, per_person: float, people: int) -> None:
    """Display calculation results.
    
    Args:
        bill: Original bill
        tip: Tip amount
        total: Total with tip
        per_person: Amount per person
        people: Number of people
    """
    print("\n" + "="*40)
    print("  📊 BILL SUMMARY")
    print("="*40)
    print(f"  Bill Amount:    ${bill:>10.2f}")
    print(f"  Tip ({tip/bill*100:.0f}%):       ${tip:>10.2f}")
    print(f"  {'-'*34}")
    print(f"  Total:          ${total:>10.2f}")
    
    if people > 1:
        print(f"\n  Split between {people} people:")
        print(f"  Per Person:     ${per_person:>10.2f}")
    
    print("="*40)


def main() -> None:
    """Main calculator loop."""
    display_welcome()
    
    calculations = 0
    
    while True:
        bill = get_bill_amount()
        if bill is None:
            break
        
        tip_pct = get_tip_percentage()
        people = get_split_count()
        
        tip = calculate_tip(bill, tip_pct)
        total = calculate_total(bill, tip)
        per_person = calculate_per_person(total, people)
        
        display_results(bill, tip, total, per_person, people)
        
        calculations += 1
        print(f"\n  (Total calculations: {calculations})")
    
    print("\n" + "="*50)
    print(f"  Total calculations: {calculations}")
    print("\nThanks for using Tip Calculator!")
    print("See you next time!")


if __name__ == "__main__":
    main()

"""
Age Calculator
Calculate your exact age in years, months, days, hours, and minutes.

How to Play:
1. Enter your birth date
2. See your exact age breakdown
3. Calculate again or quit

Python Concepts:
- datetime module
- Date arithmetic
- String formatting
"""

from datetime import datetime, date


def calculate_age(birth_date: date) -> dict:
    today = date.today()
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
    
    if months < 0:
        years -= 1
        months += 12
    
    total_days = (today - birth_date).days
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    
    return {
        'years': years,
        'months': months,
        'days': days,
        'total_days': total_days,
        'total_hours': total_hours,
        'total_minutes': total_minutes
    }


def main():
    print("\n" + "="*50)
    print("  🎂 AGE CALCULATOR")
    print("="*50)
    print("\nCalculate your exact age!")
    print("\nPython Concepts: datetime, Date Arithmetic")
    
    while True:
        print("\nEnter your birth date:")
        try:
            year = int(input("  Year (e.g., 1995): ").strip())
            month = int(input("  Month (1-12): ").strip())
            day = int(input("  Day (1-31): ").strip())
            
            birth = date(year, month, day)
            
            if birth > date.today():
                print("  Birth date cannot be in the future!")
                continue
            
            age = calculate_age(birth)
            
            print("\n" + "="*50)
            print("  📊 YOUR AGE")
            print("="*50)
            print(f"  Birth Date:   {birth.strftime('%B %d, %Y')}")
            print(f"  Today:        {date.today().strftime('%B %d, %Y')}")
            print(f"  " + "-"*44)
            print(f"  Years:        {age['years']}")
            print(f"  Months:       {age['months']}")
            print(f"  Days:         {age['days']}")
            print(f"  " + "-"*44)
            print(f"  Total Days:   {age['total_days']:,}")
            print(f"  Total Hours:  {age['total_hours']:,}")
            print(f"  Total Minutes:{age['total_minutes']:,}")
            print("="*50)
        
        except ValueError:
            print("  Invalid date! Please try again.")
            continue
        
        again = input("\nCalculate another? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            break
    
    print("\nThanks for using Age Calculator!")


if __name__ == "__main__":
    main()

"""
Calculator Game
An interactive calculator to learn arithmetic operations and user input handling.

How to Play:
1. Select an operation (+, -, *, /)
2. Enter two numbers
3. See the result
4. Continue calculating or exit

Python Concepts:
- Arithmetic operators (+, -, *, /)
- Functions for each operation
- User input and type conversion
- Error handling (division by zero)
- While loops for continuous calculation
- Menu-driven interface
"""


def add(a: float, b: float) -> float:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float | None:
    """Divide two numbers.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
        
    Returns:
        Quotient or None if division by zero
    """
    if b == 0:
        return None
    return a / b


def get_number(prompt: str) -> float | None:
    """Get a number from user input.
    
    Args:
        prompt: Message to display
        
    Returns:
        Number as float, or None for invalid input
    """
    while True:
        user_input = input(prompt).strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation() -> str | None:
    """Get arithmetic operation from user.
    
    Returns:
        Operation symbol or None for quit
    """
    print("\n  Operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  q : Quit")
    
    while True:
        op = input("\nEnter operation (+, -, *, /, q): ").strip()
        if op in ['+', '-', '*', '/']:
            return op
        elif op.lower() == 'q':
            return None
        else:
            print("Invalid operation. Please enter +, -, *, /, or q.")


def calculate(a: float, b: float, op: str) -> tuple[float | None, str]:
    """Perform calculation based on operation.
    
    Args:
        a: First number
        b: Second number
        op: Operation symbol
        
    Returns:
        Tuple of (result, error_message)
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    result = operations[op](a, b)
    
    if result is None:
        return None, "Error: Division by zero!"
    return result, ""


def display_welcome() -> None:
    """Display welcome message and instructions."""
    print("\n" + "="*50)
    print("  CALCULATOR")
    print("="*50)
    print("\nWelcome to the Calculator!")
    print("\nInstructions:")
    print("  1. Choose an operation")
    print("  2. Enter two numbers")
    print("  3. See the result")
    print("  4. Continue or quit")
    print("\nPython Concepts: Functions, Operators, Error Handling")


def display_history(history: list[dict]) -> None:
    """Display calculation history.
    
    Args:
        history: List of calculation dictionaries
    """
    if not history:
        print("\n  No calculations yet.")
        return
    
    print("\n  📜 CALCULATION HISTORY")
    print("  " + "="*35)
    
    for i, calc in enumerate(history, 1):
        a = calc['a']
        op = calc['op']
        b = calc['b']
        result = calc['result']
        print(f"  {i}. {a} {op} {b} = {result}")


def main() -> None:
    """Main calculator loop."""
    display_welcome()
    
    history = []
    
    while True:
        op = get_operation()
        
        if op is None:
            break
        
        a = get_number("Enter first number (or 'q' to quit): ")
        if a is None:
            break
        
        b = get_number("Enter second number (or 'q' to quit): ")
        if b is None:
            break
        
        result, error = calculate(a, b, op)
        
        if error:
            print(f"\n  ❌ {error}")
        else:
            print(f"\n  ✅ Result: {a} {op} {b} = {result}")
            history.append({'a': a, 'op': op, 'b': b, 'result': result})
        
        # Show history count
        print(f"\n  (Total calculations: {len(history)})")
    
    # Show final history
    display_history(history)
    
    print("\n" + "="*50)
    print("  FINAL SUMMARY")
    print("="*50)
    print(f"  Total calculations: {len(history)}")
    
    if history:
        last = history[-1]
        print(f"  Last calculation: {last['a']} {last['op']} {last['b']} = {last['result']}")
    
    print("\nThanks for using Calculator!")
    print("See you next time!")


if __name__ == "__main__":
    main()

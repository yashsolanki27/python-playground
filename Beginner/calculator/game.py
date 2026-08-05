"""
Calculator Game
A simple calculator to learn functions, arithmetic operations, and error handling.

How to Play:
1. Enter two numbers when prompted
2. Choose an operation (+, -, *, /, **, %)
3. See the result
4. Continue calculating or exit

Python Concepts:
- Functions for each operation
- Arithmetic operators
- Error handling (division by zero)
- Input validation
- Loop for continuous calculation
- String formatting
"""

from typing import Union


def display_welcome():
    """Display welcome message and available operations."""
    print("=" * 50)
    print(" Simple Calculator")
    print("=" * 50)
    print("\nAvailable Operations:")
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print("  ** Power")
    print("  %  Modulus (Remainder)")
    print("\nEnter 'quit' at any time to exit.")
    print("-" * 50 + "\n")


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> Union[float, str]:
    """Divide a by b with zero division check."""
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def power(a: float, b: float) -> float:
    """Calculate a raised to power b."""
    return a ** b


def modulus(a: float, b: float) -> Union[float, str]:
    """Calculate remainder of a divided by b."""
    if b == 0:
        return "Error: Division by zero!"
    return a % b


def get_number(prompt: str) -> Union[float, None]:
    """
    Get a number from user input.
    
    Args:
        prompt: Input prompt message
        
    Returns:
        Float number or None if user wants to quit
    """
    while True:
        user_input = input(prompt).strip()
        
        if user_input.lower() == 'quit':
            return None
        
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_operation() -> Union[str, None]:
    """
    Get operation choice from user.
    
    Returns:
        Operation string or None if user wants to quit
    """
    valid_operations = ['+', '-', '*', '/', '**', '%']
    
    while True:
        operation = input("Enter operation (+, -, *, /, **, %): ").strip()
        
        if operation.lower() == 'quit':
            return None
        
        if operation in valid_operations:
            return operation
        
        print(f"Invalid operation! Please choose from: {', '.join(valid_operations)}")


def calculate(a: float, b: float, operation: str) -> Union[float, str]:
    """
    Perform calculation based on operation.
    
    Args:
        a: First number
        b: Second number
        operation: Operation to perform
        
    Returns:
        Result or error message
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        '%': modulus
    }
    
    return operations[operation](a, b)


def display_result(a: float, b: float, operation: str, result: Union[float, str]):
    """
    Display the calculation result.
    
    Args:
        a: First number
        b: Second number
        operation: Operation performed
        result: Calculation result
    """
    # Format operation for display
    operation_names = {
        '+': 'plus',
        '-': 'minus',
        '*': 'times',
        '/': 'divided by',
        '**': 'to the power of',
        '%': 'modulus'
    }
    
    print(f"\n{'=' * 40}")
    print(f" {a} {operation} {b} = {result}")
    print(f"{'=' * 40}\n")


def play_game():
    """Main calculator function."""
    display_welcome()
    
    calculation_count = 0
    
    while True:
        # Get first number
        a = get_number("Enter first number: ")
        if a is None:
            break
        
        # Get operation
        operation = get_operation()
        if operation is None:
            break
        
        # Get second number
        b = get_number("Enter second number: ")
        if b is None:
            break
        
        # Perform calculation
        result = calculate(a, b, operation)
        
        # Display result
        display_result(a, b, operation, result)
        
        calculation_count += 1
        
        # Ask to continue
        while True:
            continue_calc = input("Do another calculation? (yes/no): ").lower().strip()
            if continue_calc in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if continue_calc in ['no', 'n']:
            break
        
        print()  # Empty line for readability
    
    # Summary
    print(f"\n{'=' * 50}")
    print(f" Calculator Summary")
    print(f"{'=' * 50}")
    print(f" You performed {calculation_count} calculation{'s' if calculation_count != 1 else ''}")
    print(f"{'=' * 50}")
    print("\nThanks for using the calculator! Goodbye!")


def main():
    """Main entry point with play again functionality."""
    while True:
        play_game()
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to use the calculator again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            print("\nSee you next time!")
            break
        
        print("\n" + "=" * 50)
        print(" Starting new session...")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
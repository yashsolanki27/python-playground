"""
Number To Word Converter
Convert numbers to English words to learn string manipulation and math operations.

How to Play:
1. Enter a number (0-999,999,999)
2. See the number written in English words
3. Convert multiple numbers or quit

Python Concepts:
- String formatting and concatenation
- Mathematical operations (modulo, division)
- Lists for word mappings
- Functions for modular code
- Input validation
"""

# Word mappings
ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  NUMBER TO WORD CONVERTER")
    print("="*50)
    print("\nConvert numbers to English words!")
    print("\nRange: 0 to 999,999,999")
    print("\nPython Concepts: Strings, Math, Lists, Functions")


def convertHundreds(num: int) -> str:
    """Convert a number less than 1000 to words.
    
    Args:
        num: Number between 0 and 999
        
    Returns:
        Number in English words
    """
    result = ""
    
    if num >= 100:
        result += ONES[num // 100] + " hundred"
        num %= 100
        if num > 0:
            result += " and "
    
    if num >= 20:
        result += TENS[num // 10]
        num %= 10
        if num > 0:
            result += "-" + ONES[num]
    elif num >= 10:
        result += TEENS[num - 10]
    elif num > 0:
        result += ONES[num]
    
    return result.strip()


def number_to_words(num: int) -> str:
    """Convert any number to English words.
    
    Args:
        num: Number to convert (0-999,999,999)
        
    Returns:
        Number in English words
    """
    if num == 0:
        return "zero"
    
    if num < 0:
        return "negative " + number_to_words(-num)
    
    result = ""
    
    if num >= 1000000:
        result += convertHundreds(num // 1000000) + " million"
        num %= 1000000
        if num > 0:
            result += " "
    
    if num >= 1000:
        result += convertHundreds(num // 1000) + " thousand"
        num %= 1000
        if num > 0:
            result += " "
    
    if num > 0:
        if result and num < 100:
            result += "and "
        result += convertHundreds(num)
    
    return result.strip()


def get_number() -> int | None:
    """Get number from user input.
    
    Returns:
        Integer or None for quit
    """
    while True:
        user_input = input("\nEnter a number (0-999,999,999) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            num = int(user_input)
            if -999999999 <= num <= 999999999:
                return num
            print("Number must be between -999,999,999 and 999,999,999.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main() -> None:
    """Main converter loop."""
    display_welcome()
    
    conversions = 0
    
    while True:
        num = get_number()
        
        if num is None:
            break
        
        words = number_to_words(num)
        
        print(f"\n  📝 Result:")
        print(f"  Number: {num:,}")
        print(f"  Words:  {words}")
        
        conversions += 1
        print(f"\n  (Total conversions: {conversions})")
    
    print("\n" + "="*50)
    print(f"  Total conversions: {conversions}")
    print("\nThanks for using Number To Word Converter!")
    print("See you next time!")


if __name__ == "__main__":
    main()

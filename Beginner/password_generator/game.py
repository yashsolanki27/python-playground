"""
Password Generator
A secure password generation utility to learn string operations and the secrets module.

How to Play:
1. Choose password length
2. Select character types (uppercase, lowercase, digits, symbols)
3. Generate secure passwords
4. Check password strength

Python Concepts:
- secrets module for secure randomness
- String constants for character sets
- List comprehensions
- Boolean flags for options
- Password strength analysis
- Security best practices
"""

import secrets
import string


def display_welcome() -> None:
    """Display welcome message and instructions."""
    print("\n" + "="*50)
    print("  PASSWORD GENERATOR")
    print("="*50)
    print("\nWelcome to the Password Generator!")
    print("\nFeatures:")
    print("  1. Generate secure random passwords")
    print("  2. Customize character types")
    print("  3. Check password strength")
    print("  4. Generate multiple passwords at once")
    print("\nPython Concepts: secrets, strings, security")


def get_password_length() -> int:
    """Get desired password length from user.
    
    Returns:
        Password length as integer
    """
    while True:
        try:
            length = int(input("\nEnter password length (8-64): ").strip())
            if 8 <= length <= 64:
                return length
            print("Please enter a number between 8 and 64.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_character_options() -> dict[str, bool]:
    """Get character type preferences from user.
    
    Returns:
        Dictionary of character type flags
    """
    print("\n  Select character types:")
    
    options = {
        'uppercase': True,
        'lowercase': True,
        'digits': True,
        'symbols': True
    }
    
    labels = {
        'uppercase': 'Uppercase letters (A-Z)',
        'lowercase': 'Lowercase letters (a-z)',
        'digits': 'Digits (0-9)',
        'symbols': 'Symbols (!@#$%^&*)'
    }
    
    for key, label in labels.items():
        current = "Yes" if options[key] else "No"
        while True:
            choice = input(f"  Include {label}? (yes/no) [{current}]: ").strip().lower()
            if choice in ['yes', 'y', '']:
                options[key] = True
                break
            elif choice in ['no', 'n']:
                options[key] = False
                break
            print("  Please enter 'yes' or 'no'.")
    
    # Ensure at least one option is selected
    if not any(options.values()):
        print("\n  At least one character type must be selected!")
        print("  Defaulting to all types.")
        options = {k: True for k in options}
    
    return options


def generate_password(length: int, options: dict[str, bool]) -> str:
    """Generate a secure random password.
    
    Args:
        length: Desired password length
        options: Character type preferences
        
    Returns:
        Generated password string
    """
    # Build character pool
    char_pool = ""
    
    if options['uppercase']:
        char_pool += string.ascii_uppercase
    if options['lowercase']:
        char_pool += string.ascii_lowercase
    if options['digits']:
        char_pool += string.digits
    if options['symbols']:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not char_pool:
        char_pool = string.ascii_letters + string.digits
    
    # Generate password using secrets for security
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    
    return password


def check_password_strength(password: str) -> dict[str, any]:
    """Analyze password strength.
    
    Args:
        password: Password to analyze
        
    Returns:
        Dictionary with strength analysis
    """
    analysis = {
        'length': len(password),
        'has_upper': any(c.isupper() for c in password),
        'has_lower': any(c.islower() for c in password),
        'has_digit': any(c.isdigit() for c in password),
        'has_symbol': any(c in string.punctuation for c in password),
        'unique_chars': len(set(password)),
        'score': 0,
        'strength': ''
    }
    
    # Calculate score
    score = 0
    
    # Length score
    if analysis['length'] >= 12:
        score += 25
    elif analysis['length'] >= 8:
        score += 15
    
    # Character variety
    if analysis['has_upper']:
        score += 15
    if analysis['has_lower']:
        score += 15
    if analysis['has_digit']:
        score += 15
    if analysis['has_symbol']:
        score += 20
    
    # Uniqueness bonus
    if analysis['unique_chars'] >= analysis['length'] * 0.8:
        score += 10
    
    analysis['score'] = min(score, 100)
    
    # Determine strength label
    if score >= 80:
        analysis['strength'] = '🔴 STRONG'
    elif score >= 60:
        analysis['strength'] = '🟠 MODERATE'
    elif score >= 40:
        analysis['strength'] = '🟡 FAIR'
    else:
        analysis['strength'] = '🟢 WEAK'
    
    return analysis


def display_strength(analysis: dict[str, any]) -> None:
    """Display password strength analysis.
    
    Args:
        analysis: Password analysis dictionary
    """
    print("\n  📊 PASSWORD STRENGTH")
    print("  " + "="*35)
    print(f"  Length:        {analysis['length']} characters")
    print(f"  Uppercase:     {'✅' if analysis['has_upper'] else '❌'}")
    print(f"  Lowercase:     {'✅' if analysis['has_lower'] else '❌'}")
    print(f"  Digits:        {'✅' if analysis['has_digit'] else '❌'}")
    print(f"  Symbols:       {'✅' if analysis['has_symbol'] else '❌'}")
    print(f"  Unique chars:  {analysis['unique_chars']}")
    print(f"  Score:         {analysis['score']}/100")
    print(f"  Strength:      {analysis['strength']}")


def generate_multiple(length: int, options: dict[str, bool], count: int) -> list[str]:
    """Generate multiple passwords.
    
    Args:
        length: Password length
        options: Character options
        count: Number of passwords to generate
        
    Returns:
        List of generated passwords
    """
    return [generate_password(length, options) for _ in range(count)]


def main() -> None:
    """Main password generator loop."""
    display_welcome()
    
    while True:
        print("\n  Options:")
        print("  1. Generate a password")
        print("  2. Generate multiple passwords")
        print("  3. Check password strength")
        print("  4. Quit")
        
        choice = input("\nYour choice (1-4): ").strip()
        
        if choice == '1':
            length = get_password_length()
            options = get_character_options()
            password = generate_password(length, options)
            
            print(f"\n  🔐 Generated Password:")
            print(f"  {password}")
            
            analysis = check_password_strength(password)
            display_strength(analysis)
        
        elif choice == '2':
            length = get_password_length()
            options = get_character_options()
            
            while True:
                try:
                    count = int(input("How many passwords? (1-10): ").strip())
                    if 1 <= count <= 10:
                        break
                    print("Please enter 1-10.")
                except ValueError:
                    print("Invalid input.")
            
            passwords = generate_multiple(length, options, count)
            
            print(f"\n  🔐 Generated Passwords:")
            for i, pwd in enumerate(passwords, 1):
                print(f"  {i}. {pwd}")
        
        elif choice == '3':
            password = input("\nEnter password to check: ").strip()
            if password:
                analysis = check_password_strength(password)
                display_strength(analysis)
            else:
                print("No password entered.")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")
    
    print("\nThanks for using Password Generator!")
    print("Stay secure! 🔒")


if __name__ == "__main__":
    main()

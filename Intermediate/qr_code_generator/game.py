"""
QR Code Generator
Generate ASCII QR codes. Learn encoding and ASCII art.

How to Play:
1. Enter text or URL
2. See ASCII QR code
3. Copy or save the output

Python Concepts:
- String encoding
- Binary representation
- ASCII art generation
- Hash functions
"""

import hashlib


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  📱 QR CODE GENERATOR")
    print("="*50)
    print("\nGenerate ASCII QR codes!")
    print("\nPython Concepts: Encoding, ASCII Art, Hashing")


def generate_pattern(text: str, size: int = 21) -> list[list[int]]:
    """Generate a QR-like pattern from text.
    
    Args:
        text: Input text
        size: Pattern size
        
    Returns:
        2D grid of 0s and 1s
    """
    # Create a simple hash-based pattern
    text_hash = hashlib.md5(text.encode()).hexdigest()
    
    # Initialize grid
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    # Add finder patterns (corners)
    for i in range(7):
        for j in range(7):
            # Top-left
            if i < size and j < size:
                if i == 0 or i == 6 or j == 0 or j == 6 or (2 <= i <= 4 and 2 <= j <= 4):
                    grid[i][j] = 1
            # Top-right
            if i < size and size-7+j < size:
                if i == 0 or i == 6 or j == 0 or j == 6 or (2 <= i <= 4 and 2 <= j <= 4):
                    grid[i][size-7+j] = 1
            # Bottom-left
            if size-7+i < size and j < size:
                if i == 0 or i == 6 or j == 0 or j == 6 or (2 <= i <= 4 and 2 <= j <= 4):
                    grid[size-7+i][j] = 1
    
    # Fill data area with hash pattern
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                # Use hash to determine if cell is filled
                idx = (i * size + j) % len(text_hash)
                hex_val = int(text_hash[idx], 16)
                if hex_val % 3 == 0:
                    grid[i][j] = 1
    
    return grid


def text_to_qr(text: str) -> str:
    """Convert text to ASCII QR representation.
    
    Args:
        text: Input text
        
    Returns:
        ASCII string representation
    """
    size = 21
    grid = generate_pattern(text, size)
    
    # Convert to ASCII
    lines = []
    for row in grid:
        line = ""
        for cell in row:
            if cell == 1:
                line += "██"
            else:
                line += "  "
        lines.append(line)
    
    return "\n".join(lines)


def main() -> None:
    """Main generator loop."""
    display_welcome()
    
    generated = 0
    
    while True:
        print("\n  Options:")
        print("  1. Generate QR code")
        print("  2. Quit")
        
        choice = input("\n  Your choice (1-2): ").strip()
        
        if choice == '1':
            text = input("\n  Enter text or URL: ").strip()
            if not text:
                print("  Please enter some text!")
                continue
            
            print(f"\n  📱 QR Code for: {text[:30]}...")
            print("  " + "="*44)
            print(text_to_qr(text))
            print("  " + "="*44)
            
            generated += 1
            print(f"\n  (Total generated: {generated})")
        
        elif choice == '2':
            break
        
        else:
            print("  Invalid choice!")
    
    print("\nThanks for using QR Code Generator!")
    print("See you next time!")


if __name__ == "__main__":
    main()

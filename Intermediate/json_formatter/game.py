"""
JSON Formatter
Format, validate, and minify JSON data. Learn JSON processing and validation.

How to Play:
1. Enter JSON data or load from file
2. Pretty print or minify
3. Validate JSON structure
4. Save formatted output

Python Concepts:
- JSON module
- String formatting
- Error handling
- File I/O
"""

import json
import os


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  📋 JSON FORMATTER")
    print("="*50)
    print("\nFormat, validate, and minify JSON!")
    print("\nPython Concepts: JSON, Error Handling, File I/O")


def get_json_input() -> str | None:
    """Get JSON input from user.
    
    Returns:
        JSON string or None for quit
    """
    print("\n  Input options:")
    print("  1. Type JSON")
    print("  2. Load from file")
    print("  3. Quit")
    
    choice = input("\n  Your choice (1-3): ").strip()
    
    if choice == '1':
        print("\n  Enter JSON (type 'END' on new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        return '\n'.join(lines)
    
    elif choice == '2':
        filename = input("\n  Enter filename: ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("  File not found!")
            return None
    
    return None


def format_json(json_str: str, indent: int = 2) -> str:
    """Format JSON with indentation.
    
    Args:
        json_str: Raw JSON string
        indent: Indentation spaces
        
    Returns:
        Formatted JSON string
    """
    data = json.loads(json_str)
    return json.dumps(data, indent=indent, ensure_ascii=False)


def minify_json(json_str: str) -> str:
    """Minify JSON (remove whitespace).
    
    Args:
        json_str: Raw JSON string
        
    Returns:
        Minified JSON string
    """
    data = json.loads(json_str)
    return json.dumps(data, separators=(',', ':'), ensure_ascii=False)


def validate_json(json_str: str) -> tuple[bool, str]:
    """Validate JSON structure.
    
    Args:
        json_str: JSON string to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    try:
        data = json.loads(json_str)
        json_type = type(data).__name__
        return True, f"Valid JSON! Type: {json_type}"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"


def analyze_json(json_str: str) -> None:
    """Analyze and display JSON structure.
    
    Args:
        json_str: JSON string
    """
    data = json.loads(json_str)
    
    print("\n  📊 JSON Analysis:")
    print("  " + "-"*30)
    print(f"  Type: {type(data).__name__}")
    
    if isinstance(data, dict):
        print(f"  Keys: {len(data)}")
        for key in data:
            print(f"    - {key}: {type(data[key]).__name__}")
    elif isinstance(data, list):
        print(f"  Items: {len(data)}")
        if data:
            print(f"  First item type: {type(data[0]).__name__}")
    elif isinstance(data, str):
        print(f"  Length: {len(data)} characters")
    elif isinstance(data, (int, float)):
        print(f"  Value: {data}")


def main() -> None:
    """Main formatter loop."""
    display_welcome()
    
    operations = 0
    
    while True:
        json_str = get_json_input()
        
        if json_str is None:
            break
        
        # Validate first
        is_valid, message = validate_json(json_str)
        
        if not is_valid:
            print(f"\n  ❌ {message}")
            continue
        
        print(f"\n  ✅ {message}")
        
        analyze_json(json_str)
        
        print("\n  Options:")
        print("  1. Pretty print")
        print("  2. Minify")
        print("  3. Validate only")
        print("  4. Save to file")
        print("  5. Continue")
        
        choice = input("\n  Your choice (1-5): ").strip()
        
        if choice == '1':
            formatted = format_json(json_str)
            print("\n  📄 Pretty Print:")
            print("  " + "="*40)
            print(formatted)
            print("  " + "="*40)
        
        elif choice == '2':
            minified = minify_json(json_str)
            print(f"\n  📄 Minified ({len(minified)} chars):")
            print("  " + "="*40)
            print(minified)
            print("  " + "="*40)
        
        elif choice == '3':
            print(f"\n  ✅ {message}")
        
        elif choice == '4':
            filename = input("\n  Enter filename (e.g., output.json): ").strip()
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(format_json(json_str))
                print(f"  ✅ Saved to {filename}")
            except Exception as e:
                print(f"  ❌ Error saving: {e}")
        
        operations += 1
        print(f"\n  (Total operations: {operations})")
    
    print("\nThanks for using JSON Formatter!")
    print("See you next time!")


if __name__ == "__main__":
    main()

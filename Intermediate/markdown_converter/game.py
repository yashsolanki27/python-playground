"""
Markdown to HTML Converter
Convert markdown text to HTML. Learn string processing and file operations.

How to Play:
1. Enter markdown text or load from file
2. See the HTML output
3. Save to file if needed

Python Concepts:
- String manipulation
- Regular expressions
- File I/O
- Text processing
"""

import re
import os


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  MARKDOWN TO HTML CONVERTER")
    print("="*50)
    print("\nConvert markdown to HTML!")
    print("\nSupported syntax:")
    print("  # Heading 1, ## Heading 2, etc.")
    print("  **bold**, *italic*")
    print("  - list items")
    print("  [link](url)")
    print("  `code`")
    print("\nPython Concepts: Regex, String Processing, File I/O")


def markdown_to_html(markdown: str) -> str:
    """Convert markdown text to HTML.
    
    Args:
        markdown: Markdown text
        
    Returns:
        HTML string
    """
    html = markdown
    
    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and Italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    # Unordered lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\n\g<0></ul>', html)
    
    # Paragraphs (lines not starting with <)
    lines = html.split('\n')
    result = []
    for line in lines:
        if line.strip() and not line.startswith('<'):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    html = '\n'.join(result)
    
    return html


def get_input() -> str | None:
    """Get markdown input from user.
    
    Returns:
        Markdown text or None for quit
    """
    print("\n  Input options:")
    print("  1. Type markdown")
    print("  2. Load from file")
    print("  3. Quit")
    
    choice = input("\n  Your choice (1-3): ").strip()
    
    if choice == '1':
        print("\n  Enter markdown (type 'END' on new line to finish):")
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


def main() -> None:
    """Main converter loop."""
    display_welcome()
    
    conversions = 0
    
    while True:
        markdown = get_input()
        
        if markdown is None:
            break
        
        html = markdown_to_html(markdown)
        
        print("\n  📄 HTML Output:")
        print("  " + "="*40)
        print(html)
        print("  " + "="*40)
        
        conversions += 1
        
        # Save option
        save = input("\n  Save to file? (yes/no): ").strip().lower()
        if save in ['yes', 'y']:
            filename = input("  Enter filename (e.g., output.html): ").strip()
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"  ✅ Saved to {filename}")
            except Exception as e:
                print(f"  ❌ Error saving: {e}")
        
        print(f"\n  (Total conversions: {conversions})")
    
    print("\nThanks for using Markdown Converter!")
    print("See you next time!")


if __name__ == "__main__":
    main()

# Markdown to HTML Converter

## Description
Convert markdown text to HTML instantly! Supports headers, bold, italic, links, lists, and code blocks.

## How to Play
1. Run the game: `python game.py`
2. Type markdown or load from file
3. See the HTML output
4. Save to file if needed

## Python Concepts Learned
- **Regular Expressions**: Pattern matching
- **String Manipulation**: Text transformation
- **File I/O**: Reading and writing files
- **Text Processing**: Parsing markdown

## Supported Markdown
| Markdown | HTML |
|----------|------|
| # Header | `<h1>Header</h1>` |
| **bold** | `<strong>bold</strong>` |
| *italic* | `<em>italic</em>` |
| `code` | `<code>code</code>` |
| [link](url) | `<a href="url">link</a>` |
| - item | `<li>item</li>` |

## Sample Output
```
==================================================
  MARKDOWN TO HTML CONVERTER
==================================================

  Enter markdown (type 'END' on new line to finish):
  # Hello World
  This is **bold** and *italic*.
  - Item 1
  - Item 2
  END

  📄 HTML Output:
  ========================================
  <h1>Hello World</h1>
  <p>This is <strong>bold</strong> and <em>italic</em>.</p>
  <ul>
  <li>Item 1</li>
  <li>Item 2</li>
  </ul>
  ========================================

  Save to file? (yes/no): y
  Enter filename: output.html
  ✅ Saved to output.html
```

## Code Structure
```
markdown_converter/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add more markdown syntax
- [ ] Support images
- [ ] Add table conversion
- [ ] Create preview mode

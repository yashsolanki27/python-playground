# JSON Formatter

## Description
Format, validate, and minify JSON data! A useful utility for developers working with APIs and data files.

## How to Play
1. Run the game: `python game.py`
2. Enter JSON data or load from file
3. Pretty print or minify
4. Analyze structure
5. Save output

## Python Concepts Learned
- **JSON Module**: Parsing and dumping
- **Error Handling**: Invalid JSON detection
- **String Formatting**: Pretty printing
- **File I/O**: Save/load operations

## Features
| Feature | Description |
|---------|-------------|
| Pretty Print | Format with indentation |
| Minify | Remove all whitespace |
| Validate | Check JSON syntax |
| Analyze | Show structure details |

## Sample Output
```
==================================================
  📋 JSON FORMATTER
==================================================

  Enter JSON (type 'END' on new line to finish):
  {"name": "John", "age": 30, "city": "NYC"}
  END

  ✅ Valid JSON! Type: dict

  📊 JSON Analysis:
  ------------------------------
  Type: dict
  Keys: 3
    - name: str
    - age: int
    - city: str

  Options:
  1. Pretty print
  2. Minify
  3. Validate only
  4. Save to file
  5. Continue

  Your choice (1-5): 1

  📄 Pretty Print:
  ========================================
  {
    "name": "John",
    "age": 30,
    "city": "NYC"
  }
  ========================================
```

## Code Structure
```
json_formatter/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add JSON editing
- [ ] Support JSON Path queries
- [ ] Add diff comparison
- [ ] Create JSON schema validation

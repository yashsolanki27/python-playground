# Unit Converter

## Description
Convert between different units of measurement - length, weight, and speed!

## How to Play
1. Run: `python game.py`
2. Select category (length/weight/speed)
3. Enter value and select units
4. See the converted result

## Python Concepts
- Dictionaries for conversion factors
- Nested data structures
- Functions and modularity

## Supported Units
| Category | Units |
|----------|-------|
| Length | meter, km, cm, mm, mile, yard, foot, inch |
| Weight | kg, gram, mg, pound, ounce, ton |
| Speed | m/s, km/h, mph, knot, ft/s |

## Sample Output
```
  Categories:
  1. Length
  2. Weight
  3. Speed
  4. Quit

  Select (1-4): 1

  Enter value: 1

  From unit:
    1. meter
    2. kilometer
    ...
  Select: 1

  To unit:
    1. meter
    2. kilometer
    ...
  Select: 8

  ✅ 1.0 meter = 39.3701 inch
```

## Future Enhancements
- [ ] Add temperature conversions
- [ ] Add area and volume
- [ ] Save conversion history
- [ ] Create favorites list

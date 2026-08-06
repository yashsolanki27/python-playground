"""
Unit Converter
Convert between different units of measurement.

How to Play:
1. Select conversion type (length, weight, speed)
2. Enter value and units
3. See converted result

Python Concepts:
- Dictionaries for conversion factors
- Functions for each category
- User input validation
"""


CONVERSIONS = {
    'length': {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'mile': 0.000621371,
        'yard': 1.09361,
        'foot': 3.28084,
        'inch': 39.3701
    },
    'weight': {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1000000,
        'pound': 2.20462,
        'ounce': 35.274,
        'ton': 0.001
    },
    'speed': {
        'm/s': 1,
        'km/h': 3.6,
        'mph': 2.23694,
        'knot': 1.94384,
        'ft/s': 3.28084
    }
}


def convert(value: float, from_unit: str, to_unit: str, category: str) -> float:
    factors = CONVERSIONS[category]
    base_value = value / factors[from_unit]
    return base_value * factors[to_unit]


def show_units(category: str):
    units = list(CONVERSIONS[category].keys())
    for i, u in enumerate(units, 1):
        print(f"    {i}. {u}")
    return units


def main():
    print("\n" + "="*50)
    print("  📏 UNIT CONVERTER")
    print("="*50)
    print("\nConvert between different units!")
    print("\nPython Concepts: Dictionaries, Functions, Math")
    
    while True:
        print("\n  Categories:")
        print("  1. Length")
        print("  2. Weight")
        print("  3. Speed")
        print("  4. Quit")
        
        choice = input("\n  Select (1-4): ").strip()
        
        if choice == '4':
            break
        
        categories = {'1': 'length', '2': 'weight', '3': 'speed'}
        if choice not in categories:
            print("  Invalid choice!")
            continue
        
        category = categories[choice]
        
        val = input("\n  Enter value: ").strip()
        try:
            value = float(val)
        except ValueError:
            print("  Invalid number!")
            continue
        
        print(f"\n  From unit:")
        from_units = show_units(category)
        try:
            from_idx = int(input("  Select: ").strip()) - 1
            from_unit = from_units[from_idx]
        except (ValueError, IndexError):
            print("  Invalid choice!")
            continue
        
        print(f"\n  To unit:")
        to_units = show_units(category)
        try:
            to_idx = int(input("  Select: ").strip()) - 1
            to_unit = to_units[to_idx]
        except (ValueError, IndexError):
            print("  Invalid choice!")
            continue
        
        result = convert(value, from_unit, to_unit, category)
        
        print(f"\n  ✅ {value} {from_unit} = {result:.4f} {to_unit}")
    
    print("\nThanks for using Unit Converter!")


if __name__ == "__main__":
    main()

"""
Temperature Converter
Convert between Celsius, Fahrenheit, and Kelvin.

How to Play:
1. Enter temperature value
2. Select source unit
3. Select target unit
4. See converted result

Python Concepts:
- Arithmetic operations
- Functions
- User input validation
"""


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

def celsius_to_kelvin(c: float) -> float:
    return c + 273.15

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f: float) -> float:
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k: float) -> float:
    return k - 273.15

def kelvin_to_fahrenheit(k: float) -> float:
    return (k - 273.15) * 9/5 + 32


def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    
    conversions = {
        ('C', 'F'): celsius_to_fahrenheit,
        ('C', 'K'): celsius_to_kelvin,
        ('F', 'C'): fahrenheit_to_celsius,
        ('F', 'K'): fahrenheit_to_kelvin,
        ('K', 'C'): kelvin_to_celsius,
        ('K', 'F'): kelvin_to_fahrenheit,
    }
    
    return conversions[(from_unit, to_unit)](value)


def main():
    print("\n" + "="*50)
    print("  TEMPERATURE CONVERTER")
    print("="*50)
    
    units = {'1': 'C', '2': 'F', '3': 'K'}
    unit_names = {'C': 'Celsius', 'F': 'Fahrenheit', 'K': 'Kelvin'}
    
    while True:
        val = input("\nEnter temperature (or 'q' to quit): ").strip()
        if val.lower() == 'q':
            break
        
        try:
            value = float(val)
        except ValueError:
            print("Invalid number!")
            continue
        
        print("\nFrom: 1=Celsius, 2=Fahrenheit, 3=Kelvin")
        from_u = input("Select (1/2/3): ").strip()
        if from_u not in units:
            print("Invalid choice!")
            continue
        
        print("\nTo: 1=Celsius, 2=Fahrenheit, 3=Kelvin")
        to_u = input("Select (1/2/3): ").strip()
        if to_u not in units:
            print("Invalid choice!")
            continue
        
        result = convert(value, units[from_u], units[to_u])
        
        print(f"\n  ✅ {value}°{units[from_u]} = {result:.2f}°{units[to_u]}")
        print(f"  ({unit_names[units[from_u]]} to {unit_names[units[to_u]]})")
    
    print("\nThanks for using Temperature Converter!")


if __name__ == "__main__":
    main()

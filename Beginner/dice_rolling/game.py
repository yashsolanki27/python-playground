"""
Dice Rolling Simulator
A dice rolling game to learn random module, lists, and statistics.

How to Play:
1. Choose how many dice to roll (1-6)
2. Roll the dice and see ASCII art results
3. Track your roll history and statistics
4. Try to reach target combinations

Python Concepts:
- Random module for dice rolls
- Lists for storing roll history
- Dictionaries for statistics
- ASCII art for visual display
- Loops and conditionals
- Statistics calculation
"""

import random


# ASCII art for dice faces
DICE_ART = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  DICE ROLLING SIMULATOR")
    print("="*50)
    print("\nWelcome to the Dice Rolling Simulator!")
    print("\nRules:")
    print("  1. Choose how many dice to roll (1-6)")
    print("  2. See ASCII art of each die")
    print("  3. Track your roll history and stats")
    print("  4. Try to roll specific combinations!")
    print("\nPython Concepts: Random, Lists, Statistics, ASCII Art")


def roll_dice(count: int) -> list[int]:
    """Roll multiple dice and return results.
    
    Args:
        count: Number of dice to roll
        
    Returns:
        List of dice values (1-6)
    """
    return [random.randint(1, 6) for _ in range(count)]


def display_dice(rolls: list[int]) -> None:
    """Display dice rolls as ASCII art.
    
    Args:
        rolls: List of dice values
    """
    if not rolls:
        print("  No dice to display.")
        return
    
    # Print all dice side by side
    print("\n  Your rolls:")
    print()
    
    # Print top border of all dice
    for dice in rolls:
        print(f"  {DICE_ART[dice][0]}", end="  ")
    print()
    
    # Print middle rows
    for row in range(1, 4):
        for dice in rolls:
            print(f"  {DICE_ART[dice][row]}", end="  ")
        print()
    
    # Print bottom border
    for dice in rolls:
        print(f"  {DICE_ART[dice][4]}", end="  ")
    print()
    
    # Print values
    print()
    for i, dice in enumerate(rolls, 1):
        print(f"  Die {i}: {dice}", end="    ")
    print()
    
    total = sum(rolls)
    print(f"\n  Total: {total}")


def get_dice_count() -> int:
    """Get number of dice from player.
    
    Returns:
        Number of dice (1-6)
    """
    while True:
        try:
            count = int(input("\nHow many dice to roll? (1-6): ").strip())
            if 1 <= count <= 6:
                return count
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_combinations(rolls: list[int]) -> list[str]:
    """Check for special dice combinations.
    
    Args:
        rolls: List of dice values
        
    Returns:
        List of combination names found
    """
    combinations = []
    total = sum(rolls)
    
    if len(rolls) >= 2:
        # Check for pairs
        if len(rolls) == 2 and rolls[0] == rolls[1]:
            combinations.append("🎯 Double!")
        
        # Check for three of a kind
        if len(rolls) >= 3:
            from collections import Counter
            counts = Counter(rolls)
            for value, count in counts.items():
                if count >= 3:
                    combinations.append(f"🔥 Triple {value}s!")
                if count >= 4:
                    combinations.append(f"💎 Four {value}s!")
                if count >= 5:
                    combinations.append(f"👑 Five {value}s!")
                if count >= 6:
                    combinations.append(f"🏆 SIX OF A KIND! LEGENDARY!")
    
    # Check for specific totals
    if total == 7:
        combinations.append("🍀 Lucky 7!")
    elif total == 11:
        combinations.append("⚡ Lucky 11!")
    elif total == len(rolls) * 6:
        combinations.append("🌟 MAXIMUM ROLLS!")
    elif total == len(rolls):
        combinations.append("🎯 MINIMUM ROLLS!")
    
    # Check for straight (1,2,3,4,5,6)
    if len(rolls) == 6 and sorted(rolls) == [1, 2, 3, 4, 5, 6]:
        combinations.append("🌈 STRAIGHT! Perfect sequence!")
    
    return combinations


def display_statistics(history: list[list[int]]) -> None:
    """Display roll statistics.
    
    Args:
        history: List of all rolls
    """
    if not history:
        print("\n  No rolls yet!")
        return
    
    all_rolls = [dice for roll in history for dice in roll]
    total_rolls = len(all_rolls)
    total_sum = sum(all_rolls)
    
    print("\n  📊 ROLL STATISTICS")
    print("  " + "="*35)
    print(f"  Total dice rolled:  {total_rolls}")
    print(f"  Total sum:          {total_sum}")
    print(f"  Average:            {total_sum/total_rolls:.2f}")
    print(f"  Highest single:     {max(all_rolls)}")
    print(f"  Lowest single:      {min(all_rolls)}")
    print(f"  Number of rolls:    {len(history)}")
    
    # Frequency distribution
    from collections import Counter
    freq = Counter(all_rolls)
    print("\n  Frequency:")
    for value in range(1, 7):
        count = freq.get(value, 0)
        bar = "█" * count
        print(f"    {value}: {bar} ({count})")


def main() -> None:
    """Main game loop."""
    display_welcome()
    
    history = []
    
    while True:
        count = get_dice_count()
        rolls = roll_dice(count)
        
        display_dice(rolls)
        
        combinations = check_combinations(rolls)
        if combinations:
            print("\n  🎉 COMBINATIONS:")
            for combo in combinations:
                print(f"    {combo}")
        
        history.append(rolls)
        
        # Show roll count
        print(f"\n  (Total rolls: {len(history)})")
        
        # Ask to continue
        choice = input("\nRoll again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            break
    
    # Show final statistics
    display_statistics(history)
    
    print("\n" + "="*50)
    print("  FINAL SUMMARY")
    print("="*50)
    print(f"  Total rolls: {len(history)}")
    if history:
        all_rolls = [dice for roll in history for dice in roll]
        print(f"  Total dice rolled: {len(all_rolls)}")
        print(f"  Grand total: {sum(all_rolls)}")
    
    print("\nThanks for playing Dice Rolling Simulator!")
    print("See you next time!")


if __name__ == "__main__":
    main()

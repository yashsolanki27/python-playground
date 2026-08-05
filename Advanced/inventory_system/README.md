# Inventory System

## Description
A text-based RPG inventory management system! Add items, equip gear, use potions, and manage your character's inventory with persistent save/load functionality.

## How to Play
1. Run the game: `python game.py`
2. Create your character
3. Add items to your inventory
4. Equip weapons and armor
5. Use potions and food
6. Buy items from the shop
7. Save and load your progress!

## Python Concepts Learned
- **Object-Oriented Programming**: Item, Player, and InventorySystem classes
- **File I/O**: JSON save/load system
- **Data Persistence**: Saving game progress
- **Dictionary Operations**: Converting objects to/from dicts
- **List Management**: Inventory operations
- **Error Handling**: Try-except blocks
- **Menu-Driven Interface**: User interaction

## Game Features

### Item Types
- **Weapons**: Equip to increase attack
- **Armor**: Equip to increase defense
- **Potions**: Use to restore health
- **Food**: Use to restore hunger
- **Misc**: Special items

### Player Stats
- Health: Hit points
- Attack: Damage dealt
- Defense: Damage reduction
- Gold: Currency for shop

### Save System
- Automatic JSON save file
- Load previous progress
- Track save timestamps

## Sample Output
```
============================================================
 INVENTORY SYSTEM
============================================================

Welcome to the RPG Inventory Manager!
Manage your items, equip gear, and become stronger!
------------------------------------------------------------

Enter your character's name (or press Enter for 'Hero'): Adventurer

Welcome, Adventurer!

=== MAIN MENU ===
1. View Inventory
2. View Stats
3. Use Item
4. Equip Item
5. Add Item (Demo)
6. Drop Item
7. Shop
8. Save Game
9. Load Game
0. Quit
----------------------------------------

Enter your choice (0-9): 5

Added 7 demo items to your inventory!

=== MAIN MENU ===
1. View Inventory
...

Enter your choice (0-9): 1

=== INVENTORY ===
1. Health Potion (x1) - Restores 25 health
2. Mana Potion (x1) - Restores 25 mana
3. Bread (x1) - Restores 10 hunger
4. Apple (x1) - Restores 5 hunger
5. Iron Sword (x1) - A sturdy iron sword
6. Leather Armor (x1) - Basic leather armor
7. Magic Ring (x1) - A mysterious ring

Gold: 100

=== MAIN MENU ===
...
Enter your choice (0-9): 4

Equippable items:
1. Iron Sword (weapon)
2. Leather Armor (armor)

Enter item number to equip: 1

You equipped Iron Sword!

=== MAIN MENU ===
...
Enter your choice (0-9): 2

=== Adventurer's STATS ===
Health: 100/100
Attack: 25
Defense: 5
Gold: 100

Equipped Weapon: Iron Sword
Equipped Armor: None
Items in Inventory: 6

=== MAIN MENU ===
...
Enter your choice (0-9): 8

Game saved successfully!

=== MAIN MENU ===
...
Enter your choice (0-9): 0

Save before quitting? (yes/no): yes

Game saved successfully!

Thanks for playing! Goodbye!
```

## Code Structure
```
inventory_system/
├── game.py           # Main game file (400 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Classes

### Item Class
- `name`: Item name
- `description`: Item description
- `item_type`: Type (weapon, armor, potion, food, misc)
- `value`: Item value/cost
- `quantity`: Number of items
- `use()`: Use the item
- `to_dict()/from_dict()`: Serialization

### Player Class
- `name`: Character name
- `health/max_health`: Health points
- `attack/defense`: Stats
- `gold`: Currency
- `inventory`: List of Items
- `equipped_weapon/armor`: Equipped gear
- `add_item()`: Add to inventory
- `remove_item()`: Remove from inventory
- `use_item()`: Use an item
- `equip_item()`: Equip weapon/armor

### InventorySystem Class
- `player`: Player object
- `running`: Game state
- `run()`: Main game loop
- `save_game()`: Save to JSON
- `load_game()`: Load from JSON

## Key Functions
- `display_welcome()`: Shows intro
- `display_menu()`: Shows main menu
- `add_demo_items()`: Adds test items
- `shop_menu()`: Buy items with gold
- `save_game()`: JSON file save
- `load_game()`: JSON file load

## Save System
- File: `player_save.json`
- Format: JSON
- Includes: Player stats, inventory, equipped items
- Timestamp: Last save time

## Shop System
- Buy items with gold
- Various item types available
- Gold deduction on purchase
- Inventory management

## Error Handling
- Input validation for menus
- File I/O error handling
- Invalid item selection
- Not enough gold handling

## Future Enhancements
- [ ] Add combat system
- [ ] Create multiple characters
- [ ] Add item crafting
- [ ] Implement item trading
- [ ] Add item rarity system
- [ ] Create quest system
- [ ] Add visual inventory
- [ ] Implement item stacking rules
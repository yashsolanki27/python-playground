"""
Inventory System
A text-based RPG inventory system to learn OOP, file I/O, and data management.

How to Play:
1. Add items to your inventory
2. Use items for different effects
3. Drop items you don't need
4. View your inventory and stats
5. Save and load your progress!

Python Concepts:
- Object-Oriented Programming
- File I/O (JSON)
- Data persistence
- Dictionary operations
- List management
- Error handling
- Menu-driven interface
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class Item:
    """Represents an inventory item."""
    
    def __init__(self, name: str, description: str, item_type: str, 
                 value: int, quantity: int = 1):
        self.name = name
        self.description = description
        self.item_type = item_type  # weapon, armor, potion, food, misc
        self.value = value
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert item to dictionary for saving."""
        return {
            'name': self.name,
            'description': self.description,
            'item_type': self.item_type,
            'value': self.value,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Item':
        """Create item from dictionary."""
        return cls(
            name=data['name'],
            description=data['description'],
            item_type=data['item_type'],
            value=data['value'],
            quantity=data['quantity']
        )
    
    def use(self) -> Tuple[str, int]:
        """
        Use the item and return effect.
        
        Returns:
            Tuple of (effect_message, stat_change)
        """
        if self.item_type == 'potion':
            return f"You drink the {self.name}. Health restored!", 25
        elif self.item_type == 'food':
            return f"You eat the {self.name}. Hunger satisfied!", 10
        elif self.item_type == 'weapon':
            return f"You equip the {self.name}. Attack increased!", 5
        elif self.item_type == 'armor':
            return f"You wear the {self.name}. Defense increased!", 5
        else:
            return f"You examine the {self.name}. Nothing special happens.", 0
    
    def __str__(self) -> str:
        return f"{self.name} (x{self.quantity}) - {self.description}"


class Player:
    """Represents the player character."""
    
    def __init__(self, name: str = "Hero"):
        self.name = name
        self.health: int = 100
        self.max_health: int = 100
        self.attack: int = 10
        self.defense: int = 5
        self.gold: int = 100
        self.inventory: List[Item] = []
        self.equipped_weapon: Optional[Item] = None
        self.equipped_armor: Optional[Item] = None
    
    def add_item(self, item: Item) -> bool:
        """
        Add item to inventory.
        
        Args:
            item: Item to add
            
        Returns:
            True if successful
        """
        # Check if item already exists
        for existing_item in self.inventory:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                return True
        
        # Add new item
        self.inventory.append(item)
        return True
    
    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        """
        Remove item from inventory.
        
        Args:
            item_name: Name of item to remove
            quantity: Quantity to remove
            
        Returns:
            True if successful
        """
        for i, item in enumerate(self.inventory):
            if item.name == item_name:
                if item.quantity > quantity:
                    item.quantity -= quantity
                    return True
                elif item.quantity == quantity:
                    self.inventory.pop(i)
                    return True
                else:
                    return False
        return False
    
    def use_item(self, item_name: str) -> Tuple[bool, str]:
        """
        Use an item from inventory.
        
        Args:
            item_name: Name of item to use
            
        Returns:
            Tuple of (success, message)
        """
        for item in self.inventory:
            if item.name == item_name:
                effect, stat_change = item.use()
                
                # Apply effect based on item type
                if item.item_type in ['potion', 'food']:
                    self.health = min(self.max_health, self.health + stat_change)
                elif item.item_type == 'weapon':
                    self.attack += stat_change
                elif item.item_type == 'armor':
                    self.defense += stat_change
                
                # Remove one quantity
                self.remove_item(item_name, 1)
                
                return True, effect
        
        return False, f"You don't have {item_name} in your inventory!"
    
    def equip_item(self, item_name: str) -> Tuple[bool, str]:
        """
        Equip a weapon or armor.
        
        Args:
            item_name: Name of item to equip
            
        Returns:
            Tuple of (success, message)
        """
        for item in self.inventory:
            if item.name == item_name:
                if item.item_type == 'weapon':
                    if self.equipped_weapon:
                        # Unequip current weapon
                        self.attack -= self.equipped_weapon.value
                        self.add_item(self.equipped_weapon)
                    
                    # Equip new weapon
                    self.equipped_weapon = item
                    self.attack += item.value
                    self.remove_item(item_name, 1)
                    return True, f"You equipped {item_name}!"
                
                elif item.item_type == 'armor':
                    if self.equipped_armor:
                        # Unequip current armor
                        self.defense -= self.equipped_armor.value
                        self.add_item(self.equipped_armor)
                    
                    # Equip new armor
                    self.equipped_armor = item
                    self.defense += item.value
                    self.remove_item(item_name, 1)
                    return True, f"You equipped {item_name}!"
                
                else:
                    return False, f"{item_name} cannot be equipped!"
        
        return False, f"You don't have {item_name} in your inventory!"
    
    def get_inventory_display(self) -> str:
        """Get formatted inventory display."""
        if not self.inventory:
            return "Your inventory is empty."
        
        display = "\n=== INVENTORY ===\n"
        for i, item in enumerate(self.inventory, 1):
            display += f"{i}. {item}\n"
        display += f"\nGold: {self.gold}"
        return display
    
    def get_stats_display(self) -> str:
        """Get formatted stats display."""
        display = f"\n=== {self.name}'s STATS ===\n"
        display += f"Health: {self.health}/{self.max_health}\n"
        display += f"Attack: {self.attack}\n"
        display += f"Defense: {self.defense}\n"
        display += f"Gold: {self.gold}\n"
        display += f"\nEquipped Weapon: {self.equipped_weapon.name if self.equipped_weapon else 'None'}\n"
        display += f"Equipped Armor: {self.equipped_armor.name if self.equipped_armor else 'None'}\n"
        display += f"Items in Inventory: {len(self.inventory)}"
        return display
    
    def to_dict(self) -> Dict:
        """Convert player to dictionary for saving."""
        return {
            'name': self.name,
            'health': self.health,
            'max_health': self.max_health,
            'attack': self.attack,
            'defense': self.defense,
            'gold': self.gold,
            'inventory': [item.to_dict() for item in self.inventory],
            'equipped_weapon': self.equipped_weapon.to_dict() if self.equipped_weapon else None,
            'equipped_armor': self.equipped_armor.to_dict() if self.equipped_armor else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create player from dictionary."""
        player = cls(data['name'])
        player.health = data['health']
        player.max_health = data['max_health']
        player.attack = data['attack']
        player.defense = data['defense']
        player.gold = data['gold']
        player.inventory = [Item.from_dict(item) for item in data['inventory']]
        
        if data.get('equipped_weapon'):
            player.equipped_weapon = Item.from_dict(data['equipped_weapon'])
        if data.get('equipped_armor'):
            player.equipped_armor = Item.from_dict(data['equipped_armor'])
        
        return player


class InventorySystem:
    """Main inventory system class."""
    
    SAVE_FILE = "player_save.json"
    
    def __init__(self):
        self.player: Optional[Player] = None
        self.running: bool = True
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "=" * 60)
        print(" INVENTORY SYSTEM")
        print("=" * 60)
        print("\nWelcome to the RPG Inventory Manager!")
        print("Manage your items, equip gear, and become stronger!")
        print("-" * 60 + "\n")
    
    def display_menu(self):
        """Display main menu."""
        print("\n=== MAIN MENU ===")
        print("1. View Inventory")
        print("2. View Stats")
        print("3. Use Item")
        print("4. Equip Item")
        print("5. Add Item (Demo)")
        print("6. Drop Item")
        print("7. Shop")
        print("8. Save Game")
        print("9. Load Game")
        print("0. Quit")
        print("-" * 40)
    
    def add_demo_items(self):
        """Add demo items for testing."""
        demo_items = [
            Item("Health Potion", "Restores 25 health", "potion", 50),
            Item("Mana Potion", "Restores 25 mana", "potion", 60),
            Item("Bread", "Restores 10 hunger", "food", 10),
            Item("Apple", "Restores 5 hunger", "food", 5),
            Item("Iron Sword", "A sturdy iron sword", "weapon", 150),
            Item("Leather Armor", "Basic leather armor", "armor", 100),
            Item("Magic Ring", "A mysterious ring", "misc", 200),
        ]
        
        for item in demo_items:
            self.player.add_item(item)
        
        print("\nAdded 7 demo items to your inventory!")
    
    def shop_menu(self):
        """Display shop menu."""
        print("\n=== SHOP ===")
        print("Buy items with your gold!")
        print(f"Your Gold: {self.player.gold}")
        print("-" * 40)
        
        shop_items = [
            Item("Health Potion", "Restores 25 health", "potion", 50),
            Item("Mana Potion", "Restores 25 mana", "potion", 60),
            Item("Bread", "Restores 10 hunger", "food", 10),
            Item("Steel Sword", "A sharp steel sword", "weapon", 300),
            Item("Chain Mail", "Strong chain mail armor", "armor", 250),
        ]
        
        for i, item in enumerate(shop_items, 1):
            print(f"{i}. {item.name} - {item.value} gold")
        
        print("0. Back to Menu")
        
        try:
            choice = int(input("\nEnter item number to buy: "))
            if choice == 0:
                return
            
            if 1 <= choice <= len(shop_items):
                item = shop_items[choice - 1]
                if self.player.gold >= item.value:
                    self.player.gold -= item.value
                    self.player.add_item(item)
                    print(f"\nBought {item.name}!")
                else:
                    print("\nNot enough gold!")
        except ValueError:
            print("Invalid input!")
    
    def run(self):
        """Main game loop."""
        self.display_welcome()
        
        # Create new player or load
        if os.path.exists(self.SAVE_FILE):
            load_choice = input("Save file found! Load it? (yes/no): ").lower()
            if load_choice in ['yes', 'y']:
                self.load_game()
            else:
                name = input("Enter your character's name (or press Enter for 'Hero'): ").strip()
                self.player = Player(name if name else "Hero")
        else:
            name = input("Enter your character's name (or press Enter for 'Hero'): ").strip()
            self.player = Player(name if name else "Hero")
        
        print(f"\nWelcome, {self.player.name}!")
        
        while self.running:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (0-9): ").strip()
                
                if choice == '1':
                    print(self.player.get_inventory_display())
                
                elif choice == '2':
                    print(self.player.get_stats_display())
                
                elif choice == '3':
                    # Use item
                    if not self.player.inventory:
                        print("\nYour inventory is empty!")
                        continue
                    
                    print("\nYour items:")
                    for i, item in enumerate(self.player.inventory, 1):
                        print(f"{i}. {item.name}")
                    
                    item_choice = int(input("Enter item number to use: ")) - 1
                    if 0 <= item_choice < len(self.player.inventory):
                        item_name = self.player.inventory[item_choice].name
                        success, message = self.player.use_item(item_name)
                        print(f"\n{message}")
                    else:
                        print("Invalid item number!")
                
                elif choice == '4':
                    # Equip item
                    if not self.player.inventory:
                        print("\nYour inventory is empty!")
                        continue
                    
                    print("\nEquippable items:")
                    equippable = [item for item in self.player.inventory 
                                if item.item_type in ['weapon', 'armor']]
                    
                    if not equippable:
                        print("No equippable items!")
                        continue
                    
                    for i, item in enumerate(equippable, 1):
                        print(f"{i}. {item.name} ({item.item_type})")
                    
                    item_choice = int(input("Enter item number to equip: ")) - 1
                    if 0 <= item_choice < len(equippable):
                        item_name = equippable[item_choice].name
                        success, message = self.player.equip_item(item_name)
                        print(f"\n{message}")
                    else:
                        print("Invalid item number!")
                
                elif choice == '5':
                    self.add_demo_items()
                
                elif choice == '6':
                    # Drop item
                    if not self.player.inventory:
                        print("\nYour inventory is empty!")
                        continue
                    
                    print("\nYour items:")
                    for i, item in enumerate(self.player.inventory, 1):
                        print(f"{i}. {item.name}")
                    
                    item_choice = int(input("Enter item number to drop: ")) - 1
                    if 0 <= item_choice < len(self.player.inventory):
                        item_name = self.player.inventory[item_choice].name
                        self.player.remove_item(item_name, 1)
                        print(f"\nDropped {item_name}!")
                    else:
                        print("Invalid item number!")
                
                elif choice == '7':
                    self.shop_menu()
                
                elif choice == '8':
                    self.save_game()
                
                elif choice == '9':
                    self.load_game()
                
                elif choice == '0':
                    save_choice = input("\nSave before quitting? (yes/no): ").lower()
                    if save_choice in ['yes', 'y']:
                        self.save_game()
                    print("\nThanks for playing! Goodbye!")
                    self.running = False
                
                else:
                    print("Invalid choice! Please enter 0-9.")
            
            except ValueError:
                print("Invalid input! Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def save_game(self):
        """Save game to file."""
        try:
            data = self.player.to_dict()
            data['save_time'] = datetime.now().isoformat()
            
            with open(self.SAVE_FILE, 'w') as f:
                json.dump(data, f, indent=2)
            
            print("\nGame saved successfully!")
        except Exception as e:
            print(f"\nError saving game: {e}")
    
    def load_game(self):
        """Load game from file."""
        try:
            if not os.path.exists(self.SAVE_FILE):
                print("\nNo save file found!")
                return
            
            with open(self.SAVE_FILE, 'r') as f:
                data = json.load(f)
            
            self.player = Player.from_dict(data)
            print(f"\nGame loaded successfully!")
            print(f"Last saved: {data.get('save_time', 'Unknown')}")
        except Exception as e:
            print(f"\nError loading game: {e}")


def main():
    """Main entry point."""
    system = InventorySystem()
    system.run()


if __name__ == "__main__":
    main()
"""
Flashcard App
Study with digital flashcards. Learn data persistence and random selection.

How to Play:
1. Create your own flashcards
2. Study them in random order
3. Track your progress

Python Concepts:
- Lists and dictionaries
- File I/O (JSON)
- Random shuffling
- Score tracking
"""

import json
import os
import random


FLASHCARDS_FILE = "flashcards.json"


def load_flashcards() -> list[dict]:
    """Load flashcards from file.
    
    Returns:
        List of flashcard dictionaries
    """
    if os.path.exists(FLASHCARDS_FILE):
        try:
            with open(FLASHCARDS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_flashcards(flashcards: list[dict]) -> None:
    """Save flashcards to file.
    
    Args:
        flashcards: List to save
    """
    with open(FLASHCARDS_FILE, 'w') as f:
        json.dump(flashcards, f, indent=2)


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  📚 FLASHCARD APP")
    print("="*50)
    print("\nCreate and study flashcards!")
    print("\nPython Concepts: Lists, File I/O, Random")


def add_flashcard(flashcards: list[dict]) -> None:
    """Add a new flashcard.
    
    Args:
        flashcards: List to add to
    """
    print("\n  Add New Flashcard")
    print("  " + "-"*30)
    
    front = input("  Front (question/term): ").strip()
    if not front:
        print("  Cancelled!")
        return
    
    back = input("  Back (answer/definition): ").strip()
    if not back:
        print("  Cancelled!")
        return
    
    category = input("  Category (optional): ").strip() or "General"
    
    card = {
        'front': front,
        'back': back,
        'category': category,
        'correct': 0,
        'incorrect': 0
    }
    
    flashcards.append(card)
    save_flashcards(flashcards)
    
    print(f"\n  ✅ Flashcard added!")


def view_flashcards(flashcards: list[dict]) -> None:
    """View all flashcards.
    
    Args:
        flashcards: List of flashcards
    """
    if not flashcards:
        print("\n  No flashcards yet!")
        return
    
    print("\n  📋 ALL FLASHCARDS")
    print("  " + "="*60)
    
    for i, card in enumerate(flashcards, 1):
        print(f"\n  {i}. [{card.get('category', 'General')}]")
        print(f"     Q: {card['front']}")
        print(f"     A: {card['back']}")
        print(f"     Stats: ✅ {card.get('correct', 0)} | ❌ {card.get('incorrect', 0)}")
    
    print("\n  " + "="*60)
    print(f"  Total: {len(flashcards)} flashcards")


def study_mode(flashcards: list[dict]) -> None:
    """Study flashcards in random order.
    
    Args:
        flashcards: List of flashcards
    """
    if not flashcards:
        print("\n  No flashcards to study!")
        return
    
    print("\n  📖 STUDY MODE")
    print("  " + "-"*30)
    print("  Press Enter to reveal answer")
    print("  Type 'y' if correct, 'n' if incorrect")
    print("  Type 'q' to quit studying")
    
    cards = flashcards.copy()
    random.shuffle(cards)
    
    correct = 0
    incorrect = 0
    
    for i, card in enumerate(cards, 1):
        print(f"\n  Card {i}/{len(cards)}")
        print(f"  Category: {card.get('category', 'General')}")
        print(f"\n  Q: {card['front']}")
        
        input("\n  Press Enter to reveal answer...")
        print(f"  A: {card['back']}")
        
        while True:
            choice = input("\n  Correct? (y/n/q): ").strip().lower()
            if choice in ['y', 'n', 'q']:
                break
            print("  Please enter y, n, or q.")
        
        if choice == 'q':
            break
        elif choice == 'y':
            correct += 1
            card['correct'] = card.get('correct', 0) + 1
        else:
            incorrect += 1
            card['incorrect'] = card.get('incorrect', 0) + 1
    
    save_flashcards(flashcards)
    
    total = correct + incorrect
    if total > 0:
        accuracy = (correct / total) * 100
        print(f"\n  📊 Study Results:")
        print(f"  Correct: {correct}")
        print(f"  Incorrect: {incorrect}")
        print(f"  Accuracy: {accuracy:.1f}%")


def delete_flashcard(flashcards: list[dict]) -> None:
    """Delete a flashcard.
    
    Args:
        flashcards: List to modify
    """
    if not flashcards:
        print("\n  No flashcards to delete!")
        return
    
    view_flashcards(flashcards)
    
    try:
        idx = int(input("\n  Enter card number to delete: ").strip()) - 1
        if 0 <= idx < len(flashcards):
            removed = flashcards.pop(idx)
            save_flashcards(flashcards)
            print(f"\n  ✅ Deleted: {removed['front']}")
        else:
            print("  Invalid card number!")
    except ValueError:
        print("  Invalid input!")


def main() -> None:
    """Main flashcard loop."""
    display_welcome()
    
    flashcards = load_flashcards()
    
    while True:
        print(f"\n  ({len(flashcards)} flashcards)")
        print("  Options:")
        print("  1. Add flashcard")
        print("  2. View all flashcards")
        print("  3. Study mode")
        print("  4. Delete flashcard")
        print("  5. Quit")
        
        choice = input("\n  Your choice (1-5): ").strip()
        
        if choice == '1':
            add_flashcard(flashcards)
        elif choice == '2':
            view_flashcards(flashcards)
        elif choice == '3':
            study_mode(flashcards)
        elif choice == '4':
            delete_flashcard(flashcards)
        elif choice == '5':
            break
        else:
            print("  Invalid choice!")
    
    print("\nThanks for using Flashcard App!")
    print("Keep learning! 📚")


if __name__ == "__main__":
    main()

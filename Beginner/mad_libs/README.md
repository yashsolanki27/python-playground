# Mad Libs Game

## Description
The classic word game where you fill in the blanks to create hilarious stories! Choose a template, enter words, and read your funny creation!

## How to Play
1. Run the game: `python game.py`
2. Choose a story template
3. Enter words when prompted (nouns, verbs, adjectives)
4. Read your completed story
5. Create more stories!

## Python Concepts Learned
- **String Formatting**: Building stories with f-strings
- **Lists**: Storing story templates
- **User Input**: Getting words from player
- **String Replacement**: Template filling
- **Dictionaries**: Word mappings

## Sample Output
```
==================================================
  MAD LIBS GAME
==================================================

Create hilarious stories by filling in the blanks!

  Choose a story:
  1. The Crazy Day
  2. Space Adventure
  3. School Story
  4. Pet Tale

Enter choice (1-4): 1

  Enter words for the story:
  Enter an adjective (describing word): silly
  Enter a day of the week: Monday
  Enter another adjective: furry
  Enter a noun (thing): penguin
  Enter a verb (action word): dance
  Enter another noun: refrigerator
  Enter one more adjective: sparkly
  Enter another verb: jump
  Enter yet another adjective: happy

==================================================
  📖 THE CRAZY DAY
==================================================

  One silly Monday, a furry penguin decided to dance to the refrigerator. 
  It was so sparkly that everyone started jumping. 
  The penguin felt happy and decided to jump instead!

==================================================
```

## Code Structure
```
mad_libs/
├── game.py           # Main game file
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Future Enhancements
- [ ] Add more story templates
- [ ] Save stories to file
- [ ] Add story sharing feature
- [ ] Create multiplayer mode
- [ ] Add story rating system

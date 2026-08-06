"""
Mad Libs Game
A fun word game where you fill in blanks to create silly stories.

How to Play:
1. Choose a story template
2. Enter words when prompted (nouns, verbs, adjectives, etc.)
3. See your hilarious story!

Python Concepts:
- String formatting with f-strings
- Lists for story templates
- User input handling
- String concatenation
"""

import random


STORIES = [
    {
        'title': 'The Crazy Day',
        'template': "One {adjective1} {day}, a {adjective2} {noun1} decided to {verb1} to the {noun2}. "
                    "It was so {adjective3} that everyone started {verb2}ing. "
                    "The {noun1} felt {adjective4} and decided to {verb3} instead!",
        'prompts': ['adjective1', 'day', 'adjective2', 'noun1', 'verb1', 'noun2', 
                    'adjective3', 'verb2', 'adjective3', 'noun1', 'adjective4', 'verb3']
    },
    {
        'title': 'Space Adventure',
        'template': "Captain {name} flew the {adjective1} rocket to {planet}. "
                    "There, they found a {adjective2} {creature} who loved to {verb1}. "
                    "Together they {verb2}ed across the {noun1} and found {adjective3} treasure!",
        'prompts': ['name', 'adjective1', 'planet', 'adjective2', 'creature', 'verb1', 
                    'verb2', 'noun1', 'adjective3']
    },
    {
        'title': 'School Story',
        'template': "In {year}, {name} went to school with a {adjective1} {noun1}. "
                    "The teacher asked everyone to {verb1} their {noun2}. "
                    "But {name} was too busy {verb2}ing with the {adjective2} {noun3}!",
        'prompts': ['year', 'name', 'adjective1', 'noun1', 'verb1', 'noun2', 
                    'name', 'verb2', 'adjective2', 'noun3']
    },
    {
        'title': 'Pet Tale',
        "template": "My {adjective1} pet {animal} loves to {verb1} {noun1}s. "
                    "Every {time}, it {verb2}s with the {adjective2} {noun2}. "
                    "Sometimes it even {verb3}s on the {adjective3} {noun3}!",
        'prompts': ['adjective1', 'animal', 'verb1', 'noun1', 'time', 'verb2', 
                    'adjective2', 'noun2', 'verb3', 'adjective3', 'noun3']
    }
]


PROMPT_DESCRIPTIONS = {
    'adjective1': 'an adjective (describing word)',
    'adjective2': 'another adjective',
    'adjective3': 'one more adjective',
    'adjective4': 'yet another adjective',
    'noun1': 'a noun (thing)',
    'noun2': 'another noun',
    'noun3': 'one more noun',
    'verb1': 'a verb (action word)',
    'verb2': 'another verb',
    'verb3': 'one more verb',
    'name': 'a name',
    'day': 'a day of the week',
    'planet': 'a planet name',
    'creature': 'a creature/animal',
    'year': 'a year',
    'animal': 'an animal',
    'time': 'a time of day'
}


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  MAD LIBS GAME")
    print("="*50)
    print("\nCreate hilarious stories by filling in the blanks!")
    print("\nRules:")
    print("  1. Choose a story template")
    print("  2. Enter words when prompted")
    print("  3. Read your funny story!")
    print("\nPython Concepts: Strings, Formatting, Lists")


def select_story() -> dict:
    """Let player choose a story.
    
    Returns:
        Selected story dictionary
    """
    print("\n  Choose a story:")
    
    for i, story in enumerate(STORIES, 1):
        print(f"  {i}. {story['title']}")
    
    while True:
        try:
            choice = int(input(f"\nEnter choice (1-{len(STORIES)}): ").strip())
            if 1 <= choice <= len(STORIES):
                return STORIES[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")


def get_words(story: dict) -> dict[str, str]:
    """Get all required words from the player.
    
    Args:
        story: Story dictionary with prompts
        
    Returns:
        Dictionary of word type to user's word
    """
    words = {}
    unique_prompts = []
    seen = set()
    
    for prompt in story['prompts']:
        if prompt not in seen:
            unique_prompts.append(prompt)
            seen.add(prompt)
    
    print("\n  Enter words for the story:")
    
    for prompt in unique_prompts:
        description = PROMPT_DESCRIPTIONS.get(prompt, prompt)
        word = input(f"  Enter {description}: ").strip()
        
        while not word:
            print("  Please enter a word!")
            word = input(f"  Enter {description}: ").strip()
        
        words[prompt] = word
    
    return words


def build_story(story: dict, words: dict[str, str]) -> str:
    """Build the story with user's words.
    
    Args:
        story: Story template
        words: User's words
        
    Returns:
        Complete story string
    """
    template = story['template']
    
    for word_type, word in words.items():
        template = template.replace('{' + word_type + '}', word)
    
    return template


def display_story(title: str, story_text: str) -> None:
    """Display the completed story.
    
    Args:
        title: Story title
        story_text: Complete story
    """
    print("\n" + "="*50)
    print(f"  📖 {title.upper()}")
    print("="*50)
    print(f"\n  {story_text}")
    print("\n" + "="*50)


def main() -> None:
    """Main Mad Libs loop."""
    display_welcome()
    
    stories_told = 0
    
    while True:
        story = select_story()
        words = get_words(story)
        complete_story = build_story(story, words)
        
        display_story(story['title'], complete_story)
        
        stories_told += 1
        print(f"\n  (Total stories: {stories_told})")
        
        play_again = input("\nCreate another story? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            break
    
    print("\n" + "="*50)
    print(f"  Total stories created: {stories_told}")
    print("\nThanks for playing Mad Libs!")
    print("See you next time!")


if __name__ == "__main__":
    main()

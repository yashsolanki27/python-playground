"""
Quiz Game
A trivia quiz game to learn dictionaries, lists, and data structures.

How to Play:
1. Choose a quiz category (Science, History, Geography, Technology)
2. Answer multiple-choice questions
3. Get immediate feedback on each answer
4. See your final score at the end

Python Concepts:
- Dictionaries for storing questions and answers
- Lists for answer options
- Random module for shuffling questions
- Loops for iterating through questions
- Score tracking
- Data structures organization
"""

import random


# Quiz questions organized by category
QUIZ_DATA = {
    'Science': [
        {
            'question': 'What is the chemical symbol for water?',
            'options': ['A) H2O', 'B) CO2', 'C) NaCl', 'D) O2'],
            'answer': 'A',
            'explanation': 'Water is H2O - two hydrogen atoms and one oxygen atom.'
        },
        {
            'question': 'What planet is known as the Red Planet?',
            'options': ['A) Venus', 'B) Mars', 'C) Jupiter', 'D) Saturn'],
            'answer': 'B',
            'explanation': 'Mars appears red due to iron oxide (rust) on its surface.'
        },
        {
            'question': 'What is the powerhouse of the cell?',
            'options': ['A) Nucleus', 'B) Ribosome', 'C) Mitochondria', 'D) Cell Wall'],
            'answer': 'C',
            'explanation': 'Mitochondria generate most of the cell\'s ATP energy.'
        },
        {
            'question': 'What gas do plants absorb from the atmosphere?',
            'options': ['A) Oxygen', 'B) Nitrogen', 'C) Carbon Dioxide', 'D) Hydrogen'],
            'answer': 'C',
            'explanation': 'Plants use CO2 for photosynthesis to make glucose.'
        },
        {
            'question': 'What is the speed of light approximately?',
            'options': ['A) 300,000 km/s', 'B) 150,000 km/s', 'C) 500,000 km/s', 'D) 100,000 km/s'],
            'answer': 'A',
            'explanation': 'Light travels at approximately 299,792 km/s in vacuum.'
        }
    ],
    'History': [
        {
            'question': 'In what year did World War II end?',
            'options': ['A) 1943', 'B) 1944', 'C) 1945', 'D) 1946'],
            'answer': 'C',
            'explanation': 'WWII ended in 1945 with the surrender of Japan.'
        },
        {
            'question': 'Who was the first President of the United States?',
            'options': ['A) John Adams', 'B) Thomas Jefferson', 'C) George Washington', 'D) Benjamin Franklin'],
            'answer': 'C',
            'explanation': 'George Washington served as the first U.S. President from 1789-1797.'
        },
        {
            'question': 'In which year did the Titanic sink?',
            'options': ['A) 1910', 'B) 1912', 'C) 1914', 'D) 1916'],
            'answer': 'B',
            'explanation': 'The Titanic sank on April 15, 1912 after hitting an iceberg.'
        },
        {
            'question': 'Who painted the Mona Lisa?',
            'options': ['A) Michelangelo', 'B) Raphael', 'C) Leonardo da Vinci', 'D) Donatello'],
            'answer': 'C',
            'explanation': 'Leonardo da Vinci painted the Mona Lisa around 1503-1519.'
        },
        {
            'question': 'What ancient wonder was located in Giza, Egypt?',
            'options': ['A) Colossus', 'B) Pyramids', 'C) Lighthouse', 'D) Gardens'],
            'answer': 'B',
            'explanation': 'The Great Pyramids of Giza are the only surviving ancient wonder.'
        }
    ],
    'Geography': [
        {
            'question': 'What is the largest ocean on Earth?',
            'options': ['A) Atlantic', 'B) Indian', 'C) Arctic', 'D) Pacific'],
            'answer': 'D',
            'explanation': 'The Pacific Ocean covers about 63 million square miles.'
        },
        {
            'question': 'What is the longest river in the world?',
            'options': ['A) Amazon', 'B) Nile', 'C) Mississippi', 'D) Yangtze'],
            'answer': 'B',
            'explanation': 'The Nile stretches approximately 4,130 miles through Africa.'
        },
        {
            'question': 'What is the smallest country in the world?',
            'options': ['A) Monaco', 'B) Vatican City', 'C) San Marino', 'D) Liechtenstein'],
            'answer': 'B',
            'explanation': 'Vatican City is only 0.17 square miles (0.44 km²).'
        },
        {
            'question': 'Which continent has the most countries?',
            'options': ['A) Asia', 'B) Europe', 'C) Africa', 'D) South America'],
            'answer': 'C',
            'explanation': 'Africa has 54 recognized countries, more than any other continent.'
        },
        {
            'question': 'What is the capital of Australia?',
            'options': ['A) Sydney', 'B) Melbourne', 'C) Canberra', 'D) Perth'],
            'answer': 'C',
            'explanation': 'Canberra is the capital, not Sydney or Melbourne as many think.'
        }
    ],
    'Technology': [
        {
            'question': 'What does "CPU" stand for?',
            'options': ['A) Central Processing Unit', 'B) Computer Personal Unit', 'C) Central Program Utility', 'D) Core Processing Unit'],
            'answer': 'A',
            'explanation': 'The CPU is the primary component that processes instructions.'
        },
        {
            'question': 'What year was the first iPhone released?',
            'options': ['A) 2005', 'B) 2006', 'C) 2007', 'D) 2008'],
            'answer': 'C',
            'explanation': 'Apple released the first iPhone on June 29, 2007.'
        },
        {
            'question': 'What does "HTML" stand for?',
            'options': ['A) Hyper Text Markup Language', 'B) High Tech Modern Language', 'C) Hyper Transfer Markup Language', 'D) Home Tool Markup Language'],
            'answer': 'A',
            'explanation': 'HTML is the standard markup language for creating web pages.'
        },
        {
            'question': 'Who co-founded Apple Computer with Steve Jobs?',
            'options': ['A) Bill Gates', 'B) Steve Wozniak', 'C) Paul Allen', 'D) Tim Cook'],
            'answer': 'B',
            'explanation': 'Steve Wozniak co-founded Apple with Jobs and Ronald Wayne in 1976.'
        },
        {
            'question': 'What does "API" stand for?',
            'options': ['A) Application Programming Interface', 'B) Advanced Program Integration', 'C) Application Process Integration', 'D) Automated Programming Interface'],
            'answer': 'A',
            'explanation': 'APIs allow different software applications to communicate.'
        }
    ]
}


def display_welcome() -> None:
    """Display welcome message and rules."""
    print("\n" + "="*50)
    print("  QUIZ GAME")
    print("="*50)
    print("\nWelcome to the Quiz Game!")
    print("\nRules:")
    print("  1. Choose a category")
    print("  2. Answer 5 multiple-choice questions")
    print("  3. Get 1 point for each correct answer")
    print("  4. See your score and correct answers at the end")
    print("\nPython Concepts: Dictionaries, Lists, Data Structures")


def select_category() -> str:
    """Let player choose a quiz category.
    
    Returns:
        Selected category name
    """
    print("\n  Choose a category:")
    categories = list(QUIZ_DATA.keys())
    
    for i, cat in enumerate(categories, 1):
        count = len(QUIZ_DATA[cat])
        print(f"  {i}. {cat} ({count} questions)")
    
    while True:
        choice = input(f"\nEnter choice (1-{len(categories)}): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")


def ask_question(question_data: dict, question_num: int) -> tuple[bool, str]:
    """Ask a single quiz question.
    
    Args:
        question_data: Dictionary with question, options, answer, explanation
        question_num: Current question number
        
    Returns:
        Tuple of (is_correct, correct_answer)
    """
    print(f"\n  Question {question_num}:")
    print(f"  {question_data['question']}")
    
    for option in question_data['options']:
        print(f"    {option}")
    
    while True:
        answer = input("\n  Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            break
        print("  Invalid input. Please enter A, B, C, or D.")
    
    correct = question_data['answer']
    is_correct = (answer == correct)
    
    if is_correct:
        print("\n  ✅ Correct!")
    else:
        print(f"\n  ❌ Wrong! The correct answer was {correct}.")
    
    print(f"  📚 {question_data['explanation']}")
    
    return is_correct, correct


def play_quiz(category: str) -> tuple[int, list[dict]]:
    """Play a quiz round.
    
    Args:
        category: Selected quiz category
        
    Returns:
        Tuple of (score, list of missed questions)
    """
    questions = QUIZ_DATA[category].copy()
    random.shuffle(questions)
    
    score = 0
    missed = []
    
    print(f"\n  Category: {category}")
    print(f"  Questions: {len(questions)}")
    print("  Let's begin!")
    
    for i, q in enumerate(questions, 1):
        is_correct, _ = ask_question(q, i)
        
        if is_correct:
            score += 1
        else:
            missed.append(q)
        
        # Show running score
        print(f"\n  📊 Score so far: {score}/{i}")
    
    return score, missed


def display_results(score: int, total: int, missed: list[dict], category: str) -> None:
    """Display final quiz results.
    
    Args:
        score: Number of correct answers
        total: Total number of questions
        missed: List of missed question data
        category: Quiz category
    """
    percentage = (score / total) * 100
    
    print("\n" + "="*50)
    print("  QUIZ RESULTS")
    print("="*50)
    print(f"\n  Category: {category}")
    print(f"  Score: {score}/{total} ({percentage:.1f}%)")
    
    # Performance message
    if percentage == 100:
        print("\n  🏆 PERFECT SCORE! Amazing work!")
    elif percentage >= 80:
        print("\n  🌟 Excellent! You really know your stuff!")
    elif percentage >= 60:
        print("\n  👍 Good job! Keep learning!")
    elif percentage >= 40:
        print("\n  📚 Not bad, but there's room to improve!")
    else:
        print("\n  💪 Keep studying! You'll do better next time!")
    
    # Show missed questions
    if missed:
        print(f"\n  📋 Questions you missed ({len(missed)}):")
        for q in missed:
            print(f"\n  Q: {q['question']}")
            print(f"  A: {q['answer']}) {q['explanation']}")
    else:
        print("\n  🎉 You got everything right!")


def main() -> None:
    """Main quiz loop."""
    display_welcome()
    
    while True:
        category = select_category()
        score, missed = play_quiz(category)
        
        display_results(score, len(QUIZ_DATA[category]), missed, category)
        
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Quiz Game!")
            print("See you next time!")
            break


if __name__ == "__main__":
    main()

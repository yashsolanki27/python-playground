# Blackjack Game

## Description
A classic Blackjack (21) card game where you play against the dealer. Use strategy to get as close to 21 as possible without going over!

## How to Play
1. Run the game: `python game.py`
2. Start with $1000
3. Place your bet each round
4. Choose to Hit (take a card) or Stand (keep your hand)
5. Try to beat the dealer's hand
6. Blackjack pays 3:2!

## Python Concepts Learned
- **Object-Oriented Programming**: Card, Deck, and Hand classes
- **Inheritance & Composition**: Objects working together
- **Complex Logic**: Game rules and win conditions
- **State Management**: Tracking money, hands, and game state
- **Random Module**: Shuffling and dealing cards
- **Type Hints**: Function annotations
- **Error Handling**: Input validation and edge cases

## Game Rules
- **Goal**: Get closer to 21 than the dealer without going over
- **Card Values**:
  - Number cards: Face value
  - Face cards (J, Q, K): 10
  - Ace: 11 or 1 (auto-adjusted)
- **Blackjack**: 21 with first 2 cards pays 3:2
- **Bust**: Going over 21 loses automatically
- **Dealer**: Must hit on 16 or less, stand on 17 or more

## Sample Output
```
============================================================
 BLACKJACK
============================================================

Rules:
  - Get closer to 21 than the dealer without going over
  - Face cards (J, Q, K) are worth 10
  - Aces are worth 11 or 1
  - Blackjack (21 with 2 cards) pays 3:2
  - Dealer must hit on 16 or less, stand on 17 or more

Commands:
  - 'hit' or 'h': Take another card
  - 'stand' or 's': Keep your current hand
  - 'quit': Exit the game
------------------------------------------------------------

Starting money: $1000

========================================
 ROUND 1
========================================

You have $1000. Enter your bet: $100

========================================
 DEALER'S HAND
========================================
[Hidden] + 7 of Hearts

========================================
 YOUR HAND
========================================
King of Spades + 8 of Clubs
Value: 18
========================================

Do you want to (h)it or (s)tand? s

--- Dealer's Turn ---
Dealer's hand: [Hidden] + 7 of Hearts
Dealer takes: 4 of Diamonds
Dealer's hand: 7 of Hearts + 4 of Diamonds
Dealer's value: 11
Dealer takes: 9 of Spades
Dealer's hand: 7 of Hearts + 4 of Diamonds + 9 of Spades
Dealer's value: 20

Dealer stands at 20

========================================
 DEALER'S HAND
========================================
7 of Hearts + 4 of Diamonds + 9 of Spades
Value: 20

========================================
 YOUR HAND
========================================
King of Spades + 8 of Clubs
Value: 18
========================================

Dealer wins! You lose.

You lost $100!

Your money: $900

Do you want to play another round? (yes/no): no

============================================================
 FINAL RESULTS
============================================================
Starting money: $1000
Final money: $900
Profit/Loss: $-100
Rounds played: 1
Wins: 0
Losses: 1

Better luck next time!
============================================================

Thanks for playing Blackjack!
```

## Code Structure
```
blackjack/
├── game.py           # Main game file (300 lines)
├── README.md         # This file
└── requirements.txt  # No dependencies
```

## Classes

### Card Class
- `suit`: Card suit (Hearts, Diamonds, Clubs, Spades)
- `rank`: Card rank (2-10, J, Q, K, A)
- `value()`: Get blackjack value

### Deck Class
- `cards`: List of Card objects
- `reset()`: Create new deck
- `shuffle()`: Shuffle deck
- `deal()`: Deal one card

### Hand Class
- `cards`: List of Card objects
- `add_card(card)`: Add card to hand
- `get_value()`: Calculate hand value
- `is_busted()`: Check if over 21
- `is_blackjack()`: Check for natural 21

## Key Functions
- `display_welcome()`: Shows game rules
- `get_bet(money)`: Gets valid bet amount
- `get_player_choice()`: Gets hit/stand choice
- `dealer_turn(deck, dealer_hand)`: Plays dealer's hand
- `determine_winner(player, dealer, bet)`: Calculates winner
- `display_game_state(...)`: Shows current hands
- `play_round(deck, money)`: Plays one round
- `play_game()`: Main game loop

## Strategy Tips
- Always hit on 11 or less
- Always stand on 17 or more
- Consider dealer's visible card
- Remember dealer must hit on 16

## Error Handling
- Validates bet amount (0 < bet <= money)
- Validates hit/stand input
- Handles deck reshuffling
- Prevents invalid moves

## Future Enhancements
- [ ] Add splitting pairs
- [ ] Add doubling down
- [ ] Add insurance bets
- [ ] Create GUI version
- [ ] Add card counting indicator
- [ ] Implement multiple hands
- [ ] Add dealer AI strategies
- [ ] Create multiplayer mode
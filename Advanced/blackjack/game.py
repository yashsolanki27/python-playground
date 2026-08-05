"""
Blackjack Game
A card game to learn OOP, complex logic, and game state management.

How to Play:
1. Place a bet (starting with $1000)
2. Receive 2 cards, dealer shows 1 card
3. Choose to Hit (take card) or Stand (keep hand)
4. Try to get closer to 21 than the dealer without going over
5. Win money based on your bet!
6. Blackjack (21 with first 2 cards) pays 3:2

Python Concepts:
- Object-Oriented Programming (Classes)
- Lists and list operations
- Random module
- Game state management
- Complex conditional logic
- User input validation
- Money/bet management
"""

import random
from typing import List, Tuple, Optional


class Card:
    """Represents a playing card."""
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
    
    def value(self) -> int:
        """Get the blackjack value of the card."""
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Will be adjusted to 1 if needed
        else:
            return int(self.rank)
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a deck of cards."""
    
    def __init__(self):
        self.cards: List[Card] = []
        self.reset()
    
    def reset(self):
        """Create a new deck of 52 cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)
    
    def deal(self) -> Optional[Card]:
        """Deal one card from the deck."""
        if self.cards:
            return self.cards.pop()
        return None


class Hand:
    """Represents a hand of cards."""
    
    def __init__(self):
        self.cards: List[Card] = []
    
    def add_card(self, card: Card):
        """Add a card to the hand."""
        self.cards.append(card)
    
    def get_value(self) -> int:
        """Calculate the value of the hand, adjusting for Aces."""
        value = 0
        aces = 0
        
        for card in self.cards:
            value += card.value()
            if card.rank == 'Ace':
                aces += 1
        
        # Adjust for Aces (11 -> 1 if needed)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        
        return value
    
    def is_busted(self) -> bool:
        """Check if hand is over 21."""
        return self.get_value() > 21
    
    def is_blackjack(self) -> bool:
        """Check if hand is a natural blackjack (21 with 2 cards)."""
        return len(self.cards) == 2 and self.get_value() == 21
    
    def display(self, hide_first: bool = False) -> str:
        """Display the hand."""
        if hide_first and len(self.cards) > 1:
            return f"[Hidden] + {self.cards[1]}"
        else:
            return " + ".join(str(card) for card in self.cards)


def display_welcome():
    """Display welcome message and game rules."""
    print("=" * 60)
    print(" BLACKJACK")
    print("=" * 60)
    print("\nRules:")
    print("  - Get closer to 21 than the dealer without going over")
    print("  - Face cards (J, Q, K) are worth 10")
    print("  - Aces are worth 11 or 1")
    print("  - Blackjack (21 with 2 cards) pays 3:2")
    print("  - Dealer must hit on 16 or less, stand on 17 or more")
    print("\nCommands:")
    print("  - 'hit' or 'h': Take another card")
    print("  - 'stand' or 's': Keep your current hand")
    print("  - 'quit': Exit the game")
    print("-" * 60 + "\n")


def get_bet(money: int) -> int:
    """
    Get bet amount from player.
    
    Args:
        money: Player's current money
        
    Returns:
        Bet amount
    """
    while True:
        bet_input = input(f"\nYou have ${money}. Enter your bet: $").strip()
        
        if bet_input.lower() == 'quit':
            return -1
        
        try:
            bet = int(bet_input)
            if 0 < bet <= money:
                return bet
            elif bet > money:
                print(f"You don't have enough money! You only have ${money}.")
            else:
                print("Bet must be greater than 0!")
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_player_choice() -> str:
    """
    Get player's choice (hit or stand).
    
    Returns:
        'hit', 'stand', or 'quit'
    """
    while True:
        choice = input("\nDo you want to (h)it or (s)tand? ").lower().strip()
        
        if choice in ['hit', 'h']:
            return 'hit'
        elif choice in ['stand', 's']:
            return 'stand'
        elif choice == 'quit':
            return 'quit'
        else:
            print("Invalid choice! Enter 'hit' or 'stand'.")


def dealer_turn(deck: Deck, dealer_hand: Hand):
    """
    Play the dealer's turn.
    
    Args:
        deck: Card deck
        dealer_hand: Dealer's hand
    """
    print("\n--- Dealer's Turn ---")
    print(f"Dealer's hand: {dealer_hand.display()}")
    
    while dealer_hand.get_value() < 17:
        card = deck.deal()
        if card:
            dealer_hand.add_card(card)
            print(f"Dealer takes: {card}")
            print(f"Dealer's hand: {dealer_hand.display()}")
            print(f"Dealer's value: {dealer_hand.get_value()}")
    
    if dealer_hand.is_busted():
        print("\nDealer busts!")
    else:
        print(f"\nDealer stands at {dealer_hand.get_value()}")


def determine_winner(player_hand: Hand, dealer_hand: Hand, bet: int) -> Tuple[str, int]:
    """
    Determine the winner and calculate payout.
    
    Args:
        player_hand: Player's hand
        dealer_hand: Dealer's hand
        bet: Original bet
        
    Returns:
        Tuple of (result_message, money_change)
    """
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    
    # Check for blackjack
    if player_hand.is_blackjack() and not dealer_hand.is_blackjack():
        return "BLACKJACK! You win!", int(bet * 1.5)
    
    if dealer_hand.is_blackjack() and not player_hand.is_blackjack():
        return "Dealer has Blackjack! You lose.", -bet
    
    # Check for busts
    if player_hand.is_busted():
        return "You busted! You lose.", -bet
    
    if dealer_hand.is_busted():
        return "Dealer busted! You win!", bet
    
    # Compare hands
    if player_value > dealer_value:
        return "You win!", bet
    elif dealer_value > player_value:
        return "Dealer wins! You lose.", -bet
    else:
        return "It's a push (tie)!", 0


def display_game_state(player_hand: Hand, dealer_hand: Hand, hide_dealer: bool = True):
    """
    Display current game state.
    
    Args:
        player_hand: Player's hand
        dealer_hand: Dealer's hand
        hide_dealer: Whether to hide dealer's first card
    """
    print("\n" + "=" * 40)
    print(" DEALER'S HAND")
    print("=" * 40)
    print(dealer_hand.display(hide_first=hide_dealer))
    if not hide_dealer:
        print(f"Value: {dealer_hand.get_value()}")
    
    print("\n" + "=" * 40)
    print(" YOUR HAND")
    print("=" * 40)
    print(player_hand.display())
    print(f"Value: {player_hand.get_value()}")
    print("=" * 40)


def play_round(deck: Deck, money: int) -> Tuple[int, bool]:
    """
    Play a single round of Blackjack.
    
    Args:
        deck: Card deck
        money: Player's current money
        
    Returns:
        Tuple of (new_money, continue_playing)
    """
    # Get bet
    bet = get_bet(money)
    if bet == -1:
        return money, False
    
    # Reset hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal initial cards
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Display initial state
    display_game_state(player_hand, dealer_hand, hide_dealer=True)
    
    # Check for immediate blackjack
    if player_hand.is_blackjack():
        display_game_state(player_hand, dealer_hand, hide_dealer=False)
        result, money_change = determine_winner(player_hand, dealer_hand, bet)
        print(f"\n{result}")
        print(f"You won ${abs(money_change)}!")
        return money + money_change, True
    
    # Player's turn
    while True:
        choice = get_player_choice()
        
        if choice == 'quit':
            return money, False
        
        if choice == 'hit':
            card = deck.deal()
            if card:
                player_hand.add_card(card)
                print(f"\nYou received: {card}")
                display_game_state(player_hand, dealer_hand, hide_dealer=True)
                
                if player_hand.is_busted():
                    print("\nYou busted!")
                    result, money_change = determine_winner(player_hand, dealer_hand, bet)
                    print(f"\n{result}")
                    print(f"You lost ${abs(money_change)}!")
                    return money + money_change, True
        
        elif choice == 'stand':
            break
    
    # Dealer's turn
    dealer_turn(deck, dealer_hand)
    
    # Final display and results
    display_game_state(player_hand, dealer_hand, hide_dealer=False)
    
    result, money_change = determine_winner(player_hand, dealer_hand, bet)
    print(f"\n{result}")
    
    if money_change > 0:
        print(f"You won ${money_change}!")
    elif money_change < 0:
        print(f"You lost ${abs(money_change)}!")
    else:
        print("It's a push!")
    
    return money + money_change, True


def play_game():
    """Main game function."""
    display_welcome()
    
    # Initialize
    deck = Deck()
    money = 1000  # Starting money
    
    print(f"Starting money: ${money}")
    
    rounds_played = 0
    wins = 0
    losses = 0
    
    while money > 0:
        print(f"\n{'=' * 40}")
        print(f" ROUND {rounds_played + 1}")
        print(f"{'=' * 40}")
        
        # Check if deck needs reshuffling
        if len(deck.cards) < 20:
            print("\nReshuffling deck...")
            deck.reset()
        
        # Play round
        money, continue_playing = play_round(deck, money)
        
        if not continue_playing:
            break
        
        rounds_played += 1
        
        # Update stats
        if money > 1000:
            wins += 1
        elif money < 1000:
            losses += 1
        
        print(f"\nYour money: ${money}")
        
        if money <= 0:
            print("\nYou're out of money! Game over!")
            break
        
        # Ask to continue
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ['no', 'n']:
            break
    
    # Final stats
    print(f"\n{'=' * 60}")
    print(f" FINAL RESULTS")
    print(f"{'=' * 60}")
    print(f"Starting money: $1000")
    print(f"Final money: ${money}")
    print(f"Profit/Loss: ${money - 1000}")
    print(f"Rounds played: {rounds_played}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    
    if money > 1000:
        print("\nCongratulations! You're a winner!")
    elif money == 1000:
        print("\nYou broke even!")
    else:
        print("\nBetter luck next time!")
    
    print(f"{'=' * 60}")
    print("\nThanks for playing Blackjack!")


def main():
    """Main entry point."""
    play_game()


if __name__ == "__main__":
    main()
import random
#importing the random 

class CardDealer:
    """This class represts a deck of 52 shuffled cards with a dealing mechanism."""

    def __init__(self):
        """Initialize and shuffle the deck of 52 cards."""
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.deck = [f"{rank} of {suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)  # Shuffle the deck
        print("Card Dealer")
        print("I have shuffled a deck of 52 cards.")

    def deal_cards(self, num_cards):
        """Deal the requested number of cards if available."""
        if num_cards > len(self.deck):
            print(f"Sorry, only {len(self.deck)} cards left in the deck.")
            return self.deck[:]  # Return all remaining cards

        cards_dealt = self.deck[:num_cards]  # Get the requested cards
        self.deck = self.deck[num_cards:]  # Remove dealt cards from deck
        return cards_dealt

    def cards_left(self):
        """Return the number of cards left in the deck."""
        return len(self.deck)


def main():
    """Main function to run the card dealing application."""
    dealer = CardDealer()

    while True:
        if dealer.cards_left() == 0:
            print("No more cards left in the deck! The game is over.")
            break

        try:
            num_cards = int(input("\nHow many cards would you like? "))
            if num_cards < 1:
                print("You must request at least one card.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Deal cards
        cards = dealer.deal_cards(num_cards)
        print("\nYour cards:")
        for card in cards:
            print(card)

        # Display remaining cards
        print(f"\nCards left in the deck: {dealer.cards_left()}")

        # Ask user to continue or exit
        while True:
            choice = input("\nDo you want to continue or exit? (y/n): ").strip().lower()
            if choice == 'y':
                break  # Continue dealing
            elif choice == 'n':
                print("Good luck!")
                return  # Exit the program
            else:
                print("Invalid command. Please enter 'y' to continue or 'n' to exit.")

if __name__ == "__main__":
    main()

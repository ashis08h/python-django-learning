import random


class Deck:
    """
    Class responsible to suffle the cards and distribute between two persons.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        """
        Initializes the deck by creating a list of all 52 cards.
        """
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(f'{rank} of {suit}')

    def shuffle(self):
        """
        Method to Shuffles the deck of cards randomly.
        """
        random.shuffle(self.cards)

    def split(self):
        """
        Splits the deck into two halves. If odd, the extra card remains in the original deck.
        """
        middle = len(self.cards) // 2
        first_half = self.cards[:middle]
        second_half = self.cards[middle:]
        return first_half, second_half

    def __str__(self):
        """Returns a string representation of the deck."""
        return ', '.join(self.cards)


deck = Deck()
deck.shuffle()

first_half, second_half = deck.split()

# Print the two halves of the deck
print("First Half:")
print(first_half)
print("\nSecond Half:")
print(second_half)

from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        self._new_hand = []

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        cards_left = self.count()
        to_remove = min([cards_left, num])
        if cards_left == 0:
            raise ValueError("All cards have been dealt")
        else:
            self._new_hand = self.cards[-to_remove:]
            self.cards = self.cards[:-to_remove]
        return self._new_hand

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            return shuffle(self.cards)

    def deal_card(self):
        self._deal(1)
        return self._new_hand[0]

    def deal_hand(self, num):
        self._deal(num)
        return self._new_hand


d = Deck()
print(d.cards)
d.shuffle()
print(d.cards)
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.cards)

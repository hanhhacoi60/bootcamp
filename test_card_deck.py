from card_deck import Card, Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.sample_card = Card("Clubs", "J")

    def test_init(self):
        self.assertEqual(self.sample_card.suit, "Clubs")
        self.assertEqual(self.sample_card.value, "J")

    def test_repr(self):
        self.assertEqual(repr(self.sample_card), "J of Clubs")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.sample_deck = Deck()

    def test_init(self):
        self.assertIsInstance(self.sample_deck.cards, list)
        self.assertEqual(len(self.sample_deck.cards), 52)

    def test_repr(self):
        self.assertEqual(repr(self.sample_deck), "Deck of 52 cards")

    def test_iter(self):
        self.assertTrue(iter(self.sample_deck))

    def test_count(self):
        self.assertEqual(self.sample_deck.count(), 52)
        self.sample_deck.cards.pop()
        self.assertEqual(self.sample_deck.count(), 51)

    def test_deal_cards(self):
        self.sample_deck._deal(10)
        self.assertEqual(len(self.sample_deck.cards), 42)
        self.assertEqual(len(self.sample_deck._new_hand), 10)

    def test_deal_last(self):
        self.sample_deck._deal(56)
        self.assertEqual(len(self.sample_deck.cards), 0)
        self.assertEqual(len(self.sample_deck._new_hand), 52)

    def test_deal_no_cards(self):
        self.sample_deck.cards.clear()
        with self.assertRaises(ValueError):
            self.sample_deck._deal(2)

    def test_deal_card(self):
        result = self.sample_deck.deal_card()
        self.assertIsInstance(result, Card)
        self.assertEqual(result, self.sample_deck._new_hand[0])
        self.assertEqual(len(self.sample_deck.cards), 51)
        self.assertEqual(len(self.sample_deck._new_hand), 1)

    def test_deal_hand(self):

        result = self.sample_deck.deal_hand(15)
        self.assertIsInstance(result, list)
        self.assertEqual(len(self.sample_deck.cards), 37)
        self.assertEqual(len(self.sample_deck._new_hand), 15)

    def test_shuffle_invalid(self):
        """shuffle raises a ValueError if the card deck is not full"""
        self.sample_deck.cards.pop()
        with self.assertRaises(ValueError):
            self.sample_deck.shuffle()

    def test_shuffle_valid(self):
        """shuffle shuffles a full deck in place"""
        original = self.sample_deck.cards[:] #making a new copy b/c lists are mutable!
        self.sample_deck.shuffle()
        result = self.sample_deck.cards
        self.assertEqual(len(result), 52)
        self.assertFalse(original == result)

if __name__ == "__main__":
    unittest.main()

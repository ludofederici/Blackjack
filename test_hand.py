import unittest
from hand import Hand
from card import Rank, Suit, Card

class TestHand(unittest.TestCase):

	def setUp(self):
		self.ace_of_clubs = Card(Rank.ACE, Suit.CLUB)
		self.ace_of_diamonds = Card(Rank.ACE, Suit.DIAMOND)
		self.ace_of_hearts = Card(Rank.ACE, Suit.HEART)
		self.two_of_diamonds = Card(Rank.TWO, Suit.DIAMOND)
		self.five_of_spades = Card(Rank.FIVE, Suit.SPADE)
		self.ten_of_hearts = Card(Rank.TEN, Suit.HEART)
		self.jack_of_clubs = Card(Rank.JACK, Suit.CLUB)
		self.eight_of_diamonds = Card(Rank.EIGHT, Suit.DIAMOND)

	"""tests the Hand.min_value method to ensure the ace is counted as 1"""
	def test_min_value(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.ten_of_hearts)
		hand.add_card(self.eight_of_diamonds)
		value = hand.min_value()
		self.assertEqual(value, 19, "Should be 19")

	"""test of Hand.max_value method to ensure 1 ace is counted as 11 & the other as 1"""
	def test_max_value_two_aces(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.ace_of_diamonds)
		value = hand.max_value()
		self.assertEqual(value, 12, "Should be 12")

	"""test Hand.max_value method make sure that 2 aces are valued at 1 and 1 ace counts as 11"""
	def test_max_value_three_aces_one_five(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.ace_of_diamonds)
		hand.add_card(self.ace_of_hearts)
		hand.add_card(self.five_of_spades)
		value = hand.max_value()
		self.assertEqual(value, 18, "Should be 18")

	"""test Hand.max_value to make sure that an ace is valued at 1 when the other cards have a value of 11 or more"""
	def test_max_value_ace_five_ten(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.five_of_spades)
		hand.add_card(self.ten_of_hearts)
		value = hand.max_value()
		self.assertEqual(value, 16, "Should be 16")

	"""test Hand.has_blackjack when the hand has a blackjack"""
	def test_has_blackjack(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.ten_of_hearts)
		self.assertEqual(hand.has_blackjack(), True, "Should be True")

	"""test Hand.has_blackjack when the hand does not have a blackjack"""
	def test_not_has_blackjack(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.eight_of_diamonds)
		self.assertEqual(hand.has_blackjack(), False, "Should be False")

	"""tests Hand.has_blackjack when the value of the cards equals 21 but there are more than 2 cards in the hand"""
	def test_not_has_blackjack_three_cards(self):
		hand = Hand()
		hand.add_card(self.ace_of_clubs)
		hand.add_card(self.eight_of_diamonds)
		hand.add_card(self.two_of_diamonds)
		self.assertEqual(hand.has_blackjack(), False, "Should be False")


if __name__ == '__main__':
	unittest.main()


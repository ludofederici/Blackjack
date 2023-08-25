from enum import Enum
import random 

class Rank(Enum):
	"""represents all the ranks of cards in a deck"""
	ACE = "A"
	TWO = "2"
	THREE = "3"
	FOUR = "4"
	FIVE = "5"
	SIX = "6"
	SEVEN = "7"
	EIGHT = "8"
	NINE = "9"
	TEN = "10"
	JACK = "J"
	QUEEN = "Q"
	KING = "K"

	def __str__(self):
		return self.value 

class Suit(Enum):
	"""represents all the suits of cards in a deck"""

	"""escape sequence for bright red + Unicode character for diamond + Escape sequence to reset attributes"""
	DIAMOND = u'\033[91m\u2666\033[0m'

	"""unicode character for club"""
	CLUB = u'\u2663'

	"""escape sequence for bright red + Unicode character for heart + Escape sequence to reset attributes"""
	HEART = u'\033[91m\u2665\033[0m'

	"""unicode character for spade"""
	SPADE = u'\u2660'

	def __str__(self):
		return self.value

class Card:
	"""represents the rank, suit, and whether the card is face up or down for a card"""
	def __init__(self, rank, suit, is_face_up = True):
		self.rank = rank
		self.suit = suit
		self.is_face_up = is_face_up

	"""either reveals the cards rank and suit or X when the dealer's card is face down"""
	def __str__(self):
		if self.is_face_up:
			return f"[{self.rank}{self.suit}]"
		else:
			return "[X]"	

	"""gives a value to each rank"""
	def value(self):
		if self.rank == Rank.ACE:
			return 1
		elif self.rank == Rank.TWO:
			return 2
		elif self.rank == Rank.THREE:
			return 3
		elif self.rank == Rank.FOUR:
			return 4
		elif self.rank == Rank.FIVE:
			return 5
		elif self.rank == Rank.SIX:
			return 6
		elif self.rank == Rank.SEVEN:
			return 7
		elif self.rank == Rank.EIGHT:
			return 8
		elif self.rank == Rank.NINE:
			return 9
		elif self.rank == Rank.TEN:
			return 10
		elif self.rank == Rank.JACK:
			return 10
		elif self.rank == Rank.QUEEN:
			return 10
		elif self.rank == Rank.KING:
			return 10


class Shoe:
	"""represents the decks in the shoe"""
	def __init__(self, num_decks):
		"""creates num_deck of 52 cards and shuffles them together"""	
		self.cards = []
		for _ in range(num_decks):
			for rank in Rank:
				for suit in Suit:
					self.cards.append(Card(rank, suit))
		random.shuffle(self.cards)

	"""retreives the next card in the shoe"""
	def next_card(self):
		return self.cards.pop()

	"""checks if there are enough cards in the shoe for a new round"""
	def has_enough_for_new_hand(self):
		return len(self.cards) > 20


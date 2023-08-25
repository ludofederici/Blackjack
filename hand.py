from card import Rank, Card
from actions import Action

class Hand:
	"""represents the hands"""

	def __init__(self, hand_num = 1):
		self.cards = []
		self.bet = 0
		self.hand_num = hand_num
		self.was_split = False

	def add_card(self, card):
		"""adds a card to the hand"""
		self.cards.append(card) 

	def __str__(self):
		"""creates a string showing the hand as comma-separated cards"""
		return ",".join([str(card) for card in self.cards])

	def min_value(self):
		"""value of the hand with the card rank "ace" as one"""
		return sum([card.value() for card in self.cards])

	def max_value(self):
		"""max possible value of a hand that is less than or equal to 21. values 1 ace as 11 if possible"""
		value = self.min_value()
		if Rank.ACE in [card.rank for card in self.cards]:
			if value + 10 <= 21:
				value += 10
		return value 

	def is_bust(self):
		"""determines if a hand is bust"""
		return self.min_value() > 21

	def has_blackjack(self):
		"""determines if a hand has blackjack"""
		return self.max_value() == 21 and len(self.cards) == 2

	def available_actions(self, balance):
		"""determines the possible actions the player has with their hand"""
		actions = [Action.STAND, Action.HIT]

		if balance >= self.bet:
			"""checks if the player can double down"""
			hand_value = self.min_value()
			if hand_value >= 9 and hand_value <= 11 and len(self.cards) == 2:
				actions.append(Action.DOUBLE_DOWN)

			"""checks if the player can split their hand"""
			if len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank:
				actions.append(Action.SPLIT)

		return actions

	def display(self):
		"""if the player splits their hand, the method prints their different hands accordingly"""
		prefix = ""
		if self.was_split:
			if self.hand_num == 1:
				prefix = "1st "
			elif self.hand_num == 2:
				prefix = "2nd "
			elif self.hand_num == 3:
				prefix = "3rd "
			else:
				prefix = f"{self.hand_num}th "
		print(f"Your {prefix}hand: {self}")

from hand import Hand

class Dealer:
	"""An object to represent the blackjack dealer"""

	def __init__(self):
		self.hand = Hand()

	"""creates an empty hand before the round starts. cards will be added to the hand when the cards are dealt"""
	def clear_hand(self):
		self.hand = Hand()

	"""prints the dealer's hand"""
	def display_hand(self):
		print(f"My hand: {self.hand}")

	"""reveals all the cards in the dealer's hand"""
	def reveal_cards(self):
		for card in self.hand.cards:
			card.is_face_up = True
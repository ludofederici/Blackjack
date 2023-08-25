from hand import Hand

class Player:
	"""An object to represent the player"""

	def __init__(self, balance):
		self.balance = balance
		self.hands = [Hand()]

	"""creates an empty hand before the round starts. cards will be added to the hand when the cards are dealt"""
	def clear_hands(self):
		self.hands = [Hand()]

	"""adds the specified new hand after a player has split"""
	def add_hand(self, hand):
		self.hands.append(hand)

	"""retrieves the player's hand. the first value corresponds to hand_num = 1"""
	def get_hand(self, hand_num):
		return self.hands[hand_num - 1]

	"""returns true only if all the player's hands are bust"""
	def are_all_hands_bust(self):
		for hand in self.hands:
			if not hand.is_bust():
				return False
		return True

	"""displays the player's hand(s) to the user"""
	def display_hands(self):
		for hand in self.hands:
			hand.display()




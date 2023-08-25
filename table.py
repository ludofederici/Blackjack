from card import Card, Shoe, Rank
from player import Player
from dealer import Dealer
from hand import Hand
from actions import Action
from helper import input_integer

class Table:
	"""An object to represent a blackjack table"""

	def __init__(self, num_decks_in_shoe, player):
		self.num_decks_in_shoe = num_decks_in_shoe
		self.player = player
		self.dealer = Dealer()
		self.shoe = Shoe(num_decks_in_shoe) 

	def play(self):
		"""loops to continue playing rounds of blackjack until the player has no money left or quits by
		entering a bet of 0
		"""
		while self.player.balance > 0:
			"""this condition checks if there are enough cards in the shoe for a new round.
			if there are not enough, it will create a new shoe
			"""
			if not self.shoe.has_enough_for_new_hand():
				print("Reshuffling the shoe")
				self.shoe = Shoe(self.num_decks_in_shoe) 

			print(f"Your current balance is {self.player.balance} dollars.")
			max_bet = self.player.balance
			bet = input_integer(f"How much would you like to bet? (0 - {max_bet}) ", 0, max_bet)
			if bet > 0:
				self.play_round(bet) 
			else:
				"""player quit by entering a bet of 0"""
				return

	def play_round(self, bet):
		"""plays 1 round of blackjack"""
		self.dealer.clear_hand()
		self.player.clear_hands()

		hand_num = 1
		"""hand for player is set to 1, it will only change when they have the option to split their hand"""
		hand = self.player.get_hand(hand_num)

		self.deal_cards(hand)

		self.dealer.display_hand()
		hand.display()

		"""check if either the player or dealer has blackjack with their dealt cards"""
		dealer_has_blackjack = self.dealer.hand.has_blackjack()
		player_has_blackjack = hand.has_blackjack()
		if dealer_has_blackjack and player_has_blackjack:
			"""both the dealer and player have blackjack, so the round is over,
			and no money is won or lost
			"""
			self.dealer.reveal_cards()
			self.show_hands()
			print("We both have blackjack, so we tied")
			return
		elif dealer_has_blackjack:
			"""only the dealer has blackjack, so reveal the cards and collect the bet from the player"""
			self.dealer.reveal_cards()
			self.show_hands()
			print(f"I have blackjack, so you lose {bet}")
			self.player.balance -= bet
			return
		elif player_has_blackjack:
			"""only the player has blackjack, so they win 1.5 times the amount of their bet"""
			self.dealer.reveal_cards()
			self.show_hands()
			winnings = bet + bet // 2
			print(f"You have blackjack, so you win {winnings}")
			self.player.balance += winnings
			return 

		original_balance = self.player.balance
		has_more_hands = True
		"""Continue to handle player actions until the player stands or busts on each of their hands."""
		while has_more_hands:
			hand.bet = bet

			if hand_num > 1:
				hand.display()
			self.play_hand(hand)

			if hand.is_bust():
				print(f"You busted. You lost {hand.bet} dollars")

			hand_num += 1
			if len(self.player.hands) >= hand_num:
				hand = self.player.get_hand(hand_num)
			else:
				has_more_hands = False
		
		"""the dealer now reveals their hidden card and plays unless the player has busted on all their hands"""
		self.dealer.reveal_cards()
		if not self.player.are_all_hands_bust(): 
			self.play_dealer()
			if self.dealer.hand.is_bust():
				"""if the dealer busts, the player collects their winnings"""
				winnings = 0
				for hand in self.player.hands:
					if not hand.is_bust():
						winnings += hand.bet
				self.show_hands()
				print(f"I busted. You won {winnings} dollars")
				"""returning the bet + winnings to balance"""
				self.player.balance += 2 * winnings
				return 

			"""the dealer's hand is compared to all the player's hands that didn't bust to settle the bets"""
			dealer_hand_value = self.dealer.hand.max_value()
			for hand in self.player.hands:
				if not hand.is_bust():
					player_hand_value = hand.max_value()
					if player_hand_value > dealer_hand_value:
						self.player.balance += 2 * hand.bet
					elif player_hand_value == dealer_hand_value:
						"""Returning the bet after a tie"""
						self.player.balance += hand.bet

		"""the profit is determined, and the dealer announces the result"""
		self.show_hands()
		profit = self.player.balance - original_balance
		if profit > 0:
			print(f"You won {profit} dollars")
		elif profit < 0:
			print(f"You lost {-profit} dollars")
		else:
			print("We tied")

	def show_hands(self):
		"""prints the hands of the dealer and the player"""
		self.dealer.display_hand()
		self.player.display_hands()

	def deal_cards(self, player_hand):
		"""deals cards to the player (first) and then the dealer and then the player and dealer again.
		all cards are face up except the dealer's second card
		"""
		dealer_hand = self.dealer.hand
		player_hand.add_card(self.shoe.next_card())
		dealer_hand.add_card(self.shoe.next_card())
		player_hand.add_card(self.shoe.next_card())
		card = self.shoe.next_card()
		card.is_face_up = False
		dealer_hand.add_card(card)

	def play_hand(self, hand):
		"""plays out the specified hand, requesting actions from the player until the hand is finished"""
		self.player.balance -= hand.bet

		while True:
			if hand.was_split and hand.cards[0].rank == Rank.ACE:
				"""can only draw one card after splitting aces"""
				return

			action = self.request_action(hand)
			if action == Action.STAND:
				"""hand is finished when the player stands"""
				return
			elif action == Action.HIT:
				self.hit(hand)
				hand.display()
				if hand.is_bust():
					return
			elif action == Action.DOUBLE_DOWN:
				"""when the player doubles down, their bet doubles"""
				self.player.balance -= hand.bet
				self.double_down(hand)
				hand.display()
				return
			elif action == Action.SPLIT:
				"""this hand continues, and a new hand is added"""
				self.split(hand)
				hand.display()

	def play_dealer(self):
		"""the dealer hits until the hand value is 17 or more"""
		dealer_hand = self.dealer.hand
		while dealer_hand.max_value() < 17:
			self.hit(dealer_hand)

	def hit(self, hand):
		"""add a card from the shoe to the specified hand"""
		hand.add_card(self.shoe.next_card())

	def double_down(self, hand):
		"""double the bet and hit"""
		hand.bet *= 2
		self.hit(hand)

	def split(self, hand):
		"""update the current hand by keeping 1 card and drawing a new one.
		create a new hand with a card from the specified hand plus a new card from the shoe.
		"""
		card = hand.cards.pop()
		hand.add_card(self.shoe.next_card())
		hand.was_split = True 

		split_hand_num = len(self.player.hands) + 1
		split_hand = Hand(split_hand_num)
		split_hand.add_card(card)
		split_hand.add_card(self.shoe.next_card())
		split_hand.bet = hand.bet
		split_hand.was_split = True
		self.player.add_hand(split_hand)

	def request_action(self, hand):
		"""displays the current available actions and keep asking until a valid action choice is provided"""
		actions = hand.available_actions(self.player.balance)
		options = " or ".join([str(action) for action in actions])
		choices = ", ".join([action.choice() for action in actions])

		while True:
			response = input(f"Would you like to {options}? ({choices}) ")
			for action in actions:
				if action.choice() == response:
					return action





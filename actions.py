from enum import Enum

class Action(Enum):
	"""represents all the actions a player can choose between"""
	STAND = "stand"
	HIT = "hit"
	DOUBLE_DOWN = "double down"
	SPLIT = "split"

	def __str__(self):
		return self.value 

	def choice(self):
		"""gives each action an acronym, making it easier for the user to choose an action"""
		if self == Action.STAND:
			return "s"
		elif self == Action.HIT:
			return "h"
		elif self == Action.DOUBLE_DOWN:
			return "d"
		elif self == Action.SPLIT:
			return "x"	


class Deck():
	"""Represents standard 52-card deck of playing cards."""
	
	def __init__(self):
		"""Initialize a deck with attributes."""
		self.suits = ['H', 'D', 'C', 'S']
		self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(rank, suit) for suit in self.suits 
					         for rank in self.ranks
		]

	def __str__(self):
		"""Modify str method to display Deck as a list of tuples."""
		result = '['
		for i, card in enumerate(self.cards):
			if i == 0:
				result += str(card)
			else:
				result += ', ' + str(card)
		result += ']'
		return result


class Card(): # !!! "tuple object has no attr 'rank'" Use classes when access attr
	"""Represents a playing card."""
	
	def __init__(self, rank, suit):
		"""Initialize playing card."""
		self.rank = rank
		self.suit = suit
		self.num = self.give_numerical_rank(self.rank)
		# !!! Easier to count for our test; can't search ion class obj. easily
		self.attributes = (self.rank, self.suit, self.num) 

	def __str__(self):
		"""Modify str method to display Card attributes in a tuple."""
		return '(' + self.rank + ', ' + self.suit + ', ' + str(self.num) + ')'	
	
	def give_numerical_rank(self, rank):
		"""Helper method: Gives numerical value to be assigned to attribute."""
		numerical_rank_dict = {
			'A': (1, 14),
			'J': 11,
			'Q': 12, 
			'K': 13
		}
		
		if rank in numerical_rank_dict:
			# Function should return, NOT modify state!
			return numerical_rank_dict[rank]
		else:
			return int(rank)
from random import shuffle

import deck as d

class Game():
	"""Represents a game of Texas Hold'em."""

	def __init__(self):
		"""Initialize a game with proper attributes."""
		self.deck = d.Deck()

	def shuffle_deck(self):
		"""Shuffles the deck before each game."""
		shuffle(self.deck.cards) # !!! Changes the state of the game deck.
from random import shuffle

import deck as d
import player as p

class Game():
	"""Represents a game of Texas Hold'em."""

	def __init__(self, num_of_players):
		"""Initialize a game with proper attributes."""
		self.deck = d.Deck()
		self.num_of_players = num_of_players
		self.players = [p.Player() for i in range(self.num_of_players)]

	def shuffle_deck(self):
		"""Shuffles the deck before each game."""
		shuffle(self.deck.cards) # !!! Changes the state of the game deck.

	def deal(self):
		"""Deals five cards to all players one card at a time."""
		finished_dealing = False
		while not finished_dealing:
			for player in self.players:
				player.cards.append(self.deck.cards.pop()) # !!! Changes state of game deck AND player.hand

			if len(self.players[-1].cards) == 5:
				finished_dealing = True

		return None

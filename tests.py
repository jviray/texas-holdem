import unittest
import deck as d

class DeckClassTestCase(unittest.TestCase):
	"""Tests for Deck class."""
	
	def setUp(self):
		"""Setup a deck to be used in all test methods."""
		self.deck = d.Deck()
		self.cards = self.deck.cards

	def counter(self, targets, num_of_each, cards): # !!!
		"""Helper method: Check if proper number of each target is present."""
		counts = []
			 
		for target in targets:
			count = 0
			for card in cards:
				if target in card.attributes:
					count += 1
			counts.append(count)
			
		for count in counts:
			if count != num_of_each:
				return False
			
		return True
	
	def test_total_number_of_cards(self):
		"""Test length of the deck."""
		num_of_cards = len(self.cards)
		self.assertEqual(num_of_cards, 52)
	
	def test_all_suits(self):
		"""Test that there are 13 of each suit ('H', 'D', 'C', 'S')."""
		suits = ['H', 'D', 'C', 'S']
		number_of_each = 13
		
		self.assertEqual(self.counter(suits, number_of_each, self.cards), True)
	
	def test_all_ranks(self):
		"""Test that there are 4 of each rank ('A', 2, 3 ... 'K')."""
		ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		number_of_each = 4
		
		self.assertEqual(self.counter(ranks, number_of_each, self.cards), True)
	
	def test_all_numerical_ranks(self):
		"""Test that each rank has appropriate numerical rank."""
		
		def check_proper_num_value(cards):
			"""Helper test method: Check that numerical ranks are correct. """
			face_ranks = ['A', 'J', 'Q', 'K']
			
			for card in cards:
				if card.rank == 'A' and card.num != (1, 14):
					return False
				elif card.rank == 'J' and card.num != 11:
					return False
				elif card.rank == 'Q' and card.num != 12:
					return False
				elif card.rank == 'K' and card.num != 13:
					return False
				elif card.rank not in face_ranks and int(card.rank) != card.num:
					return False
					
			return True
		
		self.assertEqual(check_proper_num_value(self.cards), True)
		
unittest.main()
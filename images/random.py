import random

class Random:
	def __init__(self, values):
		self.values = values

	def resolve(self):
		return random.choice(self.values)
import random

class Random_Images:
	def __init__(self, images):
		self.images = images

	def next(self):
		return random.choice(self.images)
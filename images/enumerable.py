class Enumerable:
	def __init__(self, values, index):
		self.values = values
		self.index = index

	def resolve(self):
		index = self.index.next()
		return self.values[index % len(self.values)]

	def __get_index_from_file(self):
		name = 'data.iit'
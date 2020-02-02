class And_Expression:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def result(self, argument):
		return self.first.result(argument) and self.second.result(argument)
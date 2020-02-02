#TODO : next() is bad

class Condition:
	def __init__(self, cases, otherwise):
		self.cases = cases
		self.otherwise = otherwise

	def result(self, argument):
		for case in self.cases:
			if case.expression.result(argument):
				return case.result.next()

		return self.otherwise.next()
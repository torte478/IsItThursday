class Condition:
	def __init__(self, cases, otherwise):
		self.cases = cases
		self.otherwise = otherwise

	def resolve(self, argument):
		for case in self.cases:
			if case.expression.result(argument):
				return case.result.resolve()

		return self.otherwise.resolve()
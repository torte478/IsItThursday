class Expression:
	def __init__(self, expression, expected):
		self.expression = expression
		self.expected = expected

	def result(self, argument):
		raise "IT IS NOT REQUIRED"
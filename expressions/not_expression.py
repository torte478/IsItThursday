class Not_Expression:
	def __init__(self, origin):
		self.origin = origin

	def result(self, argument):
		return not(self.origin.result(argument))
class Text_File:
	def __init__(self, path):
		self.path = path

	def text(self):
		with open(self.path, 'r') as file:
			return file.read()
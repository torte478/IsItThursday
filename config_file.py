class Config_File:
	def __init__(self, path):
		self.path = path

	def config(self):
		with open(self.path, 'r') as file:
			return file.read()
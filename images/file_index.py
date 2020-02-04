import os

class File_Index:
	def __init__(self, name):
		self.name = name

	def next(self):
		self.__check_file_existing()
		
		index = self.__read_index_from_file()
		self.__write_index_to_file(index + 1)

		return index

	def __read_index_from_file(self):
		file = open(self.name, 'r')
		index = int(file.readline())
		file.close()
		return index

	def __write_index_to_file(self, index):
		file = open(self.name, 'w')
		file.write(str(index % 100))
		file.close()
		return

	def __check_file_existing(self):
		if not(os.path.exists(self.name)):
			__write_index_to_file(0)
		return

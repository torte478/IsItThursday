import os

#TODO : replace file logic
#TODO rename images.* to something another
class Enumerable_Images:
	def __init__(self, images):
		self.images = images

	def next(self):
		index = self.__get_index_from_file()
		return self.images[index % len(self.images)]

	def __get_index_from_file(self):
		name = 'data.iit'
		self.__check_file_existing(name)
		
		index = self.__read_index_from_file(name)
		self.__write_index_to_file(name, index + 1)

		return index

	def __read_index_from_file(self, name):
		file = open(name, 'r')
		index = int(file.readline())
		file.close()
		return index

	def __write_index_to_file(self, name, index):
		file = open(name, 'w')
		file.write(str(index % 100))
		file.close()
		return

	def __check_file_existing(self, name):
		if not(os.path.exists(name)):
			__write_index_to_file(name, 0)
		return
		
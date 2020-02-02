import json
import random
from text_file import *

class Json_Condition:
	def __init__(self, root):
		self.root = root

	def condition(self):
		cases = self.__build_cases(self.root['cases'])
		otherwise = self.__build_images(self.root['otherwise'])
		return Condition(cases, otherwise)

	def __build_cases(self, cases):
		result = []
		for case in cases:
			expression = self.__build_expression(case['expression'])
			images = self.__build_images(case['result'])
			result.append(Case(expression, result))
		return result

	def __build_expression(self, expression):
		return Expression(expression['filter'], expression['value']) #TODO

	def __build_images(self, images):
		return Random_Images(images['values']) \
				if images['type'] == 'random' \
				else Enumerable_Images(images['values'])

class Expression:
	def __init__(self, filter, expected):
		self.filter = filter
		self.expected = expected

class Case:
	def __init__(self, expression, result):
		self.expression = expression
		self.result = result


class Condition:
	def __init__(self, cases, otherwise):
		self.cases = cases
		self.otherwise = otherwise


class Random_Images:
	def __init__(self, images):
		self.images = images

	def next(self):
		return random.choice(self.images)



class Enumerable_Images:
	def __init__(self, images):
		self.images = images

	def next(self):
		raise "NOT IMPLEMENTED" #TODO


res = Json_Condition( \
		json.loads( \
			Text_File('config.json') \
				.text()
			)
	   	).condition()
print(res.cases[0].expression.expected)

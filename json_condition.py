from expressions.expression import *
from expressions.and_expression import *
from expressions.not_expression import *
from expressions.or_expression import *
from expressions.case import *
from expressions.condition import *
from images.enumerable import *
from images.random import *


#TODO : remove constructors
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
		if 'operator' in expression:
			return self.__build_complicate_expression(expression)
		else:
			return Expression(expression['filter'], expression['value'])

	def __build_complicate_expression(self, expression):
		if expression['operator'] == 'not':
			argument = self.__build_expression(expression['argument'])
			return Not_Expression(argument)
		else:
			first = self.__build_expression(expression['first'])
			second = self.__build_expression(expression['second'])
			return And_Expression(first, second) \
					if expression['operator'] == 'and' \
					else Or_Expression(first, second)

	def __build_images(self, images):
		return Random_Images(images['values']) \
				if images['type'] == 'random' \
				else Enumerable_Images(images['values'])
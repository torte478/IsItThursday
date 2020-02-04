#TODO : refactor
from expressions.and_expression import *
from expressions.not_expression import *
from expressions.or_expression import *
from expressions.case import *
from expressions.condition import *
from images.enumerable import *
from images.file_index import *
from images.random import *
from datetime_filters import *

class Json_Condition:
	def __init__(self, root, tree):
		self.tree = tree
		self.root = root

	def condition(self):
		cases = self.__build_cases(self.root['cases'])
		otherwise = self.__build_images(self.root['otherwise'])
		return self.tree.an_expressions().a_condition(cases, otherwise)

	def __build_cases(self, cases):
		result = []
		for case in cases:
			expression = self.__build_expression(case['expression'])
			images = self.__build_images(case['result'])
			result.append(self.tree.an_expressions().a_case(expression, images))
		return result

	def __build_expression(self, expression):
		if 'operator' in expression:
			return self.__build_complicate_expression(expression)
		else:
			return self.__build_token(expression['filter'], expression['value'])

	def __build_token(self, name, expected):
		if name == 'weekday':
			return self.tree.a_filters().weekday(expected)
		else:
			if name == 'day':
				return self.tree.a_filters().day(expected)
			else:
				if name == 'month':
					return self.tree.a_filters().month(expected)
				else:
					return self.tree.a_filters().year(expected)

	def __build_complicate_expression(self, expression):
		if expression['operator'] == 'not':
			argument = self.__build_expression(expression['argument'])
			return self.tree.an_expressions().a_not_ex(argument)
		else:
			first = self.__build_expression(expression['first'])
			second = self.__build_expression(expression['second'])
			return self.tree.an_expressions().an_and_ex(first, second) \
					if expression['operator'] == 'and' \
					else self.tree.an_expressions().an_or_ex(first, second)

	def __build_images(self, images):
		return self.tree.a_collections().a_random(images['values']) \
					if images['type'] == 'random' \
					else self.tree.a_collections().an_enumerable(images['values'])



class Tree:
	def __init__(self, expressions, filters, collections):
		self.expressions = expressions
		self.filters = filters
		self.collections = collections

	def an_expressions(self):
		return self.expressions

	def a_filters(self):
		return self.filters

	def a_collections(self):
		return self.collections

class Expressions:
	def __init__(self, case, condition, or_ex, and_ex, not_ex):
		self.case = case
		self.condition = condition
		self.or_ex = or_ex
		self.and_ex = and_ex
		self.not_ex = not_ex

	def a_case(self, expressions, result):
		return self.case(expressions, result)

	def a_condition(self, cases, otherwise):
		return self.condition(cases, otherwise)

	def an_or_ex(self, first, second):
		return self.or_ex(first, second)

	def an_and_ex(self, first, second):
		return self.and_ex(first, second)

	def a_not_ex(self, arg):
		return self.not_ex(arg)

class Collections:
	def __init__(self, random, enumerable):
		self.random = random
		self.enumerable = enumerable

	def a_random(self, values):
		return self.random(values)

	def an_enumerable(self, values):
		return self.enumerable(values)
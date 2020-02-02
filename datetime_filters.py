import datetime

#TODO: remove duplicate code
class Weekday_Filter:
	def __init__(self, expected):
		self.expected = expected

	def result(self, date):
		weekdays = {
		'monday': 0,
		'tuesday': 1,
		'wednesday': 2,
		'thursday': 3,
		'friday': 4,
		'saturday': 5,
		'sunday': 6
		}
		return date.weekday() == weekdays[self.expected]

class Day_Filter:
	def __init__(self, expected):
		self.expected = int(expected)

	def result(self, date):
		return date.day == self.expected

class Month_Filter:
	def __init__(self, expected):
		self.expected = int(expected)

	def result(self, date):
		return date.month == self.expected

class Year_Filter:
	def __init__(self, expected):
		self.expected = int(expected)

	def result(self, date):
		return date.year == self.expected
import datetime

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

class Date_Filter:
	def __init__(self, get_value, expected):
		self.get_value = get_value
		self.expected = int(expected)

	def result(self, date):
		return self.get_value(date) == self.expected

class Date_Filters:
	def day(self, expected):
		return Date_Filter(lambda date: date.day, expected)

	def month(self, expected):
		return Date_Filter(lambda date: date.month, expected)

	def year(self, expected):
		return Date_Filter(lambda date: date.year, expected)

	def weekday(self, expected):
		return Weekday_Filter(expected)
import datetime
import json


def read_config(name):
    with open(name) as file:
        data = json.load(file)
        return data


def get_match(name, expected):
    switch = {
        'weekday': match_weekday,
        'day': match_day,
        'month': match_month,
        'year': match_year
        }
    match = switch.get(name)
    return match(expected)


def match_weekday(expected):
    weekdays = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
        }
    return lambda date: date.weekday() == weekdays[expected]


def match_day(expected):
    return lambda date: date.day == int(expected)


def match_month(expected):
    return lambda date: date.month == int(expected)


def match_year(expected):
    return lambda date: date.year == int(expected)


def build_expression(expression):
    if 'operator' in expression:
        if (expression['operator'] == 'not'):
            return not(build_expression(expression['argument']))
        else:
            first = build_expression(expression['first'])
            second = build_expression(expression['second'])
            return (lambda x: first(x) and second(x)) if expression['operator'] == 'and' else (lambda x: first(x) or second(x))
    else:
        return get_match(expression['filter'], expression['value'])
#            
#
#
#
#'''
config = read_config('config.json')
condition = build_expression(config)
today = datetime.date.today()

result = condition(today)

print(result)
#'''
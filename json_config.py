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
            expr = build_expression(expression['argument'])
            return lambda x: not(expr(x))
        else:
            first = build_expression(expression['first'])
            second = build_expression(expression['second'])
            return (lambda x: first(x) and second(x)) if expression['operator'] == 'and' else (lambda x: first(x) or second(x))
    else:
        return get_match(expression['filter'], expression['value'])

def run_cases(cases, value):
    for case in cases['case']:
        expression = build_expression(case['expression'])
        match = expression(value)
        if match: return case['result']

    return cases['otherwise']    
#            
#
#
#
#'''
config = read_config('config.json')
today = datetime.date.today()
result = run_cases(config, today)

print(result)
#'''
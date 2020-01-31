import datetime
import json


def read_config(name):
    with open(name) as file:
        data = json.load(file)
        return data


def get_match(name):
    switch = {
        'weekday': match_weekday,
        'day': match_day,
        'month': match_month,
        'year': match_year
        }
    return switch.get(name)


def match_weekday(date, expected):
    weekdays = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
        }
    match = date.weekday() == weekdays[expected]
    return match


def match_day(date, expected):
    return date.day == int(expected)


def match_month(date, expected):
    return date.month == int(expected)


def match_year(date, expected):
    return date.year == int(expected)


def match_all(date, conditions):
    for condition in conditions:
        match = get_match(condition['filter'])
        if (match(date, condition['value']) == False): return False
        
    return True


def solve_expression(expression, date):
    if 'operator' in expression:
        if (expression['operator'] == 'not'):
            return not(solve_expression(expression['argument'], date))
        else:
            return solve_binary_expression(expression, date)
    else:
        match = get_match(expression['filter'])
        return match(date, expression['value'])


def solve_binary_expression(expression, date):
    first = solve_expression(expression['first'], date)
    second = solve_expression(expression['second'], date)
    return (first and second) if expression['operator'] == 'and' else (first or second)
#            
#
#
#
config = read_config('config.json')
today = datetime.date.today()
result = solve_expression(config, today)

print(result)

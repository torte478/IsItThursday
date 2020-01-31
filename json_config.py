import datetime
import json

def read_config(name):
    with open(name) as file:
        data = json.load(file)
        return (data['filter'], data['value'])

def get_condition(name):
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
        'wendesday': 2,
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




config = read_config('config.json')

today = datetime.date.today()
condition = get_condition(config[0])
result = condition(today, config[1])

print(result)

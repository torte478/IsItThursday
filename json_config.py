import datetime
import json

def read_config(name):
    with open(name) as file:
        data = json.load(file)
        return data['conditions']

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


def match_all(date, conditions):
    for condition in conditions:
        match = get_match(condition['filter'])
        if (match(date, condition['value']) == False): return False
        
    return True

conditions = read_config('config.json')
today = datetime.date.today()
result = match_all(today, conditions)

print(result)

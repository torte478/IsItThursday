import datetime

def get_match(config):
    switch = {
        'weekday': match_weekday,
        'day': match_day,
        'month': match_month,
        'year': match_year
        }
    match = switch.get(config['filter'])
    return match(config['value'])


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
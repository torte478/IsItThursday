import json

weekdays = {'monday': 0, 'tuesday': 1, 'wendesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
with open('config.json') as json_file:
    data = json.load(json_file)
    weekday = data['value']
    index = weekdays[weekday]
    print(index)

import datetime

import filters
import json_expression
import windows_api

expression = json_expression.read_from_file('config.json')
today = datetime.date.today()
image = json_expression.run(expression, filters.get_match, today)
print(image)
windows_api.set_wallpaper(image)
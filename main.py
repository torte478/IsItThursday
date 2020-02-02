import datetime
import json

from json_condition import Json_Condition
from text_file import Text_File
import windows_api


condition = Json_Condition( \
				json.loads( \
					Text_File('config.json') \
					.text() \
					) \
				) \
			.condition()

image = condition.result(datetime.date.today())
print(image)
windows_api.set_wallpaper(image)
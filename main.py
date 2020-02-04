import datetime
import json

from json_condition import Json_Condition
from text_file import Text_File
from windows_api import Windows_Wallpaper


condition = Json_Condition( \
				json.loads( \
					Text_File('config.json') \
					.text() \
					) \
				) \
			.condition()

image = condition.resolve(datetime.date.today())
print(image)
Windows_Wallpaper(image).set()

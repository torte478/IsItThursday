import datetime
import json

from json_condition import *
from text_file import Text_File
from windows_api import Windows_Wallpaper


condition = Json_Condition( \
				json.loads( \
					Text_File('config.json') \
					.text() \
					), \
				Tree( \
					Expressions( \
						lambda expressions, result: Case(expressions, result), \
						lambda cases, otherwise: Condition(cases, otherwise), \
						lambda first, second: Or_Expression(first, second), \
						lambda first, second: And_Expression(first, second), \
						lambda arg: Not_Expression(arg) \
						), \
					Date_Filters(), \
					Collections( \
						lambda values: Random(values),
						lambda values: Enumerable(values, File_Index('data.iit')) \
						) \
					) \
				) \
			.condition()

image = condition.resolve(datetime.date.today())
print(image)
Windows_Wallpaper(image).set()

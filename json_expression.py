import json
import os
import random

def read_from_file(name):
    with open(name) as file:
        data = json.load(file)
        return data

def run(cases, token, value):
    case = __get_case(cases, token, value)
    return __get_image_name(case)

def __get_case(cases, token, value):
    for case in cases['case']:
        expression = __build_expression(case['expression'], token)
        match = expression(value)
        if match: return case['result']

    return cases['otherwise']

def __build_expression(expression, token):
    if 'operator' in expression:
        if (expression['operator'] == 'not'):
            expr = __build_expression(expression['argument'])
            return lambda x: not(expr(x))
        else:
            first = __build_expression(expression['first'])
            second = __build_expression(expression['second'])
            return (lambda x: first(x) and second(x)) \
                    if expression['operator'] == 'and' \
                    else (lambda x: first(x) or second(x))
    else:
        return token(expression)

def __get_image_name(result):
    return __get_image_from_multiple(result['type'], result['values']) \
           if 'type' in result \
           else result

def __get_image_from_multiple(type, values):
    if type == 'random':
        return random.choice(values)
    else:
        index = __get_index_from_file()
        return values[index % len(values)]

def __get_index_from_file():
    name = 'data.iit'
    __check_file_existing(name)
    
    index = __read_index_from_file(name)
    __write_index_to_file(name, index + 1)

    return index

def __read_index_from_file(name):
    file = open(name, 'r')
    index = int(file.readline())
    file.close()
    return index

def __write_index_to_file(name, index):
    file = open(name, 'w')
    file.write(str(index % 100))
    file.close()
    return

def __check_file_existing(name):
    if not(os.path.exists(name)):
        __write_index_to_file(name, 0)
    return
import json
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
            return (lambda x: first(x) and second(x)) if expression['operator'] == 'and' else (lambda x: first(x) or second(x))
    else:
        return token(expression)

def __get_image_name(result):
    if ('type' in result):
        if result['type'] == 'random':
            return random.choice(result['values'])
        else:
            raise "Not implemented!"
    else:
        return result
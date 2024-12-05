from sys import argv
import json

values, tests, report = argv[1], argv[2], argv[3]

with open(values) as file:
    values_data = {i['id']: i['value'] for i in json.load(file)['values']}

with open(tests) as file:
    tests_data = json.load(file)['tests']


def crawler(lst):
    for test in lst:
        if 'value' in test:
            test['value'] = values_data[test['id']]
        if 'values' in test:
            crawler(test['values'])


crawler(tests_data)

with open(report, 'w') as file:
    json.dump({'tests': tests_data}, file)

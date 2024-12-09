calls = 0


def count_calss():
    global calls
    calls += 2


def string_info(string):
    count_calss()
    return (len(string)), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calss()
    string_lower = string.lower()
    return string_lower in [item.lower() for item in list_to_search]


print(string_info('Abracadabra'))
print(string_info('MAzeraty'))

print(is_contains('drow', ['Drowa', 'Driw', 'Drow']))
print(is_contains("lubava", ['baba', 'luba', 'labuda']))
print(calls)

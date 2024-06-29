calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    return a, b, c

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower() or i.lower() in string.lower():
            # уточнить, почему в строке выше ищем в i в нижнем регистре, а не в list_
            return True
        else:
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

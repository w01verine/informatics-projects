def print_message(message):
    if len(message) > 7:
        print('too long')
    else:
        print(message)

print_message('Hello!')
print_message('You look great!')

def compute(numbers):
    result = 0
    for num in numbers:
        result -= num + 2
    return result

values = [7, 6, 5]
computed_value = compute(values)
print(computed_value)
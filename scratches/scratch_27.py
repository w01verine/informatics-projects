def get_numbers():
    user_input = input()
    values = []
    for token in user_input.split():
        values.append(int(token))
    return values

def print_selected_numbers():
    numbers = get_numbers()
    for number in numbers:
        if (number % 3) != 0:
            print(number)

print_selected_numbers()
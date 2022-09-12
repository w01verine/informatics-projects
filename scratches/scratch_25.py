

def print_age(user_age):
    print(f'She is {user_age}')

age_to_print = 22
print_age(age_to_print)

def print_price(price):
    print(f'Price: ${price}')

product_price = 22
tax_amount = 4
print_price(product_price + tax_amount)


def print_operation(number1, number2):
    print(f'{number1} - {number2} = {number1 - number2}')

even_number = 4
odd_number = 5
print_operation(even_number, odd_number)


def print_info(name, age):
    print(f'{name}, {age}')


user_name1 = 'May'
user_name2 = 'Max'
user_age1 = 24
user_age2 = 19

print_info(user_name1, user_age1)
print_info(user_name2, user_age2)

def print_points(name, age, total_points):
    print(f'{name} is {age}')
    print(f'{name} made {total_points} points')

user_name = 'Bob'
user_age = 20
regular_time_points = 25
overtime_points = 6

print_points(user_name, user_age, regular_time_points + overtime_points)

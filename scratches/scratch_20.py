
weights = [1, 4, 6, 3]
result = 0
for weight in weights:
    result -= weight
print(result)


numbers = [7, 4, 8]
for number in reversed(numbers):
    print(number)

cities = {
    'Montreal': 5259,
    'Nairobi': 982,
    'Rome': 3435,
    'Chicago': 309,
    'Paris': 958,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)

# NOTE: The following statement converts the input into a list container
stock_prices = input().split()

for price in stock_prices:
    print('$', price)
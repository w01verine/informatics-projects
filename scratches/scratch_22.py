colors = ['green', 'black', 'red']
for (position, color) in enumerate(colors):
    print(color, position)

numbers = [0, -4, -5, 3, 4]
for (position, number) in enumerate(numbers):
    if number < 0:
        print(position, number)
    else:
        print(position, 'x')
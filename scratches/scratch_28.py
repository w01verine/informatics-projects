def show(a, b, c):
    print(f'{a}\{b}\{c}')

show(c=7, a=6, b=3)

def show_time(year, month, day, hour, minutes):
    print(f'{month}/{day}/{year} {hour}:{minutes}')

show_time(2020, 5, hour=15, day=14, minutes=17)

def show(a, b, c=12):
    print(f'{a}-{c}-{b}')

show(7, 3)
show(5, 6, c=8)

def show(a, b=1, c=3):
    print(f'{c}\{a}\{b}')

show(c=9, a=7)
show(b=4, a=5)
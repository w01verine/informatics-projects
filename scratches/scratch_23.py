# input num from the user.
num = int(input())

# run while loop until num greater than 0
while (num > 0):
    # when we divide any number by 2,
    # then remainder will be 0 or 1.
    # print remainder..
    print(num % 2, end='')

    # divide num by 2.
    num = num // 2
print()
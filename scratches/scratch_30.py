def print_message1():
    print('Message #1')


def print_message2():
    print('Message #2')


print_message1 = print_message2
print_message2 = print_message1
print_message1()
print_message2()
def swap_values(user_val1=None, user_val2=None, user_val3=None, user_val4=None):
    swap = user_val1
    user_val1 = user_val2
    user_val2 = swap
    swap_t = user_val3
    user_val3 = user_val4
    user_val4 = swap_t
    return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':

    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())

    user_val1, user_val2, user_val3, user_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)

    print(user_val1, user_val2, user_val3, user_val4)
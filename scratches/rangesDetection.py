user_grade = int(input())
if (user_grade >=9 and user_grade <= 12):
    print('in high school')
else:
    print('not in high school')




def detect_ranges(numbers):
    user_channel = int(input())

    if (user_channel >= 2) and (user_channel <= 499):
        channel_type = 's'

    elif (user_channel >= 1002) and (user_channel <= 1499):
        channel_type = 'h'

    else:
        channel_type = 'e'

    print('Channel type:', channel_type)

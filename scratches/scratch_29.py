def print_fever_check(temperature):
    NORMAL_TEMP = 98.6
    CUTOFF_TEMP = 95
    degrees_of_fever = 0
    if (temperature > NORMAL_TEMP):
        degrees_of_fever = temperature - NORMAL_TEMP
    print(f'You have {degrees_of_fever:f} degrees of fever.')
    elif (temperature < CUTOFF_TEMP):
        degrees_of_fever = CUTOFF_TEMP - temperature
    print(f'Your temperature is {degrees_of_fever:f} below 95.')


body_temperature = 96.0
print('Checking for fever...')
print_fever_check(body_temperature)
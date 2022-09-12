


def exact_change(user_total):
    num_Dollars = user_total // 100  # convert to Dollars
    user_total %= 100  # get remainder after conversion
    num_Quarters = user_total // 25  # convert to Quarters
    user_total %= 25  # get remainder after conversion
    num_Dimes = user_total // 10  # convert to Dimes
    user_total %= 10  # get remainder after conversion
    num_Nickels = user_total // 5  # convert to Nickels
    user_total %= 5  # get remainder after conversion
    num_Pennies = user_total
    return (num_Dollars, num_Quarters, num_Dimes, num_Nickels, num_Pennies)



input_val = int(input())  # prompt user to input an integer
num_Dollars, num_Quarters, num_Dimes, num_Nickels, num_Pennies = exact_change(
    input_val)  # recall exact_change function

    # define output statements to output number of exact_change variables:
    # num_Dollars, num_Quarters, num_Dimes, num_Nickels, num_Pennies
if input_val <= 0:  # if amount is zero
    print('No change')  # print output

else:
    if num_Dollars > 1:  # if number of Dollars is greater than one
        print('%d Dollars' % num_Dollars)  # print number of Dollars
    elif num_Dollars == 1:  # if number of Dollars equal 1
        print('%d Dollar' % num_Dollars)  # print Dollar in singular

    if num_Quarters > 1:  # if number of Quarters is greater than one
        print('%d Quarters' % num_Quarters)  # print number of Quarters
    elif num_Quarters == 1:  # if number of Quarters equal 1
        print('%d Quarter' % num_Quarters)  # print Quarter in singular

    if num_Dimes > 1:  # if number of Dimes is greater than one
        print('%d Dimes' % num_Dimes)  # print number of Dimes
    elif num_Dimes == 1:  # if number of Dimes equal 1
        print('%d Dime' % num_Dimes)  # print Dime in singular

    if num_Nickels > 1:  # if number of Nickels is greater than one
        print('%d Nickels' % num_Nickels)  # print number of Nickels
    elif num_Nickels == 1:  # if number of Nickels equal 1
        print('%d Nickel' % num_Nickels)  # print Nickel in singular

    if num_Pennies > 1:  # if number Pennies is greater than one
        print('%d Pennies' % num_Pennies)  # print number of Pennies
    elif num_Pennies == 1:  # if number of Pennies equal 1
        print('%d Penny' % num_Pennies)  # print Penny in singular
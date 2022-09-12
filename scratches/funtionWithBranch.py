# function print_popcorn_time
def print_popcorn_time(user_ounces):
  # if bag_ounces is less than 3
  if(user_ounces<3):
    # print too small
    print("Too small")
  # else is greater than 10
  elif(user_ounces>10):
    # print too large
    print("Too large")
  # else
  else:
      print(6 * user_ounces,"seconds")
user_ounces = int(input())
print_popcorn_time(user_ounces)
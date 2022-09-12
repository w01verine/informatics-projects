# Use the "in" operator
navitskas_family = ['Tommie', 'Christina' 'Camdon', 'Ryan', 'Layla', 'Preston', 'Fallon']

name = input('Enter name to check: ')
name = name.lower()

if name in navitskas_family:
    print('Found', name, 'in the family.')
else:
    print('Could not find', name, 'in the family.')

# Use the "not in" operator
navitskas_family = ['Tommie', 'Christina' 'Camdon', 'Ryan', 'Layla', 'Preston', 'Fallon']

name = input('Enter name to check: ')
name = name.lower()

if name not in navitskas_family:
    print('Could not find', name, 'in the family.')
else:
    print('Found', name, 'in the family.')



# Checking for membership in a dictionary

my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')


# Identity Operators

w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')
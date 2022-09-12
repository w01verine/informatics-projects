highway_number = int(input('Type Highway man: '))


if highway_number < 1 or highway_number > 999 or highway_number % 100 == 0:
  print (' {} is not a valid highway number'.format (highway_number))
  quit()

# Type + serving
if highway_number > 100:
  road_type = 'auxiliary'
  serving = str(highway_number % 100)
else:
  road_type = 'primary'
  serving = ''

# Direction
if highway_number % 2 == 0:
  going = 'east/west.'
else:
  going = 'north/south.'

#

# Create output
output = ['I-{}'.format(highway_number), 'is', road_type + ',']
if serving:
  output.extend(['serving', 'I-{},'.format(serving)])
output.extend(['going', going])
print(' '.join(output))

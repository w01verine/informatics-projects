par = int(input())
strokes = int(input())

if par == 3 or par == 4 or par == 5:
    if strokes - par <= -3:
        print('Albatross')
    elif strokes - par == -2:
        print("Eagle")
    elif strokes - par == -1:
        print("Birdie")
    elif strokes - par == 0:
        print("Par")
    elif strokes - par == 1:
        print("Bogey")
    else:
        print("Error")
else:
    print("Error")
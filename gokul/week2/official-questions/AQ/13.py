# Accept three non-negative real numbers as input from the user. If the three numbers form the sides of a triangle, print True . If not, print False.
x,y,z = int(input()),int(input()),int(input())

if x+y > z or y+z > x or z+x > y:
    print(True)
else:
    print(False)

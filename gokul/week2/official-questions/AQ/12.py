# Accept three integers as input from the user. Print good triplet if one of the three numbers is the sum of the other two, and bad triplet otherwise.
x , y , z = int(input()), int(input()), int(input())
if x+y == z or y+z == z or x+z == y:
    print("good triplet ")
else:
    print("bad triplet")
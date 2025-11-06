# Accept four distinct integers as input from the user. Print in ascending order if the four numbers have been entered in ascending order, and print not in ascending order otherwise.
a,b,c,d = int(input()),int(input()),int(input()),int(input())
if a < b < c < d :
    print(True)
else: 
    print(False)
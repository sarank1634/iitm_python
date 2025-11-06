# create a python code to sort the list using for loop


l = [9, 3, 7, 1, 6, 3, 4]
n = len(l)

for i in range(n):
    for j in range(0, n - i - 1):
        if l[j] > l[j + 1]:
        
            l[j], l[j + 1] = l[j + 1], l[j]

print("Sorted list:", l)

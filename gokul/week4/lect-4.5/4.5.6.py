# create a python code to sort the list using while loop

l = [9, 3, 7, 1, 6, 3, 4]

n = len(l)
i = 0

# Bubble sort using while loop
while i < n:
    j = 0
    while j < n - i - 1:
        if l[j] > l[j + 1]:
            # Swap elements
            l[j], l[j + 1] = l[j + 1], l[j]
        j += 1
    i += 1

print("Sorted list:", l)

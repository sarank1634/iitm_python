# create a python code that prints the sum of elements in a given list
l=[1,4,5,2,3]

total = 0
for num in l:
    total += num

print("Sum of elements: ", total)


total = sum(l)
print("Sum of elements:", total)
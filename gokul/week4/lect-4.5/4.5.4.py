## write a python code to print the minimum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]

min_element = l[0]

for num in l:
    if num < min_element:
        min_element = num  # update if a smaller number is found

print("Minimum element:", min_element)
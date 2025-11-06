## write a python code to print the maximum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]

max_element = l[0]

for num in l:
    if num > max_element:
        max_element = num

print("Maximum number: ", max_element)

# o/p:-
# 54
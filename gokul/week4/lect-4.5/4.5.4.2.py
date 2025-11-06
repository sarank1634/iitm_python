# what is the difference between the two codes

l=[1,4,2,6,3]
for i in l:
    print(i)

#i takes the value of each element in the list directly.

# Prints each element one by one.


for i in range(len(l)):
    print(l[i])

# i takes the index values from 0 to len(l)-1.

# l[i] accesses the element at that index.
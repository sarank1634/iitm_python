## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
## findout the index of number 21 in the generated list, if the number is not present in the list print -1

import random


numbers = [random.randint(1, 1000) for _ in range(1000)]
print(numbers)

numbers.sort()
print("*************")
print(numbers)


try:
    index_21 = numbers.index(21)
    print("Index of 21:", index_21)
except ValueError:
    print(-1)  

# # o/p:-
# Index of 21: 18
## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list

import random

numbers = [random.randint(1, 1000) for _ in range(100)]

numbers.sort()

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print("Sorted numbers:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)
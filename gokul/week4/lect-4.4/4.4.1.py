## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list

import random

numbers = [random.randint(1, 1000) for _ in range(1000)]

numbers.sort()

print("Smallest:", numbers[0])
print("Second smallest:", numbers[1])
print("Largest:", numbers[-1])
print("Second largest:", numbers[-2])

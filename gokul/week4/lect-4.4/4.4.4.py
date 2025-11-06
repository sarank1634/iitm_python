## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list

import random

numbers = [random.randint(1,5) for _ in range(15)]

numbers.sort()

missing_numbers = [i for i in range(1, 16) if i not in numbers]

print("Missing numbers:", missing_numbers)
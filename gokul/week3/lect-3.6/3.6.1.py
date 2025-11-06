# take a number as input and find the sum of numbers from 1 to that number

n= int(input("enter a number: "))

sum_total = 0
num = 1

while num <= n:
    sum_total += num
    num += 1

print(f"the sum of nummbers from 1 to {n} is {sum_total}")
# Write a code using a while loop that adds all odd numbers from 1 to 100 (inclusive).

num = 1
sum_odd = 0

while num <= 100:
    if num%2 != 0:
        sum_odd += num
    num += 1

print(f"the sum of all odd numbers from 1 to 100 is {sum_odd}")
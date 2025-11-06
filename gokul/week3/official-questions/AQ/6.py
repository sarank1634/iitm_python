# Write a program to accept the two positive integers start and stop where 0< start<stop<=100 print all

# numbers from start to stop both inclusive with following constraints.

# If the number is divisible by 3 print Divisible by 3 at the place of number.

# If the number is divisible by 5 print Divisible by 5 at the place of number.

# If the number is divisible by 10 print Divisible by 10 at the place of number.

# If the number is divisible by any of two from 3 ,5 and 10 , print nothing, just skip.

# If the number is divisible by all ( 3 , 5 and 10) , stop printing the number.

# If the number is not divisible by any of ( 3 , 5 and 10) , just print the number as it is.

start = int(input("Enter start (0 < start < stop <= 100): "))
stop = int(input("Enter stop (start < stop <= 100): "))

for num in range(start, stop+1):
    if num % 3 == 0 and num % 5 == 0 and num % 10 == 0:
        break 
    
    divisible_count = sum([num % 3 == 0, num % 5 == 0, num % 10 == 0])
    
    if divisible_count > 1:
        continue 

    if num % 3 == 0:
        print("Divisible by 3")
    elif num % 5 == 0:
        print("Divisible by 5")
    elif num % 10 == 0:
        print("Divisible by 10")
    else:
        print(num) 

#   o/p:
# Enter start (0 < start < stop <= 100): 50
# Enter stop (start < stop <= 100): 70
# Divisible by 3
# 52
# 53
# Divisible by 3
# Divisible by 5
# 56
# Divisible by 3
# 58
# 59

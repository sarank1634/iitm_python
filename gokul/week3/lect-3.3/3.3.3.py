# find the factorial of a number using while loop, take number n as input

n = int(input("enter a number: 10"))

#initiailze
factorial = 1
num = n

#calculate factorial using while loop 
while num > 0:
    factorial *= num
    num -= 1

#print
print(f"the factorial of {n} is {factorial}")
    
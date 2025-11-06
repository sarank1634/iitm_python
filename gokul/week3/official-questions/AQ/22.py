# Write a program to find the highest common factor (HCF) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y != 0:
    x, y = y, x % y

print(f"The HCF of {a} and {b} is {x}")


# o/p:-
# Enter first number: 36
# Enter second number: 60
# The HCF of 36 and 60 is 12

# Enter first number: 17
# Enter second number: 23
# The HCF of 17 and 23 is 1

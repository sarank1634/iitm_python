# Write a program to print the first and last digits of a number without converting it to string.
 
num = int(input("enter a postive number: "))

last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10  

print("First digit:", first_digit)
print("Last digit:", last_digit)
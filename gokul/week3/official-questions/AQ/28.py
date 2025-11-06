# Two numbers n1 and n2 are said to be the same if they have an equal number of digits in them. Write a program to check whether n1 and n2 are the same. n1 and n2 are positive integers entered by the user without converting the number to string.

n1 = int(input("Enter first positive integer: "))
n2 = int(input("Enter second positive integer: "))


def count_digits(n):
    count = 0
    while n > 0:
        n //= 10 
        count += 1
    return count


if count_digits(n1) == count_digits(n2):
    print("n1 and n2 have the same number of digits")
else:
    print("n1 and n2 do NOT have the same number of digits")


# o/p:-

# Enter first positive integer: 123
# Enter second positive integer: 456
# Output: n1 and n2 have the same number of digits



# Enter first positive integer: 12
# Enter second positive integer: 345
# Output: n1 and n2 do NOT have the same number of digits

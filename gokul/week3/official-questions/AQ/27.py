# Write a program to print the Fibonacci series of n terms where n is always greater than or equal to 2.

n = int(input("Enter the number of terms (n >= 2): "))
a, b = 0, 1
print("Fibonacci series:")
print(a, b, end=' ')
for _ in range(2, n):
    c = a + b
    print(c, end=' ')
    a, b = b, c

# o/p:-
# Enter the number of terms (n >= 2): 7
# Fibonacci series:
# 0 1 1 2 3 5 8

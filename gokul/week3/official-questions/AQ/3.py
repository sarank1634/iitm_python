# Write a program to accept the positive integer n from the user and print the average of all number's factorial

# from 1 to n .

n = int(input("enter a positive integer:"))

sum_fact = 0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum_fact += fact

average = sum_fact / n

print(f"the avarage of factorial from 1 t0  {n} is {average}")


# Program Purpose:

# Accept a positive integer n from the user.

# Calculate the factorial of all numbers from 1 to n.

# Compute the average of these factorials.

# Step 1: Input
# n = int(input("enter a positive integer:"))


# Takes user input and converts it to an integer.

# Example: if the user enters 4, then n = 4.

# Step 2: Initialize sum
# sum_fact = 0


# sum_fact will store the sum of all factorials from 1 to n.

# Step 3: Loop through numbers 1 to n
# for i in range(1, n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact *= j
#     sum_fact += fact


# Breakdown:

# Outer loop: i goes from 1 to n.

# For example, if n=4, i = 1, 2, 3, 4.

# fact = 1 → initialize factorial for current number i.

# Inner loop:

# for j in range(1, i+1):
#     fact *= j


# Calculates factorial of i by multiplying all numbers from 1 to i.

# Example: i=3 → factorial = 1*2*3 = 6.

# sum_fact += fact → add the factorial of i to the running total.

# Step 4: Calculate average
# average = sum_fact / n


# Divides the sum of all factorials by n to get the average.

# Example: if n=4

# Factorials: 1! = 1, 2! = 2, 3! = 6, 4! = 24

# Sum = 1 + 2 + 6 + 24 = 33

# Average = 33 / 4 = 8.25

# Step 5: Print result
# print(f"the avarage of factorial from 1 t0  {n} is {average}")


# f"..." → f-string lets Python replace {n} and {average} with actual values.

# Corrected typos: “avarage” → “average”, “t0” → “to” for readability.

# Output example:

# Enter a positive integer: 4
# The average of factorials from 1 to 4 is 8.25


# 💡 Key concepts used:

# Nested loops → outer loop for numbers, inner loop for factorial calculation.

# Factorial calculation using multiplication.

# Accumulating sum and computing average.

# f-strings for formatted output.

# If you want, I can also show a shorter version using Python’s math.factorial() that avoids the inner loop entirely.

# Do you want me to show that?

# ChatGPT can make mistakes. Check important info. See Cookie Preferences.

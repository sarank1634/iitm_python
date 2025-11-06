# A three digit number is called a sandwich number if the difference between its first and last digit is equal to its middle digit.
#  Accept a three digit number as input and print sandwich if the number is a sandwich number. Print plain if the number is not a sandwich number. 
# For example, 123 and 853 are sandwich numbers.

a = int(input())
b = int(input())
c = int(input())
m = a-c
print(m)
if m == b :
    print("is a sandwich number") 
else:
    print("is not a sanwich number")

# o/p:-
# 1
# 2
# 3
# -2
# is not a sanwich number

# o/p:-
# 8
# 5
# 3
# 5
# is a sandwich numer

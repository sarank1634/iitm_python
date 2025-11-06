# Write a code to accept a string as input and determine if it is a palindrome or not.

s = input("Enter a string: ")

is_palindrome = True  

for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")


# o/p:-
# Enter a string: sarava
# 'sarava' is not a palindrome
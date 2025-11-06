# Accept a word as input. Assume that all characters in the word are in lower case.
#  Print True if the first and last letter of the word are the same, and False otherwise. 
# You should be able to do this using the concepts introduced in this week.

# Conditional statements can be used. They will be introduced in the next week. But the challenge is to solve this problem without using conditional statements! As an interesting exercise, can you list down some words that follow this pattern?

# n = input()
# m = n.lower()
# print(n[0] == n[-1])

# o/p:- 
# gokul
# False

#use if statement
# word = input()
# if word[0] == word[-1]:
#     print(True)
# else: 
#     print(False)

#terrinory oprator
word = input()
print(True if word[0] == word[-1] else False)
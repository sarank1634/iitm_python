# Write a code to accept a string as input and reverse it using loop:

s = input("enter a string: ")
reversed_str = ""

for i in range(len(s)-1, -1, -1):
    reversed_str += s[i]

print("Reversed string:", reversed_str)
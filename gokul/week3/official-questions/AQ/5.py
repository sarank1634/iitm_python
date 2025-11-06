# Write a program to accept the string s from the user and print all alphabets in one line separated by , before

# first occurrence of vowels .

s = input("enter a string: ")

vowels = "aeiouAEIOU"  # list of vowels
result = []

for char in s:
    if char in vowels:  # stop at first vowel
        break
    if char.isalpha():  # only consider alphabets
        result.append(char)

print(",".join(result))  # print letters separated by commas

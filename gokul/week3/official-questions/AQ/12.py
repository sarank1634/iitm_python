# Write a code to accept the string of length 10 from the user and print True if string has any character

# occurring 5 times consecutively in it, otherwise print False.

s = input("enter a string of length 10: ")

if len(s) != 10:
    print("string must be of length 10")
else:
    found = False
    for i in range(len(s) - 4):  # last possible start index is 5
        # check if current character repeats 5 times consecutively
        if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
            found = True
            break
    print(found)
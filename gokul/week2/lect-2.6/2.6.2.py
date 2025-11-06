x=input()

# print true if all characters are lower case
# print True if all the characters are upper case
# print True if the string follows the rules of title (all the words have starting letter in capital)

#lowercase
# if x == x.lower()  : 
#     print(x)
# else:
#     print(False)

# #uppercase
# if x == x.upper() :
#     print(x)
# else:
#     print(False)
# print(True if x == x.upper() else False )

# #capitalize
# if x == x.capitalize() :
#     print(x)
# else: 
#     print(False)

print(x == x.lower())
print(x==x.upper())
print(x.istitle())
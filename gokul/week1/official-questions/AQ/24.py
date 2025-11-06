# Accept a two digit number as input and print the sum of its digits. What about a three digit number?
# x = input()
# y=int(x[0])
# z=int(x[1])
# print(y+z)

x=int(input())
# y = x // 100  
# f = (x // 10)%10 
# z = (x % 10)  
# print(y+f+z)


y = x // 1000 
f = (x // 100)%10 
z = (x // 10)%10
m = (x % 10)
print(y+f+z+m)


# Accept a positive integer as input and print True if it is a perfect square and False otherwise. 
# For example, if the input is 25 , then you must print True . If the input is 15 , then you must print False

x=input() 
x=int(x)
x=x %(x**(1/2))
print(x==0)
 

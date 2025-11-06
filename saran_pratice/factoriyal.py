def calculate_fact(n):
    if n < 0:
        print("factorial numer not as a negative number")
    elif n == 0:
        return 1
    else:
        factorial =1 
        for i in range(1,n+1):
             factorial *= i
        return factorial   

number = 5
result = calculate_fact(number)
print(f"the factorial {number} is {result}")



def fact_recurssion(n):
    if n < 0:
        print("factorial not contain a negative number")
    elif n == 0:
        return 1
    else:
        return n * fact_recurssion(n-1)# 5*4*3*2*1

# f_!=1*facr(0)
# f_2=2*1*1

number = 5
ans = fact_recurssion(number)
print(f"the {number} factorial recurssion is {ans} ")
         

factorial = lambda m : m * factorial(m-1) if m > 0 else 1 
print(factorial(5))
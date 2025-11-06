# print(int(input()))

# predict the output for the below inputs

# INPUT 1 : -121
# INPUT 2 : abc
# INPUT 3 : 20.5


n=-123456
m=abs(n)
print(str(m)==str(m)[::-1])

# o/p:-
# false

# abs(n) → gives the absolute value (ignores negative sign)

# Here abs(-123456) → 123456

# str(m) → converts the number to a string

# '123456'

# str(m)[::-1] → reverses the string

# '654321'

# str(m) == str(m)[::-1] → checks if the number reads the same forwards and backwards

# '123456' == '654321' → False
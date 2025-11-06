# The following string is encoded using the Caesar cipher with a shift of 5: udymts . Decode the string!
alpha = 'abcdefghijklmnopqrstuvwxyz'
k=5 
n =''
m = 'udymts'
n = n+(alpha[(((alpha.index(m[0]))-k)%26)] )
n = n+(alpha[(((alpha.index(m[1]))-k)%26)] )
n = n+(alpha[(((alpha.index(m[2]))-k)%26)] )
n = n+(alpha[(((alpha.index(m[3]))-k)%26)] )
n = n+(alpha[(((alpha.index(m[4]))-k)%26)] )
n = n+(alpha[(((alpha.index(m[5]))-k)%26)] )

print(n)
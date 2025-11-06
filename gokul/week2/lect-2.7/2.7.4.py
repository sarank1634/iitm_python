
# write a python script for the below test case,
# Note the input will be of 5 characters long,
  
#shift the characters by 1

# testcase 1
# '''
# INPUT : 'gokul'
# OUTPUT : 'hplvm'
# '''

#this is popularly called the Caser cipher in cryptography
from cgitb import text
from re import A
from traceback import print_tb
from unittest import result

alpha = 'abcdefghijklmnopqrstuvwxyz'
t = 'gokul'
u = ''
k=1
u=u+(alpha[(((alpha.index(t[0]))+k)%26)] )
u=u+(alpha[(((alpha.index(t[1]))+k)%26)] )
u=u+(alpha[(((alpha.index(t[2]))+k)%26)] )
u=u+(alpha[(((alpha.index(t[3]))+k)%26)] )
u=u+(alpha[(((alpha.index(t[4]))+k)%26)] )
print(u)

# testcase 2
# '''
# INPUT: 'abcde'
# OUTPUT: 'bcdef'
# '''
m = 'abcde'
n = ''
n=n+(alpha[(((alpha.index(m[0]))+k)%26)] )
n=n+(alpha[(((alpha.index(m[1]))+k)%26)] )
n=n+(alpha[(((alpha.index(m[2]))+k)%26)] )
n=n+(alpha[(((alpha.index(m[3]))+k)%26)] )
n=n+(alpha[(((alpha.index(m[4]))+k)%26)] )
print(n)
# solution:

alpha = 'abcdefghijklmnopqrstuvwxyz'
k = 1

def caesar_cipher(text, k):
    result = ''
    for ch in text:
        idx = alpha.index(ch)         # find position
        new_idx = (idx + k) % 26      # shift and wrap around
        result += alpha[new_idx]      # pick shifted char
    return result

# Test cases
print(caesar_cipher('gokul', 1))  # hplvm
print(caesar_cipher('abcde', 1))  # bcdef

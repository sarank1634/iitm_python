# write a python code where you will take an input number k and a string s.
# you have to move the string by k characters to the right

# TestCase 1
'''
INPUT:
    s='abcdefg'
    k=2

OUTPUT: 'cdefghi`
'''
alpha = 'abcdefghijklmnopqustuvwxyz'
t = ''
s='abcdefg'
k=2
t = t+(alpha[((alpha.index(s[0])+k)%26)])
t = t+(alpha[((alpha.index(s[1])+k)%26)])
t = t+(alpha[((alpha.index(s[2])+k)%26)])
t = t+(alpha[((alpha.index(s[3])+k)%26)])
t = t+(alpha[((alpha.index(s[4])+k)%26)])
t = t+(alpha[((alpha.index(s[5])+k)%26)])
t = t+(alpha[((alpha.index(s[6])+k)%26)])
print(t)

# TestCase 2
'''
INPUT:
    s='chennai'
    k=20
OUTPUT:
    'wbyhhuc'
'''
y=''
s = 'chennai'
k=20
y = y+(alpha[((alpha.index(s[0])+k)%26)])
y = y+(alpha[((alpha.index(s[1])+k)%26)])
y = y+(alpha[((alpha.index(s[2])+k)%26)])
y = y+(alpha[((alpha.index(s[3])+k)%26)])
y = y+(alpha[((alpha.index(s[4])+k)%26)])
y = y+(alpha[((alpha.index(s[5])+k)%26)])
y = y+(alpha[((alpha.index(s[6])+k)%26)])

print(y)
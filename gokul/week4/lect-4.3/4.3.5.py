# predict the output

l=[1,[2,3],[[4,5],[6,7],[[8,9],10,11],[12]],13]

print(len(l)) 
# print(len(l[0]))
print(len(l[1]))
print(len(l[2]))
print(len(l[2][2]))
print(len[l[-1]])
print(len[l[-2]])

# o/p:-
# 4
# 2
# 4
# 3
# Traceback (most recent call last):
#   File "/home/gojo/Desktop/python-questions/gokul/week4/lect-4.3/4.3.5.py", line 10, in <module>
#     print(len[l[-1]])
# TypeError: 'builtin_function_or_method' object is not subscriptable
# gojo@smart-saru:~/Desktop/python-questions$

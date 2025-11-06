# predict the output

l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)   #o/p:- [1, 2, 3]
x=[]
print(len(x)) #o/p:- 0
x.append(l)
print(x)  #o/p:-[1, 2, 3]
print(len(x),"len(x)")  #o/p:- 3 len(x)
print(len(x[0]),"len(x[0])") #2 len(x[0])
m=[4,5,6]
x.append(m) 
print(x) #o/p:- [[1 2 3, 4, 5, 6]]
t=[]
t.append(x) 
t.append([100,200,300]) 
print(t) #o/p:- [[[1 2 3 4, 5, 6]], [100, 200, 300]]
print(t[0]) #o/p [[1, 2, 3], [4, 5, 6]]
print(t[1]) #o/p:- [100, 200, 300]
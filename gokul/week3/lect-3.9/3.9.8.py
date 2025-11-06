# what will be the output of the below code?
for i in range(5):
    print(i, end=' ')

#o/p: 0,1,2,3,4
for i in range(5):
    print(i, a=' ')
    
#typeError : print() got an unexpected keyboard argument 'a'
for i in range(5):
    print(i, end=3)


#correct version is 
for i in range(5):
    print(i, end='3')  # convert number to string implicitly

#end must be a string, but you gave an integer (3).
# what will be the output of the below code?

'''
for i in range(1,11,2):
    print(i)
print('-------------------')
for i in range(1,11,3):
    print(i)
print('-------------------')
for i in range(9,-1,-1):
    print(i)
print('-------------------')
for i in range(9,-1,-2):
    print(i)
print('-------------------')


'''

for i in range(1,11,2):
    print(i)
print('-------------------')
for i in range(1,11,3):
    print(i)
print('-------------------')
for i in range(9,-1,-1):
    print(i)
print('-------------------')
for i in range(9,-1,-2):
    print(i)
print('-------------------')

# explan:-
# range(1, 11, 3) → starts at 1, stops before 11, step is 3

# So Python generates numbers like this:

# Start at 1 → print 1

# Add step 3 → 1 + 3 = 4 → print 4

# Add step 3 → 4 + 3 = 7 → print 7

# Add step 3 → 7 + 3 = 10 → print 10

# Add step 3 → 10 + 3 = 13 → 13 ≥ 11, stop


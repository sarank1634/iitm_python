# write a code to print the below output , 
# using nested for loops
input="abcd"
'''
0 0 a a
0 1 a b
0 2 a c
0 3 a d
1 0 b a
1 1 b b
1 2 b c
1 3 b d
2 0 c a
2 1 c b
2 2 c c
2 3 c d
3 0 d a
3 1 d b
3 2 d c
3 3 d d
'''
test = "abcd"

for i in range(len(test)):
    for j in range(len(test)):
        print(f"{i} {test[i]} {test[j]}")


# Outer loop (i) goes from 0 to len(input_str)-1 → selects the first character.

# Inner loop (j) goes from 0 to len(input_str)-1 → selects the second character.

# f"{i} {j} {input_str[i]} {input_str[j]}" prints indices and corresponding characters.
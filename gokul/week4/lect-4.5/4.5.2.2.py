# predict the output
l=[1,5,2,9,3,6]
l=l.sort()
print(l)

#noneStep 2: Why l = l.sort() is wrong
# l.sort() sorts l, but returns None.

# When you do l = l.sort(), you overwrite your list l with None.

# So now l is not a list anymore, it is None.


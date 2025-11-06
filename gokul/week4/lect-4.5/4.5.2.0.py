l=[1,44,22,11,23,36,49,28,31,8,54]
print(l.sort())
print(l)


# Try to understand why the first print is giving `None` and the second print is giving the `sorted list``

# l.sort() sorts the list in-place.

# It does not return a new list, so the return value of l.sort() is None.

# That’s why print(l.sort()) prints None.
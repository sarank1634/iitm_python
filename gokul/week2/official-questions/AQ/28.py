# What is the difference between the string methods find and index ?

s = "hello world"

# Finds the position of the substring "world"
print(s.find("world"))

# Returns -1 when substring is not found
print(s.find("python"))

# Finds the position of "o" starting from index 5
print(s.find("o", 5))

s = "hello world"

# Finds position of the substring "world"
print(s.index("world"))

# Raises a ValueError when substring is not found
print(s.index("python"))

# Finds position of "o" starting from index 5
print(s.index("o", 5))
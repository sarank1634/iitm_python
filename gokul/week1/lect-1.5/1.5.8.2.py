# Note the different types of formatting, try running this.

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

# 1.the first one is named argument.
# 2. postional argument with indices.
# 3. implicit Positional Arguments.

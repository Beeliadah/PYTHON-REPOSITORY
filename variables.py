# A variable is a container for a values, which can be o various types

'''
This is a
multiline comment
or doctstring (used to define a function purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  -variable names are case sensitive (name and NAME are different variables)
  -must start with a letter or an underscore
  -can have numbers but can not start with one
"""

# x = 1           # int
# y = 2.5         # float
# name = 'john'   # str
# is_cool = bool  # bool

# multiple assignment
x, y, name, is_cool = (1, 2.5, 'john', True)

# Basic math
a = x + y

# casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)

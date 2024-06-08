# strings in python are surrounded by either single or double quoatation marks. let's looks at string formatting and some string methods

name = 'brad'
age = '37'

# concatenate
# print ('Hello, my name is ' + name + ' and I am ' + str(age))

# string formating

# Arguments by position
# print('my name is {name} and I am {age}'.format(name=name, age=age))

# F-strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# string methods

s = 'hello world'

# capitalize string
print(s.capitalize())

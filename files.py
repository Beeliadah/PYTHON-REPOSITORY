# python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'W')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.Write('I love python')
myFile.Write('and Javascript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.Write('I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
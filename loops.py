# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Susan']

# Simple for loop
# for person in people:
#   print(f'current person: {person}')

# Break
# for person in people:
#    if person == 'sara':
#       break
#   print(f'current person: {person}')
   
# continue
# for person in people:
#    if person == 'sara':
#       continue
#   print(f'current person: {person}')

# Range
# for i in range(len(people)):
#  print(people[i])

# For i in range(0, 11):
#    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'count: {count}')
    count += 1
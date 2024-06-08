# A Turple is a collection which is ordered and unchangeable. A llows duplicate members.

# create tuple
fruits = ('Apples', 'oranges', 'Grapes')
# fruits2 = tupple(('Apples', 'oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
fruits[0] = 'pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A st is collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
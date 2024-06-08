# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate Members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use comstrructor 
# Person2 = dict(first_name='sara', last_name='williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'martha', 'age': 30},
    {'name': 'kevin', 'age': 25},
]

print(people[1]['name'])

# A class is like a blueprint for creating objects. An object has properties and methods (function) associated with it. Almost everything in python is am object

# Create class
class user:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

def greeting(self):
    return f'my name is {self.name} and I am {self.age}'

def has_birthday(self):
    self,age += 1


# Extend class
class customer(user):
  # constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
    
def set_balance(self, balance):
  self.balance = balance

def greeting(self):
    return f'my name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user object
beeliadah = user('Beeliadah Lokwang', 'beeliadahlokwang@gmail.com', 25)
# Init customer object
mary = customer('Mary Kavochi', 'marykavochi@gmail.com', 24)

mary.set_balance(500)

beeliadah.has_birthday
print(beeliadah.greeting())
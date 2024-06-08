# A function is a block of a code which only runs when it is called.In python, we do not use curly brackets, we use identation with tabs or spaces


# Create function
def sayHello(name='sam'):
    print(f'Hello {name}')


    # Return values
    def getsum(num1, num2):
      total = num1 + num2
      return total 
    

    # A lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, but can only have one expression. very similar to JS arrow functions

    getSum = lambda num1, num2: num1 + num2



    print(getsum(10, 3))
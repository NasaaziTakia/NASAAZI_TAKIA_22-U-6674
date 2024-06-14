#Defining functions
# function syntax and parameters
#return values
# lambda function
# Functions in python are defined using a def keyword, followed by a function name
# parenthesis(), inside a parenthesis, you put a parameter name and a colon
# example
def multiply(a,b):
    return a*b
result=multiply(5,10)
print(result)

# Exercise
def greet(name="takia"):
    print(f"I am a software engineer {name}")

greet()

# Return multiple values
def get_name_and_position():
    name = 'Nasaazi Takia'
    position = 'software student'
    return name, position

get_name_and_position()

# Exercise 4
def get_name_and_age():
    name = "Nasaazi Takia"
    age = 24
    return name, age

get_name_and_age()

"""Summary:
    - def keyword is used to define a function.
    - Function name follows the def keyword.
    - Parameters can be defined within the parentheses.
    - Return statement is optional; it returns a value from the function.
    - Docstring is a string literal used for documentation.
"""

# Syntax for defining a function with a docstring
def function_name():
    """Docstring goes here."""
    # Functional code goes here
    # Return value if needed

# Lambda functions are small anonymous functions.
# They are created using the lambda keyword.

# Example: Lambda function to add two numbers
add = lambda a, b: a + b
print(add(45, 25))

# Example 5:
cordinates = [(1, 5), (3, 2), (7, 8), (2, 4)]
cordinates.sort(key=lambda coordinates: coordinates[1])
print(cordinates)

# map, Filter
# Example 6:
numbers = [1, 2, 3, 4, 5]
number_squares = map(lambda x: x**2, numbers)
squares = list(number_squares)
print(squares)

# Exercise 4: def
# Define a lambda function to create user info
get_user_info = lambda name, age, city, profession: {"name": name, "age": age, "city": city, "profession": profession}
user_info = get_user_info(name="John", age=30, city="New York", profession="Engineer")
users = [user_info]
print(users)

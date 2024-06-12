# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""summary
    
    Dictionaries in python are collections of keys and values
    -Unordered
    -mutable and
    -indexed by keys
    
    """
    
    # Example 1: Create a dictionary
    # Create a dictionary for a student pursuing software engineering
    # the key must be your name, age, technology interest and year of study. put
    # your own details
    
student_dict = {
        'name' : 'Nasaazi Takia',
        'age' : '30',
        'technology': 'AI and ML',
        'course': 'BSE',
        'Year': 'Year3'
    }
    
print(student_dict['name'])

# Access values

# Modify Values:

# Exercise 1: Modify age and technology

student_dict['age'] = '22'
student_dict['technology'] = 'data science'

print(student_dict['age'])  
print(student_dict['technology'])

# # Example2: adding keys and values
# student_dict['email'] = 'efrataaron5@gmail.com'

# print(student_dict)

# Exercise 2: Remove a key and value from student dictionary

del student_dict['age']
print(student_dict)

# Common Dictionary methods
"""summary
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""
# Example 3: Use the get method to get the value

print(student_dict.get('technology'))

# Exercise 3: Use the update method to change value in age 

student_dict.update({'age': '25'})
print(student_dict)
print()

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary

if 'age' in student_dict:
    print(" age is present in the dictionary.", student_dict['age'])
    
else:
    print(" age is not present in the dictionary.")
    
print()

# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""summary

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
 
 # Exercise : Use the update method to change the course and add a new 
 # key "WhatsApp_Number" to the dictionary
 
student_dict.update({
    'course': 'BSC',
    'WhatsApp_Number': '0742127071'
})
print(student_dict)
print()
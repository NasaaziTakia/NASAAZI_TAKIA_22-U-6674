"""summary
Name of of the oprator      symbol with example
Addition                     x+y
subtraction                  x-y
multiplication               x*y
Division                     x/y
Modulus                      x%y
Exponential                  x**y
Floor division               x//y

#example of comparision operators

Name of of the oprator     symbol with example
equal                       x==y
notEqual                    x!=y
greater than                x>y
less than                   x<y

#Example of python Logical operators

Name of the operator       symbol with example
and                         and  
or                          or   
not                          not ~

#Example of membership opearators

Name of the operator      symbol with example
in                         x in y
not in                     x not in y

#Example of bitwise opearators

Name of the operator    symbol with example
AND                     &
OR                      |
XOR                     ^
NOT                     ~

#python cases
1.snake_case
2.camelcase
3.pascalcase
4.UPPERCASE
5.kebab-case
 """
#comprehension(list,dictionary,compressions)
#comprehension provides a concise way to write lists and dictionaries
"""summary
what is the symbol for
lists            [] square brackets #used to store multiple items in a single variable
dictionaries      {} curly brackets  #used to store data value in key:value pais
"""
#Example1:Basic list comprehension
#create a list of squares in range of ten
list_of_squares=[x**2 for x in range(10)]
print(list_of_squares)
# Exercise1:
list_of_even= [x**2 for x in range(20) if x%2==0]
print(list_of_even)

#Example2:Dictionary comprehension
#create a dictionary comprehensio for favourites cars and count the length of the characters
favorite_car=["BMW","Jeep","Mercedes","fordrator","RangeRover"]
car_length={
    car:len(car) for car in favorite_car
}
print(car_length)
#Exercise2:create a list of tuples where each tuple contain a number  and its cube between a and 10 using
tuple=(range(1,11))
cube={x:x**3  for x in tuple
}
print(cube)
#end
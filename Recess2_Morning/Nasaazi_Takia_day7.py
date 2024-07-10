# #Inheritace and polymorphism
"""Summary
Inheritance and method overridding
polymorphism and method resolution order
 Abstract classes and interfaces 
 """
# #Inheritance and method overriding
""" Summary_line
 --description
 Iheritance and method overriding allows a class (child class) to inherit attributes and methods fron another class(parent class)

 key concepts;
 Base class(parent class);class whose properties are inheritted by another
 Derived class(child class)
 """

# #Example 1: create a class where a dog inherits from animal and overrides with speak method
class Animal:
    def speak(self):
        return "makes sound"
class Dog(Animal):
    def speak(self):
        return "barks"
# Implementation of inheritance
animal=Animal()
dog=Dog()
print(animal.speak())
print(dog.speak())

# #polymophism and method resolution
# #polymophism allows objects of different classess to be treated as object of a common superclass
# #Method resolution order(MRO); is order in which python looks for a method in a  hiereracy classes

# #Example 2:How polymophism works in python

class Animal:
    def speak():
        return "makes sound"
class Dog(Animal):
    def speak():
        return "barks"
class cat(Animal):
    def speak():
        return "mwoow mwoow"
def make_animal_speak(animal):
    print(animal.speak())
    make_animal_speak(Dog())

#Exercise 1: create a simple aplication to manage du=ifferent tppes of vehicles.Implement
#derived class to demostrate inheritance and polymophism

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle was made by {self.make} and its model is {self.model} made in year {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"It is a car with {self.number_of_doors} doors")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"It is a motorcycle of type {self.type_of_bike}")


Vehicle_obj=Vehicle("TOYOTA","harrier", 1996)
Vehicle_obj.display_info()


car_obj = Car("Toyota", "Camry", 2022, 4)
car_obj.display_info()

motorcycle_obj = Motorcycle("Honda", "CBR1000RR", 2021, "Sport")
motorcycle_obj.display_info()

#Reading and writing files in python
""" 
"""
#1.Working with text files,open,read,write and close
#Note:python provides inbult functions to handle text files.
#key concepts
""" description
Opening File:open()
Reading File:read()
Writting File:write()
Closing File:close()
"""
#Example 3: write a file and read a file
with open('tasha.txt',"w")as file:
    file.write(' I am tahia tasha and i love data analysis')
    file.write(' I use python to analyse data')

#Reading from a text file
with open('tasha.txt','r') as file:
    content=file.read()
    print(content)
#Handling CSV files
""" CSV(comma Separated Values)
read and do not write to the file

key concepts:
Read csv files;Using"csv.reader()"
writing csv files:Using "csv.writer"
DictReader and DictWriter:The class read and write csv files as dictionaries
"""

#Example 4:writing and reading csv file
import csv

# Writing to a CSV file
with open('tasha.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position', 'course'])  # Header row as a list
    writer.writerow(['tahia', 'student', 'python'])  # Data rows as lists
    writer.writerow(['tasha', 'student', 'ICT'])
    writer.writerow(['mercy', 'supervisor', 'BSSE'])

# Reading from a CSV file
with open('tasha.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)


#JSON and XML file processing
"""summary
JSON(Javascript Object Notation)
XML(eXtensible Markup Language)
used structure data.

key concepts;
loading dataa:osing json.load() to read JSON file
Dumpling JSON Data: Using json.dump()
Parsing JSON Data:using json.loads() for handling JSON strings
"""
#Example 4:
import json

# Writing to a JSON file
student_data = {
    'name': 'tahia',
    'course': 'BSSE',
    'year': 'year 2'
}

with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)  # Corrected to use json.dump()

# Reading the JSON
with open('student_data.json', 'r') as json_file:
    student_data = json.load(json_file)  # Correctly using json.load() to read JSON data
    print(student_data)

    #Exercise3: Using abstraction calculate the area and perimeter of the rectangle
# Define a Rectangle class
# Define a Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define a method to calculate the area
    def area(self):
        return self.width * self.height

    # Define a method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create a Rectangle object
rect = Rectangle(5, 3)

# Calculate and print the area and perimeter
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


import xml.etree.ElementTree as ET

def write_xml(file_name):
    # Create the root element
    root = ET.Element("vehicles")

    # Create a sub-element
    car = ET.SubElement(root, "car")
    ET.SubElement(car, "make").text = "Toyota"
    ET.SubElement(car, "model").text = "Corolla"
    ET.SubElement(car, "year").text = "2020"

    bike = ET.SubElement(root, "bike")
    ET.SubElement(bike, "make").text = "Yamaha"
    ET.SubElement(bike, "type").text = "Sport"
    ET.SubElement(bike, "year").text = "2019"

    truck = ET.SubElement(root, "truck")
    ET.SubElement(truck, "make").text = "Ford"
    ET.SubElement(truck, "capacity").text = "F-150"
    ET.SubElement(truck, "year").text = "2021"

    # Create a new XML file with the results
    tree = ET.ElementTree(root)
    tree.write(file_name)

def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for vehicle in root:
        print(f"Vehicle Type: {vehicle.tag}")
        for detail in vehicle:
            print(f"{detail.tag.capitalize()}: {detail.text}")
        print()

# Example usage
write_xml("vehicles.xml")
read_xml("vehicles.xml")

    

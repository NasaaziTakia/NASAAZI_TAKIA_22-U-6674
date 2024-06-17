# Error handling in Python
# Exception handling with try, except, else and finally
# Custom exceptions

"""
Error handling in python helps to handle unexpected situations and errors

1. Try: contains code that might throw an exception
NB. If an exception occurs, the rest of the code in the try block is skipped or ignored

2. Except: catcges and handles exceptions
NB. You can specify different handlers to different exception types

3. Else: the code runs if no exception occurs
NB. If no exception is raised in the try block it runs

4. Finally: it runs whether an exception occurs or not
NB. Used for cleaning up actions

"""

#Example 1:handle expetion with division with zero
try:
    number=int(input('Enter a number:'))
    result=20/number
except ValueError:
    print('invalid number:please enter a valid number')
except ZeroDivisionError:
    print("error!Division by zero not alloweded")
else:
    print(f'Result is {result}')
finally:
    print('Excution completed sucessfully')
# #Exercise 1:write a function that converts a sting to an interger and handle both value errror
# #if the string cannot be converted as a interger and the type error ig the input is not a string 
# #use multiple expect bloch to handle these expetions
try:
    a=str(input("enter a string"))
    def convert():
        print(int(a))
except ValueError:
    print("Error! can not convert to interger")
except TypeError:
    print("input is not a string")
else:
    convert()
finally:
    print("string conversion to interger ")
#example 2: Exeception raised for input,if funds are insufficient

class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        self.balance=balance
        self.amount=amount
        self.massage=f"Attempt to withdraw{self.amount}"
        super().__init__(self.massage)
def withdraw(balance,amount):
    if amount>balance:
        raise InsufficientFundsError(balance,amount)
    return balance-amount

try:
    balance=20000
    amount_to_withdraw=10000
    new_balance=withdraw(balance,amount_to_withdraw)
except InsufficientFundsError:
    print("Error:{e.massage}")
else:
    print(f'withdraw sucessful! new balance is {new_balance}')
finally:
    print('transaction sucessful')
""" summary
    to define a custom exception
    class customError(EXception):
    def _init_(self,massage)
    self.massage=massage
    ##raising a custom exception
    """

 #Exercise 2:create a custom exception invalidageEror and write a function
 #that raises if the given age is negative.handle exceptio when calling the function
class InvalidageError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {age}. Age must be non-negative."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidageError(age)
    print(f"You are {age} years old.")

try:
    age = -1
    check_age(age)
except InvalidageError as e:
    print(f"Error! {e.message}")
finally:
    print("Execution complete.")
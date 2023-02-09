import math

#task 1
'''
Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
'''

class printler:
    def __init__(self):
        self.userInput=""

    def getString(self):
        self.userInput = input()

    def printString(self):
        print(self.userInput.upper())



#task 2
'''
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length:int) -> None:
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2
    

#task 3 
'''
Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
'''


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length
    

#task 4
'''
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def move(self, x, y):
        self.x+=x
        self.y+=y

    def dist(self):
        return math.sqrt(self.x**2+self.y**2)
    


#task 5
'''
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''
class Account:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.balance = 0

    def __showBalance(self):
       print(f"{self.owner}, your current balance is {self.balance}\n")

    def deposit(self, balance):
        self.balance+=balance
        self.__showBalance()

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance-=amount
            self.__showBalance()
        else:
            print(f"You cannot withdraw {amount}")
            self.__showBalance()


#task 6
'''
Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
'''

def isPrime(num: int):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True


items = [1,2,3,4,5,6,7,8,9,10]
items = filter(lambda x: isPrime(x), items)
print([i for i in items])
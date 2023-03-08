#Task 1
#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

def multiply_list_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

user_input = int(input("Введите числа: "))
my_list = user_input.split()
result = multiply_list_numbers(my_list)

print(result)

#Task 2
#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)

string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(string)
print("Number of uppercase letters: ", upper_count)
print("Number of lowercase letters: ", lower_count)


#Task 3
#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(string):
    reversed_string = string[::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")

#Task 4
# Write a Python program that invoke square root function after specific milliseconds.

import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000.0) 
    return math.sqrt(number)

number = int(input("Enter a number: "))
delay_ms = int(input("Enter delay in milliseconds: "))

result = delayed_sqrt(number, delay_ms)
print("Square root of", number, "after", delay_ms, "milliseconds is", result)


#Task 5
#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(tuple):
    return all(tuple)

user_input = input("Enter a list of elements separated by spaces: ")
my_tuple1 = user_input.split()

print("All elements of", my_tuple1, "are True:", all_true(my_tuple1))


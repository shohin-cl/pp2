#task 1.
"""
A recipe you are reading states how many grams you need for the ingredient. Unfortunately,
your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
"""
def gr_to_oun(gram):
    return gram * 28,3495231

gram = float(input())

print(gr_to_oun(gram))

#task 2.
"""
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""
def far_to_cen(far):
    return (5/9) * (far - 32)

far = int(input())

print(far_to_cen(far))

#task 3.
"""
Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs): 
"""
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits == numlegs):
            return chickens, rabbits
    return "No solution"

numhead = int(input())
numlegs = int(input())

#task 4.
"""
You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
"""

def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]


#task 5.
"""
Write a function that accepts string from user and print all permutations of that string.
"""


def next_permutation(a):
    n = len(a)
    i = 0
    j = 0
    for i in range (n-2, -1, -1):
        if(a[i] < a[i+1]):
            break
    if(i<0):
        a.reverse()
    else:
        for j in range (n-1, -1, -1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]
        st, end = i + 1, len(a)

        a[st:end] = a[st:end][::-1]

def prnt_nxt_prmtn(a):
    a = sorted(a) 
    b = sorted(a, reverse=True)
    while a!=b:
        print(''.join(a))
        next_permutation(a)
    print(''.join(a))

a = [i for i in input()]

#task 6.
"""
Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
"""

s = input()

def rev_wrds(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)


print(rev_wrds(s))


#task 7.
"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""

def has_33(nums):
    return '33' in nums

nums = input()
print(has_33(nums))


def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == 3 and nums[i + 1] == 3):
            return True
    return False


#task 8.
'''
Write a function that takes in a list of integers and returns True if it contains 007 in order
'''
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 



#task 9.
'''
Write a function that computes the volume of a sphere given its radius.
'''

def sphere_volume(rad):
    return (4/3) * 3.14 * (rad**3)


rad = int(input())
print(sphere_volume(rad))


#task 10.
'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
'''
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


#task 11.
'''
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''
def palindrome(strg):
    if strg == strg[::-1]:
        return True
    else:
        return False

strg = input()    

print(palindrome(strg))

#task 12. 
'''
Define a functino histogram() that takes a list of
integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
'''
def hist(num):
    for i in num:
        print('x' * i)


#task 13.
'''
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
'''

import random

def guess_the_num():
    name = input("Hello! What is your name?\n")
    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
    number = random.randint(1, 20)
    guess = 0
    guesses = 0
    while guess != number:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses))

guess_the_num()


#task 14.
'''
Create a python file and import some of the functions from the above 13 tasks and try to use them.
'''
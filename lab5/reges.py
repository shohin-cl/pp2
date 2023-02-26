import re
#Task 1
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
txt = input()
x = re.findall("ab*", txt)
if x !=0:
    print("Да")
else:
    print("Нет")

#Task 2
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

txt = input()
x = re.findall("ab{2,3}", txt)
if x != 0:
    print("Yes")
else:
    print("NO")

#Task 3
#Write a Python program to find sequences of lowercase letters joined with a underscore.

txt = input()
x = re.findall("[a-z]+_+[a-z]+", txt)
if x != 0:
    print("YES")
else:
    print("No")

#Task 4
#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

txt = input()
x = re.findall("[A-Z]+[a-z]+", txt)
if x != 0:
    print("YES")
else:
    print("NO")

#Task 5
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

txt = input()
x=re.findall("a.*b", txt)
if x!= 0:
    print("Yes")
else:
    print("NO")

#Task 6
#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

txt = input()
x = re.sub(r'[ ,.]', ':', txt)
print(x)

#Task 7
#Write a python program to convert snake case string to camel case string.

txt = input()
x = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)

print(x)


#Task 8
#Write a Python program to split a string at uppercase letters.

txt = input()
x =  re.findall('[A-Z][^A-Z]*', txt)

print(x)

#Task 9
#Write a Python program to insert spaces between words starting with capital letters.

txt = input()
x = re.sub(r'(?<!^)(?=[A-Z])', ' ', x)

print(x)

#Task 10
#Write a Python program to convert a given camel case string to snake case.

txt = input()
x = re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower() 

print(x)
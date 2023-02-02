#Python Boolean
print(10 > 9)
True
#-----------------------
print(10 == 9)
False
#-----------------------
print(10 < 9)
False
#-----------------------
print(bool("abc"))
True
#-----------------------
print(bool(0))
False
#-----------------------
#Python Operators
print(10*5)
#-----------------------
print(10/2)
#-----------------------
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#-----------------------
if 5 !=10:
  print("5 and 10 is not equal")
#-----------------------
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
#-----------------------
#Python List
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#-----------------------
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#-----------------------
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#-----------------------
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
#-----------------------
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#-----------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#-----------------------
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#-----------------------
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#-----------------------
#Python Tuples
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#-----------------------
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#-----------------------
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#-----------------------
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#-----------------------
#Python Sets
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#-----------------------
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#-----------------------
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#-----------------------
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#-----------------------
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#-----------------------
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#-----------------------
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#-----------------------
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#-----------------------
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#-----------------------
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
#-----------------------
#Python If and else
a = 50
b = 10
if a > b:
  print("Hello World")
#-----------------------
a = 50
b = 10
if a != b:
  print("Hello World")
#-----------------------
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#-----------------------
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#-----------------------
if a == b and c == d:
  print("Hello")
#-----------------------
if a == b or c == d:
  print("Hello")
#-----------------------
if 5 > 2:
  print("Five is greater than two!")
#-----------------------
if 5 > 2: print("Five is greater than two!")
#-----------------------
print("Yes") if 5 > 2 else print("No")
#-----------------------
#Python While loops
i = 1
while i < 6:
  print(i)
  i += 1
#-----------------------
i = 1
while i < 6:
  if i == 3:   
    break
  i += 1
#-----------------------
i = 0
while i < 6:
  i += 1
  if i == 3:   
    continue
  print(i)
#-----------------------
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#------------------------
#Python For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits :
  print(x)
#------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  
    continue
  print(x)
#------------------------
for x in range(6):
  print(x)
#------------------------
for x in range(6):
  print(x)
#----------------------------------------------

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))



x = "Hello"
y = 15

print(bool(x))
print(bool(y))



bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) 




bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")



x = 200
print(isinstance(x, int))



thislist = ["apple", "banana", "cherry"]
print(thislist)




thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

  x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)



thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)




thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) 



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



a = 33
b = 200
if b > a:
  print("b is greater than a")



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

 

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")






if a > b: print("a is greater than b")



a = 2
b = 330
print("A") if a > b else print("B")



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")




x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



i = 1
while i < 6:
  print(i)
  i += 1



i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")




fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)




for x in "banana":
  print(x)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)




for x in range(6):
  print(x)





for x in range(2, 6):
  print(x)



for x in range(2, 30, 3):
  print(x) 



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
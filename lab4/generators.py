#Python iterators and generators
#Task 1
def sqrtn(n):
    for i in range(n+1):
        yield i ** 2


n = int(input())
sqrtn(n)

#---------------------------------------

#Task 2
def evenn(n):
   for i in range(n):
     if i % 2 ==0: 
       yield i

n = int(input())
even = evenn(n)
print(", ".join(str(x) for x in even))


#Task 3
def divs(n):
  for i in range (n):
    if i % 3 == 0 and i % 4 == 0:
      yield i

n = int(input())
div = divs(n)
print(" ".join(str(x) for x in div))

#Task 4

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a, b = int(input()), int(input())

for square in squares(a, b):
    print(square)


#Task 5
def revnum(n):
  s = (i for i in range (n))
  for i in range (n, 0, -1):
    yield i

n = int(input())
rev = revnum(n)
print(", ".join(str(i) for i in rev))


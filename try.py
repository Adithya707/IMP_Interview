print("Hello world")

a = 10
if a < 55:
   print('Less')
   print(a,' did it work') #comment

x = str(3)
y = int(3)
z = float(3)
a = bool(4)
print(type(x))

b = 'Adi'
c = 'Ach'
print(b+c)

a, b, c = "Adi", "Ach", "Aka"
print(b) 

d = ['Adi','Ach','Aka']
x,y,z = d
print(z)

def myfunc():
  global x #assignment cannot be done in same line
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
x = ['apple','bananna'] list also x = list(("applie","bannana")) list -> ordered,changaeable duplicates are allowed can have different datatype
x = ('apple','bananna') tuple -> ordered , unchangeable(immutable) duplicates are allowed can have different datatype
x = {name:'Jhon',age:21} dict ordered  ordered,changaeable but duplicates are not allowed can have different datatype values
x = {'apple','bananna'} set -> unoreder(cannot be indexed) unchangeable duplicates are not allowed
"""

import random
print(random.randrange(1,10))

a = "Hello, World"
print(a[0])#print H

for x in a:
    print(x)

b = len(a)
print(b)

print("World" in a)#return bool

if 'Adi' not in a:
    print('Adi is not in a')

a = "Hello, World!"
print(a[2:5])
print(a[-5:-2])# ! is -1

"""
a.upper() a.lower() a.replace('W','J') replace W by J
a.strip() b = a.split(','); output in the form of a list
"""

b = a.split(',')
print(type(b))
print(b)

print('I am \"God\"')

a = 10
b = 7

if a>0 and b>0:
   print("Coorect")# and or a is b a is not b

if a is not b:
   print(a,"and", b ,"are not same") 

a = [10,20,40]
a.insert(2,30)#pos, val  a.append(val) a.extend(list2) a.remove(val) a.pop(index) if no index then last index
print(a)

for x in a:
    print(x)

for x in range(len(a)):
    print(a[x])

#print(a.sort(reverse=True))

b = list(a)
b = a+b
print(b)

a = (1,2,3)
y = (4,5)
a += y
print(type(a))
print(a)   

a = {3,2,1}
print(a) # a.add(val) a.update(set) a.remove(val)  c = a.intersection(b) similar val into set c


a = {
       "Name":'Adi',
       "Age":22,
       "Religion":"Hindhu"
    }
print(a.keys())
print(a.values())
for i in a.keys():
    print(i)
    
print(a)

a["Sport"] = "Football"
print(a) # a.pop(keyname)  a.clear()

for i,j in a.items():
    print(i,'->',j)
#pass, continue and break


x = lambda a:a+10 # lambda a,b : a*b x(2,3)

print(x(5))

print("classes")
class car:
      val = 10
c = car()
print(c.val)


class Person:
      def __init__(self,name,age):
          self.name = name
          self.age = age
      def p(self):
          print('Name: '+ self.name)
          print('Age: ',self.age)
  
p = Person("Adi",22)
p.p()
print(p.name)
print(p.age)  

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
      def __init__(self,fname,lname,age):
          super().__init__(fname,lname)
          self.age = age

x = Student("Mike", "Olsen", 2019)   


# min(list),max,abs,pow(x,y)x^y math.sqrt,math.ceil,math.floor   

#JSON to Python object
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x) 
print(type(y))
print(y)   

#Python to JSON
x = json.dumps(y)
print(type(x))
print(x)

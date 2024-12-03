#Task 4.1
# <  less than
# <=  less than or equal to
# >  greater than 
# >=  greater than or equal to 
# ==  equal to 
# !=  not equal to
#Task 4.2
i = int(True)
j = int(False)
b1 = bool(4)
b2 = bool(0)
print("Task #4.2")
print("yes this conversation is allowed")
#Task 4.3, 4.4, 4.5 ,4.6
import random
i1 = random.randint(0, 20)
i2 = random.randint(10, 20)
i3 = random.randint(10, 50)
i4 = random.randint(0, 1)
print("Tasks 4.3-4.6")
print(i1)
print(i2)
print(i3)
print(i4)
#Task 4.7
y = 1
if y > 0:
   x = 1
print("Task #4.7")   
print(x)
#Task 4.8
print("Task #4.8")
pay = 100
score = 91
if score >= 90:
    pay += pay * 0.03
    print(pay)
#Task #4.9
print("Task 4.9")
pay = 100
score = 89
if score > 90:
    pay += pay * 0.03
    print(pay)
else:pay += pay * 0.01
print(pay)
#Task 4.10
print("Task 4.10 A")
number = 30
if number % 2 == 0:
   print(number, "is even.")
print(number, "is odd.")
print("Task 4.10 B")
number = 35
if number % 2 == 0:
   print(number, "is even.")
else:
   print(number, "is odd.")
#Task 4.11
print("Task #4.11")
print("in x=3 y=2 it print x because y isnt greater than 2 its equal")
print("in x=3 y=4 it print 7")
print("in x=3 y=3 it print 6")
x = 3
y = 3
if x > 2:
  if y > 2:
    z = x + y
    print("z is", z)
  else:
    print("x is", x)
#Task 4.12
print("Task #4.12")
print("in x=2 y=4 it print x because y isnt greater than 2 its equal")
print("in x=3 y=2 it print x because y isnt greater than 2 its equal")
print("in the last one it print 6")
x = 3
y = 3
if x > 2:
  if y > 2:
    z = x + y
    print("z is", z)
  else:
    print("x is", x)
#Task 4.13
print("Task #4.13")
print("the code is written in the wrong order")
if score >= 60.0:
   grade = 'D'
elif score >= 70.0:
   grade = 'C'
elif score >= 80.0:
   grade = 'B'
elif score >= 90.0:
   grade = 'A'
else:
   grade = 'F'
#Task 4.14
print("Task #4.14")
if i > 0:
   x = 0
   y = 1
else:
   y = 0
   z = 0

if i > 0:
   x = 0
   y = 1
else:
   y = 0
   z = 0


if i > 0:
   x = 0
   y = 1
else:
   y = 0
   z = 0

if i > 0:
   x = 0
   y = 1
else:
   y = 0
   z = 0
print("all of them are indented")
print("Task #4.15")
#4.15
count = 10
if count % 10 == 0:
   newLine = True
else:
   newLine = False
print (newLine)
#4.16
print("Task #4.16")
age = 16
if age < 16:
   print("Cannot get a driver's license")
if age >= 16:
   print("Can get a driver's license")

if age < 16:
   print("Cannot get a driver's license")
else:
   print("Can get a driver's license")
print("Second one is better its better to do with else ")

#Task 4.17
print("Task #4.17")
number = 30
if number % 2 == 0:
   print(number, "is even")
if number % 5 == 0:
   print(number, "is multiple of 5")

number = 30
if number % 2 == 0:
   print(number, "is even")
elif number % 5 == 0:
   print(number, "is multiple of 5")
print("if we put 14 both of them shows even \n if we put 15 both of them shows multiple of 5 \n if we put 30 in the first code it shows multiple of 5 in the second it shows even")
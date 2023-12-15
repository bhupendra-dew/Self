'''
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
print(f"{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")
print(f"{celsius}° in Celsius is equivalent to {kelvin}° Kelvin.")
'''
'''
principal = float(input("Enter the principal: "))
time = int(input("Enter the number of years: "))
interest = float(input("Enter the rate of interest: "))

simple_interest = (principal * time * interest) / 100
compound_interest = principal * (pow((1 + interest / 100), time))

print(f"After {time} years at {interest}%, the investment will be worth ${compound_interest}.")
'''
'''
i = int(input("Enter the number: "))
print("no in binary form is: ", bin(i))
print("no in octal form is: ", oct(i))
print("no in hexadecimal form is: ", hex(i))
'''
'''
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"The area of the rectangle is {area}.")
print(f"The perimeter of the rectangle is {perimeter}.")
'''

'''
n = int(input("Enter the number: "))
i = 2
count = 0
while i < n:
    if n % i == 0:
        count += 1
    i = i + 1
if count > 0:
    print("Not a prime number")
else:
    print("Prime number")
'''
'''
a = input("Enter the string: ")
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
'''
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print(f"The area of the circle is {area}.")
print(f"The circumference of the circle is {circumference}.")
'''
'''
def num(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = int(input("Enter the number: "))
num(n)

Enter the number: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''
'''
n = int(input("Enter the number: "))
num = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print("\r")
'''
'''
import math
n = int(input("Enter the number: "))
def is_prime(n):
    if n <= 1:
        return ("Not a prime number")
    if n == 2:
        return ("Prime number")
    if n % 2 == 0:
        return ("Not a prime number")
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return ("Not a prime number")
    return ("Prime number")
print(is_prime(n))
'''
# Factors of a number
'''
import math
a = int(input("Enter the number: "))
l = []
for i in range(2, a + 1):
    if a % i == 0:
        l.append(i)
print(l)
print(max(l))
'''
'''
# reverse a number
a = input("Enter the number: ")
b = a[::-1]
print(int(b))
'''

# Reverse a number
'''
a = int(input("Enter the number: "))
rev = 0
while a > 0:
    rem = a % 10
    rev = rev * 10 + rem
    a = a // 10
print(rev)
'''
'''
class Car:
    def  setenginemodel(self,engine):
        self.engine = engine

    def getenginemodel(self):
        return self.engine
    
class Honda(Car):    
    def setcarmodel(self, model):
        self.model = model

    def getcarmodel(self):
        return self.model

engine = input("Enter the engine model: ")
model = input("Enter the car model: ")
mycar = Honda()
mycar.setenginemodel(engine)
mycar.setcarmodel(model)
print("Car Details:")
print("Engine Model:", mycar.getenginemodel())
print("Car Model:", mycar.getcarmodel())
'''
'''
class Person:
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
   
class Student(Person):
    def setage(self, age):
        self.age = age
    def getage(self):
        return self.age

a = int(input("Enter the number of students: "))
b = []
c = []
for i in range(a):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    b.append(name)
    c.append(age)
    student = Student()
    student.setname(name)
    student.setage(age)
    print("Name:", student.getname())
    print("Age:", student.getage())
print("Names of the students:")
print(b)
print()
print("Ages of the students:")
print(c)
'''
'''
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
volume = (4 / 3) * math.pi * radius * radius * radius
print(f"The area of the circle is {area}.")
print(f"The volume of the circle is {volume}.")
'''
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
n = int(input("Enter the number: "))
print(fact(n))
'''
'''
def pritnFun(test):
    if test < 1:
        return
    else:
        print(test, end=" ")
        pritnFun(test - 1)
        print(test, end=" ")
        return
test = int(input("Enter the number: "))
pritnFun(test)
'''
# Fibonacci series
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input("Enter the number: "))
print(fib(n))
for i in range(0, n):
    print(fib(i), end=" ")
'''

# Factorial of a number
'''
def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)
    
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"Factoria of the number is:",f(n))
'''

# Recursion using factorial of a given number
'''
def factorialUsingRecursion(n):
    if n == 0:
        return 1
    return n * factorialUsingRecursion(n - 1)

# Using Iteration to find the factorial of a given number

def factorialUsingIteration(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
num = int(input("Enter the number: "))
print(f"Factorial of the number using recursion is:", factorialUsingRecursion(num))
print(f"Factorial of the number iteration is:", factorialUsingIteration(num))
'''
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)
print(f"GCD of the numbers is:", gcd(num1, num2))
'''
'''
### Shubhams Question ###
found = False

def nums(a):
    sum = 0
    while a > 0:
        sum += a % 10
        a //= 10          
    return sum

x = int(input("Enter start: "))
y = int(input("Enter end: "))
for x in range(x, y + 1):
    if x % 3 == 0:
        if x % 7 == 0 or x % 7 > 4:
            if nums(x) % 6 == 0:
                found = True
                print(x, end=" ")
    
if found == False:
    print("No such number found")
'''
# Multiplication table of a given number
'''
a = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{a} * {i} = {a * i}")
'''

# Maximum efficiency of a list of numbers
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = l.shuffle()
l1 = []
for i in range (a):
    for j in range(i + 1, (a)):
        l1.append(l[i] * l[j])
print(l1)
print(max(l1))
'''
'''
year = int(input("Enter the year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
'''

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
count = int(input("Enter the limit: "))

if count <= 0:
    print("Enter the number greater than 0")
else:
    for i in range(count):
        print(fib(i), end = " ")


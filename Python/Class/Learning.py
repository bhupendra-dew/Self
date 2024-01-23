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
'''
'''
class repalce:
    def rep(self, a, b):
        self.a = a
        self.b = b
        self.a = self.b
        return self.a

l = [1,2,3,4,5]
b = []

rod = repalce()

for i in range(len(l)):
    if l[i] % 5 == 0:
        a = rod.rep(l[i], "@")
        b.append(a)
    elif l[i] % 4 == 0:
        a = rod.rep(l[i], "#")
        b.append(a)
    else:
        a = rod.rep(l[i], "*")
        b.append(a)
print(b)
'''
'''
a = input("Enter the number: ").split(",")
l = []
for i in a:
    if int(i) % 4 == 0:
        l.append("#")
    elif int(i) % 5 == 0:
        l.append("@")
    else:
        l.append("*")
print(l)
'''
'''
def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        t_sum = t_sum + term

    return t_sum * 4

terms = int(input("Enter number of terms: "))

pi = leibniz(terms)

print("Pi =", pi)
'''
'''
def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False
    
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter length of side c: "))

if is_valid_triangle(side_a, side_b, side_c):
    print("Triangle is valid.")
else:
    print("Triangle is Invalid.")
'''
'''
def is_valid_triangle(a, b, c):
    if a + b + c == 180 and a != 0 and b != 0 and c != 0:
        return True
    else:
        return False
    
angle_a = float(input("Enter angle a: "))
angle_b = float(input("Enter angle c: "))
angle_c = float(input("Enter number c: "))

if is_valid_triangle(angle_a, angle_b, angle_c):
    print("The triangle is Valid.")
else:
    print("Triangle is invald.")
'''
'''
def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False
    
def type_of_triangle(a, b, c):
    if a == b and b == c:
        print("Triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("Triangle is Isoceles.")
    else:
        print("Triangle is Scalane")

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)

else:
    print("Triangle is not possible from the given sides.")
'''

# Python program to Check Palindrome Number
'''
number = int(input("Enter the number: "))
copy = number
reverse = 0
while number != 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

# Check for Palindrome
if copy == reverse:
    print("%d is PALINDROME" %(copy))
else:
    print("%d is NOT PALINDROME" %(copy))
'''

# Check Prime
'''
number = int(input("Enter number: "))
flag = 1
for i in range(2, int(number / 2)):
    if number % i == 0:
        flag = 0
        break

if flag == 1 and number >= 2:
    print("PRIME")

else:
    print("Not PRIME")
'''

### Creating a simple matrix using Python

# Method 1 : Creating a matrix with the List of list
'''
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print("Matrix: ", matrix)
'''
# Method 2: Taking Matrix input form the user in Python
'''
Row = int(input("Enter the number of rows: "))
Column = int(input("Enter the number of column: "))

# Initialize Matrix
matrix = []
print("Enter the entries row wise: ")
for row in range(Row):
    a = []
    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)

for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end = " ")
    print()
'''

# Creating a matrix using lsit comprehension
'''
matrix = [[column for column in range(5)]for row in range (5)]
print(matrix)
'''
# Assigning value to individual cell in Matrx
'''
X = [[1,2,3], [4,5,6], [7,8,9]]
row = column = 1
X[row][column] = 11
print(X)
'''

# Assign a value to an individual cell using the negative indexing in Matrix.
'''
X = [[1,2,3], [4,5,6], [7,8,9]]
row = -2
column = -1
X[row][column] = 21
print(X)
'''

### Accessing Values in a Matrix

# Method 1: Acessing matrix values
'''
X = [[1,2,3], [4,5,6], [7,8,9]]
print("Matrix at 1 row and 3 column = ", X[0][2])
print("Matrix at 3 row and 3 column = ", X[2][2])
'''

# Method 2: Accessing Matrix values using negative indexing. 
'''
import numpy as np
X = [[1,2,3], [4,5,6], [7,8,9]]
print(X[-1][-2])
'''

### Mathematical Operators with Matrix in Python

# Example 1 : Adding values to a matrix with a for loop in Python
'''
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        result[row][column] = X[row][column] + Y[row][column]

for r in result:
    print(r)
'''

# Example 2 : Adding and Subtracting values to a matrix with the list comrehension
'''
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Add_result = [[X[row][column] + Y[row][column] for column in range(len(X[0]))] for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column] for column in range(len(X[0]))] for row in range(len(X))]

print("Matrix addition")
for r in Add_result:
    print(r)

print("\nMatrix Subtraction")
for r in Sub_result:
    print(r)
'''

# Python program to multiply and divide two matrices
'''
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

rmatrix = [[0,0,0], [0,0,0], [0,0,0]]
for row in range(len(X)):
    for column in range(len(X[0])):
        rmatrix[row][column] = X[row][column] * Y[row][column]

print("Matrix Multiplication")
for r in rmatrix:
    print(r)

for j in range(len(X)):
    for j in range(len(X[0])):
        rmatrix[row][column] = X[row][column] // Y[row][column]
        

print("\nMatrix Division")
for v in rmatrix:
    print(v)
'''
'''
F = False
class over:
    def __init__(self, x) -> None:
        self.x = x
        pass
    def __add__(self, other):
        if F == False: 
            print("The value of ob1:", self.x)
            print("The value of ob2:", other.x)
            print("The addition of two objects is:", end="")
            return (self.x + other.x)
        else:
            return True

ob = over(30)
'''


# Transpose in Matrix
'''
X = [[9,8,7], [6,5,4], [3,2,1]]
result = [[0,0,0], [0,0,0], [0,0,0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        result[column][row] = X[row][column]

for r in result:
    print(r)
'''

### Matrix using Numpy

# Creating a matrix using Numpy
'''
import numpy as np
arry = np.int128(10, size=(3,3))
print(arry)
'''

# Matrix mathematical operations in python using Numpy
'''
import numpy
x = numpy.array([1,2], [4,5])
y = numpy.array([7,8], [9,10])

print("The element wise addition of matrix is: ", )
print(numpy.add(x, y))
print("The element wise subtraction of matrix is: ", )
print(numpy.subtract(x, y))
print("The element wise multiplication of matrix is: ", )
print(numpy.multiply(x, y))
print("The element wise division of matrix is: ", )
print(numpy.divide(x, y))
'''
'''
import numpy as np
array = np.random.randint(10, size = (3,3))
print(array)
'''

# Matrix mathematical operations in python using Numpy
'''
import numpy

x = numpy.array([1,2], [4,5])
y = numpy.array([7,8], [9,10])

print("The element wise addition of matrix is: ", ) 
print(numpy.add(x, y))
print("The element wise subtraction of matrix is: ", )
print(numpy.subtract(x, y))
print("The element wise multiplication of matrix is: ", )
print(numpy.multiply(x, y))
print("The element wise division of matrix is: ", )
print(numpy.divide(x, y))
'''

# Dot and cross product with Matrix in Python using Numpy
'''
import numpy 

x = numpy.array([1,2,3], [4,5,6], [7,8,9])
y = numpy.array([9,8,7], [6,5,4], [3,2,1])

dotproduct = numpy.dot(x, y)
print("The dot product of two matrix is: ", dotproduct)

cr ossproduct = numpy.cross(x, y)
print("The cross product of two matrix is: ", crossproduct)
'''

import numpy
matrix = [[1,2], [4,5]]
print("The matrix is: ")
print("\n", numpy.transpose(matrix))
# Python program to declare variables
'''
myNumber = 3
print(myNumber)

myNumber = 4
print(myNumber)

myNumber = "Hello World"
print(myNumber)
'''

# Python program to illustrate a list
'''
# creating an empty list
nums = []
# appendig data in list
nums.append(21)
nums.append(40.5)
nums.append('String')

print(nums)
'''

# Python program to illustrate, getting input from user
'''
name = input("Enter your name : ")
# user enterd the name 'AD'
print('Hello', name)
'''

# Python program to illustrate, getting input from the user and then putting the output
'''
# accepting integer from the user, the return type of input() function is string, so we need to convert the input to integer
num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
num3 = num1 * num2
print('Product is : ', num3)
'''

# Python program to illustrate selection statement
'''
num = 13
if (num > 75):
    print('num is good')
elif (num < 33):
    print('num is not good')
else:
    print('num is ok')
'''

# Python program to illustrate fuctions
'''
def hello():
    print('hello')
    print('hello again')
hello()
# calling function
hello()
'''

# Python progrma to illustrate function with main
'''
def getInteger():
    result = int(input("Enter integer : "))
    return result

def Main():
    print('Started')

    # calling the getInteger function and storing its returened value in the output variable
    output = getInteger()
    print(output)

# now we are required to tell Python for 'Main' fuunction existence
if __name__ == '__main__':
    Main()
'''

# Python program to illustrate a sample for loop
'''
for step in range(10):
    print(step)
'''

# Python program to illustrate math module
'''
import math

def Main():
    num = -1394
    # fabs is used to get the absolute value of a decimal
    num = math.fabs(num)
    print(num)

if __name__ == '__main__':
    Main()
'''

# Python code to demonstrate working of iskeyword() and importing 'keyword' for keyword operations
'''
import keyword
# printing all keywords at once using 'kwlist()'
print("The list of keywords is : ")
print(keyword.kwlist)
'''

# Python program for True, False and None operators
'''
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False +False)

print(None == 0)
print(None == [])
'''

# Example : and, or, not, is and in keyword
'''
# Showing logical operation or (returns True)
print(True or False)
# Showing logical operation and(returns False)
print(False and True)
# Showing logical operation not(returns False)
print(not True)
# using "in" to check
if 's' in 'geeksForgeeks':
    print("s is part of geeksforgeeks")
else :
    print("s is not part of geeksforgeeks")
# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")
print("\r")
print(" " == " ")
print({} is {})
'''

# Example : For, while, break, continue keyword
'''
# Using for loop
for i in range(10):
    print(i, end = " ")
    if i == 6:
        break
print()
i = 0
while  i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end=" ")
    i += 1
'''

# Example : if else ad elif keyword

# Python program to illustrate if-elif-else ladder
# !/user/bin/python
'''
i = 20 
if (i == 10):
    print("i is 10")
elif(i == 20):
    print("i is 20")
else:
    print('i is not present')
'''

# def Keyword
'''
def fun():
    print("Inside Function")
fun()
'''

# Return keyword
'''
def fun():
    S = 0
    for i in range(10):
        S += 1
    return S
print(fun())
'''

# Yeild keyword
'''
def fun():
    S = 0
    for i in range(10):
        S += i
        yield S
for i in fun():
    print(i)
'''

# Python program to demonstrate instantiating a class
'''
class Dog:
    # A simple class attribute
    attr1 = 'mammal'
    attr2 = 'dog'
    # A sample method
    def fun(self):
        print("he is", self.attr1)
        print("he is a", self.attr2)
# Driver code object instantiation
Rodger = Dog()
# Accessing class attributes and method through objects
print(Rodger.attr1)
Rodger.fun()
'''

# Using with statement
'''
with open('file_path', 'w') as file:
    file.write('hello world !')
'''

# Example : as keyword
'''
import math as gfg
print(gfg.fac#torial(5))
'''

# Example : Pass Keyword
'''
n = 10
for i in range(n):
    # pass can be used as placeholder when code is to added later
    pass
'''

# Example : Lambda Keyword
'''
g = lambda x: x*x*x
print(g(9))
'''

# Example : Import, from Keyword
'''
# import keyword
from math import factorial
import math
print(math.factorial(10))
# from keyword
print(factorial(10))
'''

# Example : try, except, raise, finallly an assert Keywords
'''
# intializing number
a = 4
b = 0
# No exception Exception raised iin try block
try:
    k = a//b #  raises divide by zero exception
    print(k)
#handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    # this block is always executed regardless of exception generation
    print("This is always executed")
# assert Keyword using assert to check for 0
print("The value of a/b is : ")
assert b != 0, "Divide by 0 error"
print(a/b)
# raise keyword raises as user defined exceptin if strings are not equal
temp =  "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different")
'''

# raised keyword raises an user definrd exception if strings are not equal
'''
temp = 'geeks for geeks'
if temp != 'geeks':
    raise TypeError('Both the strings are different')
'''

# Example : del Keyword
'''
my_variables1 = 20
my_variables2 = "GeeksForGeeks"
# Check if my_veriable1 and my_variable2 exists
print(my_variables1)
print(my_variables2)
# delete both the varibles
del my_variables1
del my_variables2
# check if my_variable1 and my_variable2 exits
print(my_variables1)
print(my_variables2)
'''

# globaal varible
'''
a = 15
b = 10
# function to perform addition 
def add():
    c = a + b
    print(c)
# calling a fuction 
add()
# nonlocal keyword
def fun():
    var1 = 10
    def gun():
        # tell python explicitly that it has to access var1 initialized in fun on line 2 using the keyword nonlocal
        nonlocal var1
        var1 = var1 + 10
        print(var1)
    gun()
fun()
'''

# var1 is in the global namespace
'''
var1 = 5
def some_func():
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():
        # var3 is in the nested local namespace
        var3 = 7
'''

# Python program processing global varible
'''
count = 5
def some_methond():
    global count
    count = count + 1
    print(count)
some_methond()
'''

# Python program showing a scope of object
'''
def some_func():
    print('Inside some_func')
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var : ", var)
    some_inner_func()
    print('Try printing var form oter function : ', var)
some_func()
'''

# Python indentation 
'''
site = 'gfg'
if site == 'gfg':
    print('Logging on to geeksforgeeks...')
else:
    print('retype the URL.')
print('All set!')
'''

# Example 
'''
j = 1
while(j <= 5):
    print(j)
    j = j + 1
'''

# Program to check input type in python
'''
num = input("Enter number : ")
print(num)
name1 = input("Enter name : ")
print(name1)
# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))
'''

# SHowing the class type 
'''
num = int(input("Enter a number : "))
print(num, " ", type(num))
floatNum = float(input("Enter a decimal number : "))
print(floatNum, " ", type(floatNum))
'''

# Python program showiing how to multiple input using split
'''
# taking two inputs at a tie 
x, y = input("Enter two values : ").split()
print("Number of bos : ", x)
print("Number of girls : ", y)
# taking three inputs at a time 
x, y, z = input("Enter three values : ").split()
print("Total number of students : ", x)
print("Number of boys is : ", y)
print("NUmber of girls is : ", z)
# Taking two inputs at a time
a, b = input("Enter two values : ").split()
print("Firstnumber is {} and second number is {}".format(a, b))
# taking multiple inputs at a time and type casting using lisit() function
x = list((map)(int, input("Enter multiple values : ").split()))
print("List of students : ", x)
'''

#  Timer code
'''
import time
count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end = '>>>')
        time.sleep(1)
    else:
        print("Start")
'''

'''
import time
count_seconds = 5
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end = ">>>", flush = True)
        time.sleep(1)
    else:
        print("Start")
'''

# Finding the factorial using the recusion as well as iteration

'''
def factorialUsingRecursion(n):
    if (n == 0):
        return 1;
 
    # recursion call
    return n * factorialUsingRecursion(n - 1);
 
# ----- Iteration -----
# Method to find the factorial of a given number
def factorialUsingIteration(n):
    res = 1;
 
    # using iteration
    for i in range(2, n + 1):
        res *= i;
 
    return res;
 
# Driver method
num = 5;
print("Factorial of",num,"using Recursion is:",
                    factorialUsingRecursion(5));
 
print("Factorial of",num,"using Iteration is:",
                    factorialUsingIteration(5));
'''


# Finding maximum of two numbers
'''
def maximum(a, b):
    if a >= b :
        return a
    else:
        return b
    
# Driver code
a = int(input("Enter your number : "))
b = int(input("Enter your number : "))
print(maximum(a, b))
'''
'''
a = int(input("Enter your number : "))
b = int(input("Enter your number : "))
maximum = max(a, b)
print(maximum)
'''
'''
a = int(input("Enter your number : "))
b = int(input("Enter your number : "))
print(a if a >= b else b)
'''
'''
a = 2; b = 4
maximum = lambda a, b : a if a > b else b
print(f'{maximum(a, b)} is  a maximum number')
'''
'''
a = int(input("Enter the year"))
if (a % 4) == 0 :
    print("The year is a leap year.")
else:
    ("Not a leap year.")
'''
'''
a = int(input("Enter your age : "))
if a >= 18 :
    print("You are eligible for voting.")
else :
    print("You are not")
'''
'''
a = int(input("Enter the number : "))
b = a // 10
if (b % 3) == 0 :
    print("The last number is divisible by 3.")
else :
    print("Not")
'''
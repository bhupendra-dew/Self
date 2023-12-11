# Program to display capital letters form A to Z
'''
for i in range(65, 91):
    print(chr(i), end = " ")
'''

# Program to print the square of first 5 numbers
'''
for i in range(1,6):
    print(i ** 2)
'''

# wap to find odd no.s between 1 to 10 and print their sum
'''
b = 0
for i in range(1, 11):  
    if (i % 2) != 0:
        b += i
print(b) 
'''

# WAP to take 4 nos. form the user and find greatest one
'''
a = int(input("Enter no1 : "))
b = int(input("Enter no2 : "))
c = int(input("Enter no3 : "))
d = int(input("Enter no4 : "))

if a > b and a > c and a > d:
    print(a, "Is the biggest") 
elif b > a and b > c and b > d :
    print(b, "Is the biggest")
elif c > a and c > a and c > d :
    print(c, "Is the biggest")
else:
    print(d, "Is the biggest")
'''

# Wap to print all letters form word1 that also appears in word2
'''
w1 = "USA North America"
w2 = "USA South America"

for i in w1:
    if i in w2:
        print(i)
'''

"""
s = 0
i = 1
while i < 12:
    if ((i % 2) != 0):
        s = s + 1
    i = i + 1
print(s)       
"""

"""
s = 0
i = 0
while i < 6:
    s = s + i
    i = i + 1
print(s)
"""

# Wap to sum of digits of given number
'''
a = int(input("Enter the number : "))
s = 0

while a > 0:
    n = a % 10
    s = s + n
    a = a // 10
print(s)
'''

# WAp print no in reverse order
'''
a = int(input("Enter your number : "))

s = 0
while a > 0:
    n = a % 10
    a = a // 10
    s = s * 10 + n
print(s)
'''
'''

for i in range(1, 11):
    for j in range(1, i + 1):
        print("*" , end = " ")
    print()

'''
'''
n = input("No. de : ")
s = 0
a = len(n)
b = int(n)

while a > 0:
    r = b % 10
    s = s + (r ** a)
    n = b // 10
if (a == s):
    print("Yup")
else:
    print("Shooooooooottttttttt")
    
'''
'''
n = int(input("No de: "))
a = 0 
b = 1
s = 0
for i in range(0, n):
    
    a = b
    b = s
    s = a + b
    print(b, end=" ")
print()
'''
'''
first = int(input("no1 de :"))
second = int(input("no2 de : "))
limit = int(input("LIMIT de : "))
print(first, second, end=" ")
for i in range(limit):
    sum = first + second
    first = second
    second = sum
    print(sum, end = " ")
'''"""
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(3, 0, -1):
    for j in range(1 , i +1):
        print(j, end=" ")
    print()
"""
'''
def greater(x,y):
    if x > y:
        print(x,"is greater.")
    else:
        print(y,"is greater.")
n = int(input("x: "))
m = int(input("y: "))
greater(n, m)
'''
'''
def area(r):
    if r > 0:
        s = 3.14 * (r ** 2)
        print("area:", s)
    else:
        print("a point")
r = int(input("radius: "))
area(r)
'''
'''
#  gcd of two numbers

a = int(input("a: "))
b = int(input("b: "))
x = 1
while (x <= a and x <= b):
    if (a % x == 0 and b % x == 0):
        c = x
    x = x + 1
print(c)
'''
"""
a = (2, 5, 6, 3, 7, 8)
b = list(a)
for i in range(2, len(a) +2):
    b.append(i * i)
print(b)
b.sort(reverse=True)
tuple(b)
print(b)
"""

'''
# A function to calculate the sum of the elements in an array
def list_sum(A, n):
    sum = 0
    for i in range(n):
        sum += A[i]
    return sum
 
 
# A sample array
A = [5, 6, 1, 2]

 
# Finding the number of elements in the array
n = len(A)
 
# Call the function and print the result
print(list_sum(A, n))

'''
'''
a = 10
b = 4

print("a & b =", a & b)
print("a | b =", a | b)
print("~a =", ~a)
print("a ^ b =", a ^ b)
'''

'''
a = 10
b = -10

print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

print("a << 1 =", a << 1)
print("b << 1 =", b << 1)
'''
'''
class Geek:

    def __init__(self, value) -> None:
        self.value = value
        pass

    def __add__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __lshift__(self, obj):
        print("lshift operator overload")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class Geek")
        
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
    

if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)
'''
'''
a = 3
b = 5

c = a + b
print(c)
'''
'''
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping", item)
    else:
        print("not overlapping", item)
'''

'''
def overlapping(list1, list2):
    a = 0
    b = 0
    for i in list1:
        a += 1
    for j in list2:
        b += 1
    for i in range(0, a):
        for j in range(0, b):
            if list1[i] == list2[j]:
                return 1
    return 0

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
if overlapping(list1, list2):
    print("overlapping")
else:
    print("not overlapping")
'''

'''
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
'''
'''
expr = 10 + 20 * 30
print(expr)
name = "geeks"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
'''
'''
class A:
    def __init__(self, a) -> None:
        self.a = a
        pass

    def __add__(self, o):
        return self.a + o.a
    
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))

print(ob1.__add__(ob2))
print(ob3.__add__(ob4))
'''
'''
class complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        pass

    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
'''

'''
class A:
    def __init__(self, a) -> None:
        self.a = a
        pass

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False
ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
'''
'''
class A:
    def __init__(self, a):
        self.a = a
        pass
    def __lt__(self.a < other.a):
        if self.a < object.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        
    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"
        
obj1 = A(2)
obj2 = A(3)
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)
print(obj1 == obj2)
'''


'''
class A:
    def  __init__(self, a) -> None:
        self.a = a
        pass
    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator."
    
ob1 = A(2)
print(~ob1)
'''
'''
class MyClass:
    def __init__(self, value) -> None:
        self.value = value
        pass

    def __and__(self, other):
        return MyClass(self.value and other.value)
    
a = MyClass(True)
b = MyClass(False)
c = a & b
'''
'''
list1 = []
list2 = []

for i in range(1, 11):
    list1.append(4 * i)

for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print("any no. divisible by 5 in list1:", any(list2))
'''
'''
list1 = []
list2 = []

for i in range(1, 21):
    list1.append(4 * i - 3)

for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)

print("any odd no. in list1:", any(list2))
'''

'''
import operator
a = 4
b = 3
print("The addition of numbers is :", end=" ")
print(operator.add(a, b))
print("The subtraction of numbers is :", end=" ")
print(operator.sub(a, b))
print("The multiplication of numbers is :", end=" ")
print(operator.mul(a, b))
print("The division of numbers is :", end=" ")
print(operator.truediv(a, b))
print("The floored division of numbers is :", end=" ")
print(operator.floordiv(a, b))
print("The modulus of numbers is :", end=" ")
print(operator.mod(a, b))
print("The power of numbers is :", end=" ")
print(operator.pow(a, b))
print("The greater than of numbers is :", end=" ")
print(operator.gt(a, b))
print("The less than of numbers is :", end=" ")
print(operator.lt(a, b))
print("The equal to of numbers is :", end=" ")
print(operator.eq(a, b))
print("The not equal to of numbers is :", end=" ")
print(operator.ne(a, b))
print("The greater than or equal to of numbers is :", end=" ")
print(operator.ge(a, b))
print("The less than or equal to of numbers is :", end=" ")
print(operator.le(a, b))
print("The and of numbers is :", end=" ")
print(operator.and_(a, b))
print("The or of numbers is :", end=" ")
print(operator.or_(a, b))
print("The xor of numbers is :", end=" ")
print(operator.xor(a, b))
print("The not of numbers is :", end=" ")
print(operator.not_(a))
print("The length of numbers is :", end=" ")
print(operator.length_hint(a))
'''

'''
import operator
li = [1, 5, 6, 7, 8]
print("The original list is :", end=" ", sep=",")


for i in range(0, len(li)):
    print(li[i], end=" ")
print("\r")

operator.setitem(li, 3, 3)

print("The modified list after setitem() is :", end=" ")


for i in range(0, len(li)):
    print(li[i], end=" ")
print("\r")

operator.delitem(li, 1)

print("The modified list after delitem() is :", end=" ")


for i in range(0, len(li)):
    print(li[i], end = " ")
print("\r")

print("The 4th element of the list is :", end = " ")
print(operator.getitem(li, 3))
'''


# Python code to demonstrate the working of setitem(), delitem() and getitem()

'''
import operator

li = [1, 5, 6, 7, 8]

print("The original list is :", end = " ")
for i in range(0, len(li)):
    print(li[i], end = " ")
print("\r")
operator.setitem(li, slice(1, 4), [2, 3, 4])
print("The modified list after setitem() is :", end = " ")

for i in range(0, len(li)):
    print(li[i], end = " ")
print("\r")
operator.delitem(li, slice(2, 4))
print("The modified list after delitem() is :", end = " ")

for i in range(0, len(li)):
    print(li[i], end = " ")
print("\r") 

print("The 1st and 2nd elemnet of the list is :", end = " ")
print(operator.getitem(li, slice(0, 2)))
'''

#  Python code to demonstrate the working of concat() and contains()
'''
import operator
s1 = "geeksfor"
s2 = "geeks"
print("The concatenated string is :", end = " ")
print(operator.concat(s1, s2))

if (operator.contains(s1, s2)):
    print("geeksfor contains geeks")
else:
    print("geeksfor does not contain geeks")
'''

# Python code to demonstrate working of and_(), or_(), xor(), invert()
'''
import operator
a = 1
b = 0
print("The bitwise and of a and b is :", end = " ") 
print(operator.add(a, b))
print("The bitwise or of a and b is :", end = " ")
print(operator.or_(a, b))
print("The bitwise xor of a and b is :", end = " ")
print(operator.xor(a, b))
print("The inverted value of a is :", end = " ")
print(operator.invert(a))
'''
'''
def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str

s = "Geeks for Geeks"

print("The original string is : ", end = " ")
print(s)

print("The reserved string(using loops) is : ", end = " ")
print(reverse(s))
'''
'''
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1 : ]) + s[0]
    
s = "Geeksforgeeks"

print("The original string is : ", end = " ")
print(s)

print("The reversed string (using recursion) is : ", end = " ")
print(reverse(s))
'''
'''
def createStack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return True
    
def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, string[i])

    string = " "

    for i in range(0, n, 1):
        string += pop(stack)
    return string

s = "Geeksforgeeks"
print("The original string is :", end = " ")
print(s)
print("The reversed string(using stack) is :", end = " ")
print(reverse(s))
'''
'''
def reverse(String):
    String = String[::-1]
    return String

s = "geeksforgeeks"

print("The original string is :", end = " ")
print(s)

print("The reversed string is : ", end = " ")
print(reverse(s))
'''

# Reverse a string in Python using list comprehension()
'''
def reverse(string):
    string = [string[i] for i in range(len(string) -1, -1, -1)]
    return "".join(string)

s = "geeksforgeeks"
print("The original string is : ", s)
print("The reversed string is : ", reverse(s))
'''


# Reverse string in Python using the function call
'''
def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
s = "BhupendraDewangan"
print("The original string is : ", s)
print("The revresed string is : ", reverse(s))
'''
'''
gfg = "geeksforgeeks"
gfg = "".join(reversed(gfg))
print(gfg)
'''
'''
String1 = "Hello, I'm a Geek"
print("Initail String : ")
print(String1)

list1 = list(String1)
list1[2] = 'p'
String2 = "".join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

String3 = String1[0:2] + 'p' + String1[3:]
print(String3)
'''
'''
String1 = "Hello, I'am a Geek"
print("Initial String: ")
print(String1)

# Updating the string
String1 = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)
'''
'''
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)
'''
'''
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
del String1
print("\nDeleting entire String: ")
print(String1)
'''

str1 = " "
str2 = "geeks"

print(repr(str1 and str2))
print(repr(str2 and str1))
print(repr(str1 or str2))
print(repr(str2 or str1))

str1 = "for"

print(repr(str1 and str2))
print(repr(str2 and str1))
print(repr(str1 or str2))
print(repr(str2 or str1))

str1 = "geeks"

print(repr(not str1))

str1 = ""

print(repr(not str1))


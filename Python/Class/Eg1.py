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
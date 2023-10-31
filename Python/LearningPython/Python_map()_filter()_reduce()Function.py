# Using map function
'''
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
'''

# Using lambda function
'''
numbers = (1, 2, 3, 4)
result = map(lambda x : x + x, numbers)
print(list(result))
'''
'''
number1 = [1, 2, 3]
number2 = [4, 5, 6]

result = map(lambda x, y : x + y, number1, number2)
print(list(result))
'''
'''
# map() can listify the list of strings individually 
lists = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, lists))
print(test)
'''
'''
# Define a function that doubles even numbers and leaves odd numbers as is 
def double_even(num): 
	if num % 2 == 0: 
		return num * 2
	else: 
		return num 

# Create a list of numbers to apply the function to 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# Use map to apply the function to each element in the list 
result = list(map(double_even, numbers)) 

# Print the result 
print(result) 
'''
# ------------------------------------------------------------------------------
# Function that filters the vowels
"""
def fun(variable):
    letters = ["a", "e", "i", "o", "u"]
    if (variable in letters):
        return True
    else:
        return False
    
sequence = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
filtered = filter(fun, sequence)
print("The filtered letters are: ")
for s in filtered:
    print(s)
"""
# a list contains both even and odd numbers. 
'''
seq = [0, 1, 2, 3, 5, 8, 13]
 
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
 
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
'''
# Define a function to check if a number is a multiple of 3
'''
def is_multiple_of_3(num):
	return num % 3 == 0

# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to filter the list of numbers and only keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

print(result)
'''
# Function to filter vowels
'''
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False
    
sequence = ["g", "e", "e", "k", "s", "l", "o", "l", "i"]
filtered = filter(fun, sequence)
print("The filtered letters are: ")
for s in filtered:
    print(s)
'''
# Filter function in python with Lambda
'''
sequnce = [0, 1, 2, 3, 4, 5, 8 ,13]
result = filter(lambda x : x % 2 != 0, sequnce)
print(list(result))
result = filter(lambda x : x % 2 == 0, sequnce)
print(list(result))
'''
"""
# Filter function in Python with Lambda and Custom Function 
# define a function to check if a number is a multiple of 3
def is_multiple_of_3(num):
    return num % 3 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result)
"""
#---------------------------------------------------------------------------
# Reduce Function
# python code to demonstrate working of reduce() function
"""
import functools
lis = [1,2,3,4,5,6,7]
print("sum : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
print("max : ", end = "")
print("max : ", end="")
print(functools.reduce(lambda a, b : a if a > b else b, lis))
"""
# Operator function
'''
import functools
import operator
lis = [1, 3, 5, 6, 2]

print("Sum : ", end="")
print(functools.reduce(operator.add, lis))
print("Product : ", end="")
print(functools.reduce(operator.mul, lis))
print("Concatenated Product : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))
'''
# reduce() vs accumulated()
'''
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a iterator containing the intermediate results. The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
'''
# using reduce() and accumulate() functions
'''
import itertools # accumulate()
import functools # reduce()
lis = [1, 3, 4, 10, 4]
print("The summation of list using accumulate is : ", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))
print("Summation of list using reduce : ", end="")
print(functools.reduce(lambda x, y: x + y, lis))
'''

# reduce() functio with three parameters
'''x
# Python program to illustrate the sum of two numbers
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for elemnet in it:
        value = function(value, elemnet)
    return value
tup = (2, 1, 0, 2, 2, 0, 0, 2)
print(reduce(lambda x, y: x+y, tup, 6))
'''
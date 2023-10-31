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
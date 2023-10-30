# Searching the starting and ending index of "portal"
'''
import re

s = "GeeksforGeeks : A Computer science portal for geeks"

match = re.search(r'portal', s)

print("Start Index : ", match.start())
print("End Index: ", match.end())
'''

# \ - Backslash
# The backslash (\) makes sure that the character is not treated in a special way. This can be considered a way of escaping metacharacters.
"""
import re

s = 'geeks.forgeeks'

# without using \ 
match = re.search(r".", s)
print(match)

# using \
match = re.search(r"\.", s)
print(match)
"""

# [] - Square Brackets
# Square Brackets ([]) represent a character class consisting of a set of characters that we wish to match. 
# For example, the character class [abc] will match any single a, b, or c. 
'''
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)
'''

# ^ - Caret
# Caret (^) symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. For example –  

# ^g will check if the string starts with g such as geeks, globe, girl, g, etc.
# ^ge will check if the string starts with ge such as geeks, geeksforgeeks, etc.
"""
import re
# Match strings starting with "The"
regex = r'The'
strings = ["The quick brown fox", "The lazy Dog", "The Big Show", "A quick brown fox"]
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not Matched: {string}')
"""

# $ - Dollar
"""
Dollar($) symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not. For example – 

s$ will check for the string that ends with a such as geeks, ends, s, etc.
ks$ will check for the string that ends with ks such as geeks, geeksforgeeks, ks, etc.
"""
"""
import re
string = input("Enter the String: ")
pattern = r"World!$"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")
"""

# . - Dot
"""Dot(.) symbol matches only a single character except for the newline character (\n). For example –  

a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
.. will check if the string contains at least 2 characters"""
"""
import re

string = "The quick brown fox jumps over thenlazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
    print("Match Found!")
else:
    print("Match not found")
"""


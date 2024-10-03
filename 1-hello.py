# Ask user for their name, strip remove extra spaces.
name = input("What's your name? ").strip().title()

# f-string (formatted string literal). 
# This feature allows you to embed expressions inside string literals, 
# making it easy to include variable values in a string.
print(f"hello, {name}")

#
first, last = name.split(" ")

print(f"hello, {first}")
print(f"hello, {last}")



# capitalize 
name = name.capitalize()

# captalize like title (Capital letter of all word.)
name = name.title()

# It will not print next line. 
print("Hello ", end="")
print(name) 

# Output: hello "friend"
print('hello, "friend"')
 


# documentation
"""
documentation of python:
docs.python.org/3/library/functions.html#print(link)

print(*objects, sep=' ', end='\n', file=None, flush=False)

"""


# Ask user for surname.
surname = input("what's you surname? ")

#Remove whitespace from str and capitalize
surname = surname.strip().title()

# special string 
print(f"hello, {surname}")

"""
doucumentation 
doc.python.org/3/library/stdtypes.html#string-methods

"""



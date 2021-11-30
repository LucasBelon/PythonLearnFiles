# coding: utf-8

# 001 file, strings
# Strings study
# It's recommended to use only one type of quote to keep the code clean

line1 = 'Hello World! I\'m here to learn how to program with py3'
line2 = "I like Python, python is fun"
line3 = 'I like to study programming, I like to learn new stuff'
line4 = "Hello World!!!"

print(line1, line2, sep='\n', end='\n\n')
# print accepts more then one variable at once
# it has arguments that change de separator. Also has a 
# argument for concatenate
print(line3, line4, sep=' ++=++ ', end='\n')

help(print)
print(dir(print))

# Different ways to use print
print("""
In command line interface we can call python3 by writing python3 on the 
terminal. In order to execute a python command we can do python -c command 
[argument]. To execute a .py file as a script and init the interactive mode we 
can run python -i file.py
""")

print('''
There are 29 reserved words in python. These are:

and def exec    if  not return
assert  del finally import  or  try
break   elif    for in  pass    while
class   else    from    is  print   yield
continue    except  global  lambda  raise
''')

print('''
There are various ways to put variables inside strings. Commonly fstrings and 
.format() are used.
''')

a = 35
b = 'friends'
# With .format()
print('I have {} {}'.format(a,b))
# With fstrings
print(f'I have {a} {b}')
# with .format(argument)
greetings = 'Hello dear {name}'
print(greetings.format(name='Lucas').title())

# --------------------------------------------------------------------
# 002 file, maths

# Mathematical Operations
number1 = 20
number2 = 10
# addying
result = number1 + number2 ; print(result)
# It's possible to run two commands on the same line with the ;
# Subtraction
result = number1 - number2 ; print(result)
# Multiplication
result = number1 * number2 ; print(result)
# Division
result = number1 / number2 ; print(result)
# Whole Division
result = number1 // number2 ; print(result)
# Remain of division
result = number1 % number2 ; print(result)
# Power
result = number1 ** number2 ; print(result)
# Another way to power
result = pow(number1,number2) ; print(result)

a = input('Whatever you write will be storaged at "a" variable: ') ; print(a)
# The input will always generate a string
a = int(input('tell me your age: ')) ; print(a)
# We can transform variables. On above example a string was transformed to a int
a = float(input('tell me your age: ')) ; print(a)
# Now the transformation was from string to float
a = tuple(input('tell me a sequence of numbers, separated by spacebar: ').
        split()) ; print(a)
# From string to tuple
a = list(input('tell me a sequence of numbers, separated by spacebar: ').
        split()) ; print(a)
# From string to list
a = set(input('tell me a sequence of numbers, separated by spacebar: ').
        split()) ; print(a)
# From string to set

# --------------------------------------------------------------------
# 003 file, list types
 
# Creating fast matrix

'''
lines, cols = 3,3 
# 3,3 becomes a tuple, which is unpacked and become lines and cols variables
matriz = [['' for x in range(lines)] for y in range(cols)]
# x works like a index reader to the range object, which works as a enumerated 
# stack from 0
# We can read it like "I want a empty string for each found index on the 
# enumerated stack, all of them added to a list"
# This way, empty strings populates a list, and this list populates another 
# list, which is a matrix
print(matrix)
a = tuple(['a' for i in range(3)])
# We can use the same method to creat a tuple, but since it's immutable, it's 
# necessary to do a transformation from a list to a tuple
print(a)
'''

# Finding out if a loop succesfully ended
brothers = ('Lucas', 'Matheus', 'Gustavo', 'Isabela', 'Renan', 'Gabriel')
for item in brothers:
    # for each item from tuple we repeat some process
    confirm = input(f'Presence call: {item} is here? [y/n] - ').lower()
    # On the above line we made the string to show with lower case characters
    if confirm == 'n':
        print('{} is missing. Time to search!!!'.format(item))
        break
        #continue
    print('Atention, continuing presence call')
    # Here there's no else statement because if is there to stop for loop
    # If the loop finishes the else works, if loop got the break it doesn't
else:
    print("They're all here, let go family!!!")

# Organizing dictionaries (this format is the same as given on Json files)
info_characters = [ # We open and close a list
    { # We open and close a dictionary. Pay attention at the commas.        
        'name': 'Matheuzão',
        'nature': 'normal',
        'strength': 5,
        'speed': 3200
    },
    {
        'name': 'Del Rey',
        'nature': 'raio',
        'strength': 100,
        'speed': 160
    },
    {
        'name': 'Derby Prata',
        'nature': 'fogo',
        'strength': 200,
        'speed': 80
    },
    {
        'name': 'Véi Barrero',
        'nature': 'água',
        'strength': 500,
        'speed': 32
    },
    {
        'name': 'Camomila',
        'nature': 'terra',
        'strength': 2,
        'speed': 8000
    },
]
for i in info_characters:
    name,nature,strength,speed = i['name'],i['nature'],i['strength'],i['speed']
    # We access each item of the list (as a dictionary)
    # and set a key value pair.
    print(i)
# --------------------------------------------------------------------
# 004 file, Dict Comprehension

# Calculating prime numbers

'''
list = []
for n in range(2,1001):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} is equal to {x} * {n//x}")
            break
    else:
    print(f"{n} is prime")
'''

friends = ('Gabriel', 'Karina', 'Mateus', 'Vinicius', 'Heitor')
# The friends tuple will give the dict keys
afinity = (10,8,6,9,7)
# The tuple afinity will give the dict values
# sice the values are immutable it's preferable to use tuples
dictonary = {
        friends[i]:afinity[i]
        # a key:value will be added
        for i in range(len(friends))
        # for each index found in a range object
        if afinity[i] >= 7
        # but only some of them will be added
        }
print(dictonary)
dictionary2 = dict(zip(friends, afinity))
# we can simplify the process using the built-in funciont zip
# The zip function unites two sequences for it's index. If one sequence
# is bigger it will continue until it's no longer possible
# It's possible to turn a zip object in dict and tuple. To do it with 
# lists and sets it's storaged the output of the method
# __repr__(), which is the representation of the object.
print(dictionary2)
print(tuple(zip( (1,2,3),('a','b','c','d'),range(10,15) )))

# --------------------------------------------------------------------
# 005 file, functions
'''
def notWorkingDivision(x,y):
    # We'll use a if-else inside return in a compact way
    return 'you tried to divide by zero' if y==0 else return x/y
'''

def division(x,y):
    # If the action is a single line we can wrote it right after the :
    if y==0 : return 'Not possible to divide by zero'
    else:return (x/y)

# See an example of a funcion defined in one line using Type Hint
def notWorkingDivision(x:int or float, y:int or float)->float or str: return 'Not possible to divide by zero' if y==0 else x/y
# Important to keep in mind that the python's filosophy praise for readibility,
# so writing as above isn't nice.
# But since there's only one person reading it, who cares?

# Type Hint is meant to say which types of variables are expected as arguments 
# and what kind of output is given on the return
# When the function simply doesn't return nothing it's left with an None

print(notWorkingDivision(10,5)) # Output: 2.0

print(division(1,0)) # Output: 'Not possible to divide by zero'

# Lambda Functions

division = lambda x,y: x/y if y != 0 else "don't follow this dark path please"
print(division(3,2)) # Output: 1.5
print(division(3,0)) # Output: "don't follow this dark path please"

def newfunction(func):
    print('We can give functions as params to other functions')
    print(func(15,3))
    print("This works well doesn't it? "
            "Look at the parenthesis when using 'func' as param"
            "to 'newfunction'")
# Param is like an argument, but we call it a parameter when we're defining 
# functions, and argument when we're using it on execution

newfunction(division)
# We could write directly the lambda function as it follows
newfunction(lambda x,y: x/y)

# We can storage fuctions inside structures as lists, tuples, dictionaries...
sequence_operations = {
        'mean': lambda sequence: sum(sequence)/len(sequence),
        'total': sum, #The same as lambda sequence: sum(sequence)
        'major': max} #The same as lambda sequence: max(sequence)
students = [
    {
        'name': 'Lucas',
        'grade': (100, 20, 75, 100, 100)
    },
    {
        'name': 'Matheus',
        'grade': (90, 80, 100, 55, 100)
    },
    {
        'name': 'Gustavo',
        'grade': (100, 70, 100, 30, 100)
    },
    {
        'name': 'Gabriel',
        'grade': (100, 100, 20, 100, 100)
    },
    {
        'name': 'Renan',
        'grade': (100, 100, 100, 100, 100)
    },
    {
        'name': 'Isabela',
        'grade': (100, 80, 100, 100, 90)
    },
]

for student in students:
    # Each item at 'students' list is a dict, so, each 'student' is a dict
    (name, grade) = (student['name'], student['grade'])
    # We leave it explicit that the itens of the tuples are being paired

    print('\n', 'student: {name}'.format(name=name), sep='')
    # The first 'name' from 'name=name' stands for the variable inside the 
    # string
    # The second references the key 'name'
    # Obs: '\n' is a newline command for strings

    operation = input('Choose a operation [mean, total, major]: ')
    # We're waiting to get the dict keys that will access the values
    # And these values are functions
    # Keep in mind that those functions only works with numeric sequences

    result = sequence_operations[operation](grade)
    # Here i'm accessing the operation inside the dict, e giving (grade) which
    # is a numeric list as parameter
    print(result)


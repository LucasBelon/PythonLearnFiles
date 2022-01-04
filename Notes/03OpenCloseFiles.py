# coding: utf-8
"""
Author: Lucas Gouveia Belon
This file is part of a great summary about Python
"""
# File 011 OpenClose -----------------------------------------------------------
"""
We can access files in diferent modes. The first is the read mode.
The file must exist. We access file with locked permission privileges, and
We must never forget to close whenever we open a file. 

When we open a file, we're actually getting a copy and putting it on our ram 
memory. When we close a file we're letting free ram space
"""
my_file = open('Data.txt','r')
file_content = my_file.read()

my_file.close()
"""
We got the content of the file and stored it on a variable, and then closed
the file, so it's no longer on our ram memory. There are some issues with the
IO statement, but it's a deeper subject
"""
print(file_content)
del file_content
# The my_file still exists, but the connection is closed
user_name = input('Enter Your Name: ')

my_file_writing = open('Data.txt','w')
# 'w' mode erases whatever is on the file. This ways, there's a lot of ways to
# make mistakes.
my_file_writing.write(user_name)
my_file_writing.close()

# File 012 Data on lists ------------------------------------------------------

# Ask the user for a list of 3 friends
# For each friend, we'll tell the user wheter they are nearby
# For each nearby friends, we'll save their name to `nearby_friends.txt`

# hint: readlines()

# We open the file on read mode
a = open('people.txt','r')
# We save the content on a variable, using list comprehension, and using
# Some string methods
b = [line.strip() for line in a.readlines()]
# We close the connection
a.close()
# We delete the connection
del a
# b is where our data is storaged
for i in b:
    close_friend=''
    while close_friend not in ['y','n']:
        close_friend = input(f'This person, {i}\nIs a friend or an '\
                f'acquaintance? [y/n]: ').lower()
    if close_friend == 'y':
        open('nearby_friends.txt','a').write(f'{i}\n')
    else:
        print("If it's not a friend, then it's not on my business")
# With this loop we write on append mode the name of the close_friend got on the
# people.txt file

del close_friend, b, i

# File 013 Almost CSV ------------------------------------------------------
# We do the same as before, open a file, store the content on a variable
# close the connection, erase the variable, start working on it

file = open('csv_data.txt','r')
lines = file.readlines()
file.close()
del file
lines = [line.strip() for line in lines[1:]]
# On the line above we delete any space or tab before and after the item
for line in lines:
    person_data = line.split(',')
    print(f'{person_data[0].title()} is {person_data[1]} years old and is '\
            f'studying {person_data[3].title()} at {person_data[2].title()}.'\
            f' Amazing isn\'t it?')

del line, lines, person_data

sample_csv_value = ','.join(['1','4','9','16','25','36','49','64','81','100'])
print(sample_csv_value)
del sample_csv_value
# File 014 Knowing JSON ------------------------------------------------------

import json
# We can use a module called json, it stands for Java Script Object Notation

file = open('friends_json.txt','r')
"""
We could do input(file.read()). But once the content is get by the .read() 
method we would no longer be able to access file contents
"""
file_contents = json.load(file) # reads file and turns it into a dictionary
# A list of dictionaries is how python interprets JSON objects
file.close()
del file

print(file_contents['friends'])

del file_contents

cars = [
    {'make': 'Ford','model':'Fiesta'},
    {'make': 'Ford','model':'Focus'}
]
# Go and investigat how to use Json.dump

file = open('json_cars.txt','w')
json.dump(cars,file)

file.close()
del file, cars

my_json_string = '[{"name":"Alpha Romeo", "Released":1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
del my_json_string, incorrect_car

# File 015 Using JSON ------------------------------------------------------

import json

#with open('Mexendo com Open, Data etc/friends_json.txt','r') as file:
with open('friends_json.txt','r') as file:
    file_contents = json.load(file)
# When we open over the with statement we open and close the file as soon as
# it's needed.
del file
# However I still like to del the reference to the file
print(file_contents['friends'])
del file_contents


cars = [
    {'make': 'Ford','model':'Fiesta'},
    {'make': 'Ford','model':'Focus'}
]
#with open('Mexendo com Open, Data etc/json_cars.txt','w') as file:
with open('json_cars.txt', 'w') as file:
    json.dump(cars,file)
del cars, file

my_json_string = '[{"name":"Alpha Romeo", "Released":1950}]'

incorrect_car = json.loads(my_json_string)
del my_json_string
print(incorrect_car[0]['name'])
del incorrect_car

"""
This file is about where are our objects in the memory
Also about how python is able to do so much of mutability stuff.
When we create objects, are they a new block of information in our memory or
is it just pointing to a pre-existing object?
What happens when we copy lists? We'll find out
"""
# File023 Mutability ----------------------------------------------------------

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# The friends_last_seen is a variable name, while the {'key':value} is the 
# information itself. The name points to the data, the name isn't by itself the
# information.

a = friends_last_seen
# What if we "copy" these things? We're actually linking two pointing objects, 
# two names, not creating a new dict object.
print(id(a))  
# The id func gives us the location of the first memory cell of the group
print(id(friends_last_seen))  

# We'll rewrite, and see if the id of the object changes.
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# A new object was created, and it's at another spot of RAM memory.
print(id(friends_last_seen))

friends_last_seen['Rolf'] = 3
print(id(friends_last_seen))
# Here we see that we made a change on a value. It's not a new object
# And that's what is the mutability concept
# We can use a trick to make a new copy of an existing object:
friends_last_seen = dict(friends_last_seen)
print(id(friends_last_seen))

''' What is immutable in Python:
Integers
Floats
Tuples
Strings
Bool
True
False
Null
NaN
'''
# File024 Ids Mutability ------------------------------------------------------
"""
We'll see now that we can actually see if a object have the same id of other.
It will see where the information is on the memory.
"""
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friend(friends, name):
    print(friends is friends_last_seen)
    # == checks value; 'is' checks id's
    friends[name] = 0

see_friend(friends_last_seen, 'Rolf')
# Here we have some local/global variables stuff happening, don't get lost.

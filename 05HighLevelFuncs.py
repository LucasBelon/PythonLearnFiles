# File 019filterfunc.py ------------------------------------------------------
"""
Python comes with lots of functions that are... Complicated. But it's better 
then to write our own functions in python, whose would not be that much fast, 
or not that much performatic. So... This 'chapter' is about the usage of those
funcs.
"""

# Will define a function that uses one of those functions, they're built-in, 
# which means that it's the 'battery included' part of python.
def starts_with_r(people):
    return people.startswith('R')
# That method 'startswith' is the built-in func we're talking about.
# It returns a bool value, and accepts as arguments some kinds of lists. Or 
# better saying, some kinds of containers.

friends = ("Roger", "Nathan", "Andressa", "Renan", "Sam")
# We could simply use 
# start_with_r = filter(starts_with_r, friends)
# But we can use lambda functions. Let's go
start_with_r = filter(lambda x: x.startswith('R'), friends)
# Arg 1 - lambda - Func that returns True/False based on a built-in func
# Arg 2 - friends - Tuple of friends that will be used on the filter function
# Obs: filter returns a generator, so it's more efficient then to copy the 
# list of names that starts with R
# obs2: filter will apply the function to each element of the list, one by one.
print("print(next(start_with_r))")

print(next(start_with_r))
print(next(start_with_r))

print("after the run")

another_starts_with_r = (f for f in friends if f.startswith('R'))
# The line above makes a tuple from the previous list. It will run once 
# massively. Not a good idea if you have an enormous amount of data.

print(list(another_starts_with_r))
print(list(another_starts_with_r))
# we ran it twice so we can see that we run out of data when we try to make a 
# list out of it.

def my_custom_filter(func, iterable):
    for i in iterable: # iterable must be a sequence of items
        if func(i): # func must return Bool
            yield i
"""
We did this for two reasons, one is to show that we can create our own funcs
with other functions. The other is to show that we can do a kind of generator
function from a simplier function.
"""
# File 020MapFunc.py ---------------------------------------------------------
"""
Now we'll see again the filter func, but also the map function.
The map function usage commonly is to apply a function to a sequence
The difference between Map and Filter is that Map applies a function over a 
sequence, and Filter creates a generator from a true-false analysis.
Think on Filter as a... Filter, and map as an application of a function over
a sequence.
"""

friends = ("Roger", "Nathan", "Andressa", "Renan", "Sam")
start_with_r = filter(lambda x: x.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))
print(next(friends_lower))
friends_lower = [friend.lower() for friend in friends]
print(friends_lower)
friends_lower = (friend.lower() for friend in friends)
print(next(friends_lower))
print("-----------")
# What we expected to see is the difference beetween aplying a func to a 
# sequence in may different ways. We used the map function that will return a 
# generator, we used a list compreension that will apply immediatly the
# function to each element, and we did the same with our 'tuple compreension'
# that also gives us a generator, but we must choose the ways that are known, 
# so, if we want to do it in the quickest way it's better to use high-level
# built-in functions.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        """
        Do not fear the 'cls', it's replacing our 'self'.
        This function is here so we're able to use dicts to create this
        User guy.
        """
        return cls(data["username"], data["password"])
        # Returns an instance of User class that will be created
        # from the items inside a dictionary with specific keys and values

# Now we create a dict with the format expected from the class and...
users = [
    {
        "username": "Lucas",
        "password": 6432565
    },
    {
        "username": "Matheus",
        "password": "Roblox"
    }
]
# create another user so the User class won't bother us about overwriting.
users2 = [
    {
        "username": "Lucas",
        "password": 6432565
    },
    {
        "username": "Matheus",
        "password": "Roblox"
    }
]
# We create a list of 'Users instances' from the 'users list of dicts'
# (quotes added so we can differentiate what user is about)
users = [User.from_dict(user) for user in users]
print(users[0].username)

a = map(User.from_dict, users2)
# Since we overwrote users list of dicts we need to use the users2
print(next(a).username)

# File 021AnyAll.py -------------------------------------------------------
"""
This chapter is most about searching through lists. What if we want to do a 
single true false search? We can do it with any and all
"""

friends = [
    {
        "name": "Renan",
        "location": "Washington, D.C."
    },
    {
        "name": "Ana",
        "location": "California"
    },
    {
        "name": "Charles",
        "location": "California"
    },
    {
        "name": "Bruno",
        "location": "San Francisco"
    }
]
# First we create a list of dictionaries with the name and location of
# some friends. Next we create a str variable where we storage our position.
your_location = input("Where are you Right Now? ")
# Now, from our position and our friends positions we can tell who is next to
# us and create a list with those values.
friends_nearby = [friend for 
        friend in friends if 
        friend["location"] == your_location]
# We could do as it follows
'''
if len(friends_nearby) > 0:
    print("You Are Not Alone!")
'''
# But again, there are some batteries included here
if any(friends_nearby):
    print("You Are Not Alone!")
# any() searches for truety values and returns true if there is at least one
# true value.
# Our little algoritm is done with it, but we need to see the other side of the
# coin, the all function
print(all([1, 2, 3, 4, 5]))
print(all([0, 1, 2, 3, 4, 5]))
# all() searches for falsey values and returns true if there is none falsey
# values. Remember that zero, empty lists, tuples, sets, dicts, are all falsey.
# File 022enumerate.py ------------------------------------------------------
"""
Since we can go through lists with the 'for' statement, sometimes it's not 
the best way to navigate in this sea. We use the enumerate built-in to do it
"""
# we create a list with top 3 friends (it could be a tuple)
top_friends = ["Matheus", "Gustavo", "Andressa"]
# And now we go for with the (i, friend) tuple that is returned from enumerate
for i, friend in enumerate(top_friends):
    print(f"My top {i + 1} friend is {friend}")
# We got a tuple, but a enumerate object is not a sequence of tuples like a list
for a in enumerate(top_friends):
    print(a)
    print(type(a))
# It's a kind of a generator.
print('print enumerate:',enumerate(top_friends), sep='\n')
# Output: <enumerate object at 0x0000007A16EDC440>
a = enumerate(top_friends)
print('print a: ',a)
print('print next enumerate',next(enumerate(a)))
print('print next enumerate',next(enumerate(a)))
print('print next enumerate',next(enumerate(a)))


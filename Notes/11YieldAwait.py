# file 045YieldFromAnotherIterator.py -----------------------------------------
"""
Yield is a weird subject. It says 'I can wait, save processing time', but it 
turns our functions into monsters, and we need to know how to deal with them.
Here we go again.
What we want is to get that concept of a task scheduler.
A deque is a double queue, because it has no 'preferred direction', it can be 
accessed from any end.
"""
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friends():
    """
    What we got here is a getter that will pull the itens of a list. But, it's
    a generator kind of function.
    """
    yield from friends


def greet(g):
    """
    In here we're trying to acess the generator, and asking for the next element
    in it, and when we do it we need to ask if there is a next element, that's
    why that 'try' is over there. And then... The function waits a little more.
    """
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass

friends_generator = get_friends()
g = greet(friends_generator)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# If we ask more 'next item' then we have in our queue things can end up
# showing a bad behavior.

# file 046YieldToGetData.py ---------------------------------------------------
"""
Here we're trying to use the yield to get data
The code commented below is a test

def greet():
    friend = yield
    # It's very weird to see a 'yield' being assigned to a variable
    print(f'Hello, {friend}')

g = greet()
g.send(None)
# Preparing the Generator
g.send('Adam')
# Sending the 'Adam' string to Yield.
# Then the function executes for 'Adam', but the StopIteration error occurs
g.send('Lucas') # If this line is executed an error occurs
# TypeError: Can't send Not-None values to a newborn generator
# Yield works well inside a structure of repetition where it can stop.
"""


from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield  # The function is suspended until a value is received
        print(f'{greeting} {friend}')  
        # We're getting one by one the items inside the deque, and waiting
        # for a greeting to happen.


def greet(g):  # Two ways to do the job:
    """
    g.send(None)  # We start a generator, a loop functino that can be suspended
    while True:
        greeting = yield  # The function is suspended until a value is received
        g.send(greeting)  # We send the greeting to the generator
        # and it's a loop, that is suspended
        # And we're waiting that it gets started and starts receiving values.
        # As it starts every loop step it's possible to send a many different
        # values
    """
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
# We start the loop by sending None to greeter. It's imeddiatly stoped, and the
# Value isn't assigned
greeter.send('Hello')
# With the generator started and waiting, we send a value to yield.

print("Hello World! Multitasking...")

greeter.send("How are you,")

# Now they're no longer generators, 'cause they aren't generating anything.
# Now we should call then co-routines.

# file 047AwaitAsync.py -------------------------------------------------------
from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print('O código para no próprio yield')
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
# print('We're right before sending None')
greeter.send(None)
# print('We just send None')
greeter.send("Hello")

greeting = input('Enter a greeting: ')
greeter.send(greeting)
greeting = input('Enter a greeting: ')
greeter.send(greeting)
greeting = input('Enter a greeting: ')
greeter.send(greeting)

# YIELD IS A FLAG THAT SAYS "I CAN WAIT TO RUN. LET OTHER THINGS TO HAPPEN
# USE PROCESSING BETTER"


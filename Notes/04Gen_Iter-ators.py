# File 016 Generators.py --------------------------------
"""
There are structures called generators. They have a special feature, they keep
the last state within it. For example, we could create a function that returns
a hundred numbers, from 1 to 100 the way above, but further we'll see that
we can create a generator with a special reserved word (we've seen the reserved
word on the first archive).
"""

def hundred_numbers():
    """
    A function that returns a list with a hundred numbers, from 0 to 99
    """
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums

print(hundred_numbers())

print([x*2 for x in hundred_numbers()])

def hundred_number():
    """
    A function that creates a generator of numbers that goes from 0 to 99
    """
    i = 0
    while i < 100:
        yield i
        i += 1
    """
    The line 'yield i' returns the i value and stops the execution of the 
    function. On the next execution it will resume from where it started and
    will stop again, until there's nothing to stop.
    This way, 'yield' is useful to make generators.
    """
# When we run print(hundred_number()) we must see the output:
# <generator object hundred_numbers at 0x000000E00B1F9510>

g = hundred_number()

print(next(g))
print(next(g))
print(list(g))

"""
We'll see that the g function is actually a list that is generated only when
we call it. This is related to the event-orientation programming. It's able to
stop and resume from where it started.
"""
# File 017 GenIterators.py ---------------------------------------
"""We will see that iterators aren't always iterables. We'll define a class
with a number in it's self. It'll have a __next__ method that returns a i+1
number. However, it will only allow to do it a hundred times. The diference
between this class from a iterator is that a iterator have on hand all of 
it's elements, or at least, it can call all of it's elements.
"""
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()
"""
We've seen that we actually got a list with all of the numbers inside it.
And the way it shows us the numbers is by changing the index of a list.
A list is a iterable object, it will always have it's elements and we can
travel through them with it's index. The numbers will be there, and won't
fade away as we run the __next__ method. That's what makes it iterable,
although the first method is a iterator. It's kind of confusing, but
it's more important to understand what things do them to understand this
silly names
"""
# File 018 Iter-Able-Ator.py -------------------------------------
"""
Now that we've seen that not always an iterator is iterable, we'll turn a 
iterator into a iterable, with some magic methods.
Remember, a list is a container, with n elements, where we can go back and
forwards, in a way that any element is lost. Sometimes we want to be able
to lose some data, we want to read, process and destroy. This way we're able to
keep low memory in usage.
"""

"""
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


print(sum(FirstHundredIterable()))

for i in FirstHundredIterable():
    print(i)
"""
# You can see that we added a single method in a children class, that inherit
# the __init__ and __next__ dunder methods. This way we are able to create
# a container with a kind of 'get' method, and we are able to move the cursor
# around the elements. It enables searches, seek methods, and many common tools
# of common lists.


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


# print(sum(FirstHundredGenerator())

# for i in FirstHundredGenerator():
#    print(i, end = ' ')

class AnotherIterable:
    def __init__(self):
        self.cars = ['fiesta', 'focus', 'chevrolet']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

for cars in AnotherIterable():
    print(cars)

my_numbers = [x for x in [1, 2,3 ,4 ,5] ] # List Compreension
my_numbers_gen = (x for x in [1, 2, 3, 4, 5] )
# The above line returns a generator. It's not a tuple compreension!
print(type(my_numbers_gen))


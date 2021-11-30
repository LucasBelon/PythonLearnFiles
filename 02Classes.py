# coding: utf-8
# 006 file ------------------------------------------
"""
Objects are classes instancies, so they share inheritance in functionalities
and atribute structures from those classes.

Every class has methods and attributes.
Metods are what you can do with the object
attributes are characteristics
Below there is a class to a mage
"""


class Mage:

    # When we're creating a class we say that the functions made with def's are 
    # methods

    def __init__(self, new_name, new_life, 
                    new_mana, new_strength,
                    new_magic, new_speed):
        # When __init__ method is defined, class characterístics also do
        # We can add features that do not come from the params, for exemple
        # we have self.bag
        self.name = new_name
        self.life = new_life
        self.mana = new_mana
        self.strength = new_strength
        self.magic = new_magic
        self.speed = new_speed
        self.bag = []

        # self is like an entity that keeps the object's attributes
        # They're "self characteristics"

    # There are special methods, represented by __method__. Those are the
    # Dunder Methods (Double-Underscore)
    # They're like fundamental blocks used to build a class
    # By reading documentation we can get a methods list and their major
    # functionalities, for the major data structures. Remember, in python
    # everything is an object
    def __len__(self):
        # Allow me to use len(mage) function
        return len(self.bag)

    def __getitem__(self, i):
        # Allow me to see the itens from a class atribute
        # In this case we are using to get access to the bag itens
        return self.bag[i]

    def __repr__(self):
        # Representation of the object in string form
        return f'<The Great Mage: {self.name}>'

    def __str__(self):
        # String shown when we do print(Mage)
        return f'\nName: {self.name}\nLife Points: ' \
               f'{self.life}\nMana Points: {self.mana}\nStrength' \
               f': {self.strength}\nGasto Mágico: {self.magic}\n' \
               f'Speed: {self.speed}\n '

    # In class definitions there are a few elements called as 'decorators'
    # They are used to modify the standard behave of a function, or to
    # define what is the behave of certain functions inside a class.
    # When we use the property decorator we can do a method call without
    # parentesis
    @property
    def firstitem(self):
        return self.bag[0]

    @property
    def kill(self):
        self.life = 0
        self.mana = 0
        self.strength = 0
        self.speed = 0
        print('You Died!!!')

    @property
    def use_magic(self):
        self.mana -= self.magic
        return print('You used you magic power. Mana Level:', self.mana)

    @property
    def see_bag(self):
        print(f'These are {self.name} belongings:')
        for i in range(len(self.bag)):
            print(self.__getitem__(i))

    # There's also the staticmethod decorator, which is used when the actions
    # from the method doesn't need any attributes
    @staticmethod
    def hi():
        print('Eu mandei dizer olá')


class DarkMage(Mage):
    def __init__(self, new_name, new_life, new_mana, 
                new_strength, new_magic, new_speed, power):
        # I still don't know exactly how to use the super(), but it seems that
        # with it I can get attributes and methods from another class.
        # See that I get all the Mage class infos and added the power attribute.
        super().__init__(new_name, new_life, new_mana,
                new_strength, new_magic, new_speed)
        self.power = power

'''
Mage = Mage('Gandalf, The White', 100, 3000, 10, 5, 100)
# I've created an object from mage class, or an instance of the mage class

print(Mage)
Mage.use_magic
Mage.use_magic

print(Mage)
Mage.kill
print(Mage)

# Here's where we see the importance of __getitem__()
Mage.bag += ['Staff', 'Magic Robe', 'Invisibility Cape']
for item in Mage.bag:
    print(item)

print(Mage)

DarkMage = DarkMage('The Invincible BlackNull',
            1000, 30000, 100, 50, 1000, 9999)

DarkMage.bag += ['Invisibility necklace', 'Destruction Robe','Dark Elm']
for item in DarkMage.bag:
    print(item)

print('')
print(DarkMage.firstitem)
DarkMage.kill
print(DarkMage)

Mage.see_bag
DarkMage.see_bag
'''


class Foo:
    # Still don't know what @classmethod does
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()


class Bar:
    # Usually it would be necessary to put the 'self' argument
    @staticmethod
    def hi():
        print('Hello, i don\'t take parameters')


your_object = Bar()
your_object.hi()
Mage = Mage('Gandalf, The White', 100, 3000, 10, 5, 100)
Mage.hi()

# From here to the end there is a copy from a site about dunder methods.
class A:
    def __new__(cls):
        print('The Creation of A\'s New Class')
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print('Initialization')

    def __del__(self):
        print('Exterminate, Exterminate... Finish.')


a = A()
del a


class B:
    def __init__(self, c):
        self.a = c

    def __repr__(self):
        return f'B ({self.a})'

    def __str__(self):
        return f'B with {self.a}'

    def __bytes__(self):
        return self.a.to_bytes(4, byteorder='big')

    def __format__(self, format_spec):
        if format_spec == 'f':
            return str(self.a)
        return str(self)


b = B(10)
print(repr(b))
print(str(b))
print(bytes(b))
print(format(b, 'f'))


class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0


alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))

# 007 file -------------------------------------------------------------------
"""
It seems that this file is used to get some new lessons about classes 
"""

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


'''
The classmethod allow us to access everything from a class
as like it was a function parameter.
number = FixedFloat.from_sum(123.113,132453.5643)
print(number)
#print(type(number))
'''


class Libra(FixedFloat):
    # We got here an class inheritance case
    def __init__(self, amount):
        super().__init__(amount)
        # We use super() to access suplerclass characteristics.
        # We get everything from FixedFloat and put on Libra's init
        self.symbol = '£'
    # We overwrite __repr__ with the below method
    def __repr__(self):
        return f'<Libra {self.symbol}{self.amount:.2f}>'

money = Libra.from_sum(15.234, 12.4212)
print(money)

# 008 file -------------------------------------------------------------------
"""
We'll get another lesson about classes. Now we'll see errors in classes
And the error class
"""
class Car:
    """
    This is a docstring. With it I can access Car.__doc__. It's common for
    docstrings to be defined with double or triple quotes
    """

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        return f'<Car {self.make} {self.model}>'


class Garage:
    """This is a docstring from Garage class. With it I can access 
    Garage.__doc__"""

    def __init__(self):
        self.cars = []

    def __len__(self) -> int:
        return len(self.cars)

    def add_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            # isinstance verifies if an object is an instance of a certain class
            # and returns a bool
            raise TypeError(
                f'You tried to add a {car.__class__.__name__}.' \
                f'But you can only add car type objects')
        self.cars.append(car)
        # raise NotImplementedError("We can't add cars to the garage yet!")


ford = Garage()
car = Car('ford', 'fiesta')
car2 = Car('Chevrolet', 'Zafira')
ford.add_car(car)
ford.add_car(car2)
print(len(ford))
print(ford.cars)
print(ford.__doc__)


class RunTimeErrorOnMyCode(TypeError):
    """Exception lauched when an "Oh shit" error happens."""

    def __init__(self, code=500, message="Oh shit. There's" \
            " something wrong here"):
        super().__init__(f'Error code: {code}; {message}')
        self.code = code


# raise MyCustomError("Oh Shit. There's something wrong here", 500)
err = RunTimeErrorOnMyCode()
print(err.__doc__)
#raise err <-- This statement force the error raise

# File 009 TryExceptError

class Car:
    """This is a docstring. With it I can access Car.__doc__"""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    """This is a docstring. With it I can access Garage.__doc__"""

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            # raise TypeError(f'You tried to add a {car.__class__.__name__}. 
            # But you can only add Car type objects
            raise ValueError(
                f'You tried to add a {car.__class__.__name__}.'\
                        ' but you can only add Car type objects')
        self.cars.append(car)


ford = Garage()
fiesta = Car('ford', 'fiesta')

try:
    ford.add_car('fiesta')
except TypeError:
    print('Your car isn\'nt a Car')
except ValueError:
    print('A ValueError raised')
finally:
    print(f'The garage now has {len(ford)} cars')
print('This program ended')

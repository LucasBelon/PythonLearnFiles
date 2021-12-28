# File 049Decorators.py -------------------------------------------------------
"""
Decorators are something like signs that changes our functions. It's very, very
like, truly very hard to understand immediatly, but we'll move forward slowly.
Let's say that I need to do a control over users that try to access a 
admin panel. We only want to allow admins to be able to see that panel.
"""

user = {
    "username": "Lucas123",
    "access_level": "admin"
}

"-------------------------------Version 1-------------------------------------"

def user_has_permission(func):
    if user.get("access_level") == "admin":
        return func
    raise RuntimeError


def my_function():
    return "Password for admin panel is 1234."


my_secure_function = user_has_permission(my_function)
print(my_secure_function())


"-------------------------------Version 2-------------------------------------"

# Here we start to do weird stuff. We're defining a function inside another
# function. Is it even allowed? Ok, calm down, we're returning our func also.

def user_has_permission(func):
    def secure_func():
        if user.get("access_level") == "admin":
            return func
    return secure_func()


def my_function():
    return "Password for admin panel is 1234."


my_secure_function = user_has_permission(my_function)
print(my_secure_function())
"""
What we're trying to do is to keep our main function safe, so it won't be
attacked. Yeah, it's weird and I don't get it.
"""

# File 050Decorators.py -------------------------------------------------------
import functools
user = {
    "username": "Lucas123",
    "access_level": "admin"
}


def user_has_permission(func):
    @functools.wraps(func)  
    # This decorator make the secure_func to has the same __name__, __doc__, 
    # As if it was func. Basically it pulls the information of the wrapped func
    def secure_func():
        """Hey"""
        if user.get("access_level") == "admin":
            return func()
    return secure_func

@user_has_permission
def my_function():
    """Allow us to retrieve the password for the admin panel"""
    return "Password for admin panel is 1234."


# my_secure_function = user_has_permission(my_function)
print(my_function.__name__)
# File 051Decorators.py -------------------------------------------------------
import functools
user = {
    "username": "Lucas123",
    "access_level": "admin"
}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        """Hey"""
        if user.get("access_level") == "admin":
            return func(panel)
    return secure_func

@user_has_permission
def my_function(panel):
    """Allow us to retrieve the password for the admin panel"""
    return f"Password for {panel} panel is 1234"


# my_secure_function = user_has_permission(my_function)
print(my_function.__name__)
print(my_function('movies'))
# File 052Decorators.py -------------------------------------------------------
import functools

user = {
    "username": "Lucas123",
    "access_level": "user"
}


def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get("access_level") == access_level:
                return func(panel)

        return secure_func

    return user_has_permission


@third_level('user')
def my_function(panel):
    """Allow us to retrieve the password for the generic panel"""
    return f"Password for {panel} panel is 1234."


print(my_function.__name__)
print(my_function('movies'))
# File 053Decorators.py -------------------------------------------------------
"""
def add_all(a1, a2, a3, a4):
    return (a1 + a2 + a3 + a4)


# vals = (1,3,5,7)
vals = {'a1': 1, 'a2': 3, 'a3': 5, 'a4': 7}
# print(add_all(*vals))
print(add_all(**vals))
"""


def add_all(*args):
    a = 0
    for i in args:
        a += i
    return a
    # return sum(args)


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'for {k} we have {v}')


print(add_all(1, 3, 5, 7, 9))

pretty_print(username='Jose123', access_level='admin')

pretty_print(**{'dif_username': 'Lucão123', 'dif_access_level': 'Owner'})
# File 054Decorators.py -------------------------------------------------------
import functools

user = {
    "username": "Lucas123",
    "access_level": "admin"
}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args,**kwargs):
        """Hey"""
        if user.get("access_level") == "admin":
            return func(*args,**kwargs)

    return secure_func


@user_has_permission
def my_function(panel):
    """Allow us to retrieve the password for the admin panel"""
    return f"Password for {panel} panel is 1234."


@user_has_permission
def another():
    return "We're returning something"


# my_secure_function = user_has_permission(my_function)
print(my_function.__name__)
print(my_function('movies'))
print(another())


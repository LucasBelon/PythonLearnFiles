# File 025defaultparam.py -----------------------------------------------------
"""
Now we'll see some tricks and tips about the params that goes on a function.
The first of all is the type hinting. What if our function is waiting for some
specific kind of data? And what if I wrote my program, but a friend is
by my side trying to find out what is happening? Type hinting is a 
non-mandatory tool to make things easier. And remember, python has it's zen
Explicit is always better then implicit.
"""
# first we create a dict
accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}
print(accounts)
# what we have below is:
# we are waiting for the amount param to be a float variable
# and the name to be a string.
# What we got when we use the "name='checking'" is that, if any
# argument is used, then it will use this one, the default arg.
def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of 
    an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

add_balance(500.00, 'savings')
print(accounts)
add_balance(500)
print(accounts)
# File 026MutDefaultParam.py --------------------------------------------------
# Here we got another example of a default param.
# Remember that we can have some similar results using smaller data types.
# That's why, instead of creating an empty list, we use None.

# def create_account(name: str, holder: str, account_holders: list = []):

def create_account(name: str, holder: str, account_holders: list = None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)

    return {
        'name': name,
        'main_acount_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf', ['Jen'])
a2 = create_account('savings', 'Jen')

print(a2)

# File 027ArgUnpacking.py -----------------------------------------------------
# Okay, but what if we want to use n arguments in a function? Or else:
# When we do print('string1', 'string2', 'string3'), how does print knows what
# to do with all these arguments? We'll find out

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and 
    return the new balance."""
    accounts[name] += amount
    return accounts[name]

# We want to do all those operations in our account.
transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]
# Below are some ways to do it, and one is with argument unpacking
for t in transactions:
    add_balance(*t)  # Argument Unpacking
    # add_balance(t[0],t[1])
    # add_balance( amount=t[0], name=t[1] )
    print(accounts)

# Here we got another example, now for creating new users with passwords:
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# imagine these users coming from a database
users = [
    {'username': 'Rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]
# user_objects = [User(username=data['username'],
#                       password=data['password']) for data in users]
user_objects = [User(**data) for data in users]
# ** Dict unpacking


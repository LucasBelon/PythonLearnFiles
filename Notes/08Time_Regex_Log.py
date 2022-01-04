# file 028DateTime.py ---------------------------------------------------------
"""
When we're talking about time we need to understand that we have many timezones
and our program may run in EUA, in many different countries of Europe, even at
Asia or Africa. Our code must not only work on where it was wrote, but also
at anywhere around the globe. We'll see how to deal with time
"""
from datetime import datetime, timezone, timedelta
# From library 'datetime' we'll import 3 modules

print(datetime.now(timezone.min))
print(datetime.now(timezone.max))
print(datetime.now(timezone.utc))
print(datetime.now(), end='\n\n')
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today, tomorrow, sep='\n')

print(today.strftime('%d-%m-%Y %H:%M'))  # string format time

# user_date = input('Enter the date in YYYY-mm-dd format: ')
# user_date = datetime.strptime(user_date, '%Y-%m-%d') # string parse time

# print(user_date)
print(datetime.now(timezone.utc) - today)

now = datetime.now(timezone.utc)
current_timestamp = now.timestamp()

now_from_timestamp = datetime.utcfromtimestamp(current_timestamp)
print(now_from_timestamp, '<- This one')
print(now.timestamp())
# file 029Timing.py -----------------------------------------------------------
"""
We can use time to tell us about days, months, and use it as a calendar so we 
can manage it well, or we can care about the time that a program spends when
It's running. We don't want a universe life longing program to run, we want
a program that ends fast.
"""
import time

# We'll write a funtion to find out how much time it lasts
def powers(limit):
    return [x ** 2 for x in range(limit)]

# And write a function to actually measure it
def measure(func):
    start = time.time()
    func()
    print(time.time() - start)
# When we do ( time.time() - start ) is equal to final time minus initial time.

measure(lambda: powers(50000))
# The measure function is wainting a function as an argument
# If we use powers, without any argument it just won't work, 'cause it has no 
# limit. So we put powers in a lambda function to overlap this issue
# And still, we would need to run this a lot of times, in order to, at least, 
# find out what is the average time. But we can use timeit library

import timeit
# timeit executes the function many times, so it's more reliable

print(timeit.timeit("[x**0.5 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: pow(x,0.5), range(10)))"))
print(timeit.timeit("list(map(lambda x: x**0.5, range(10)))"))
# The downside of it is that we need to put the function into a string

# file 030Regex.py ------------------------------------------------------------
"""
Machines like computers are very powerful to find patterns. When we want to
search for, lets say, a xxxx@xxx.com data in a database we can use a tool,
a very powerful tool called Regular Expressions. It exists in many languages
and even in many OS, and it would be a big trouble to work at searching in 
databases without it.
"""
import re

email = 'LucasBelon@github.com'.lower()
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name, domain, sep='\n')
print('##############')
###########################################

# And what if we're searching through a price list?
price = 'Price: $18,649.50'

# expression = 'Price: \$(189.50)'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)

print(matches.group(0))  # Entire Match
print(matches.group(1))  # First thing in brackets

price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)
# It's a very nice tool isn't it? There are many sources to study it
# file 031Loggin.py -----------------------------------------------------------
"""
Since we're looking to write useful programs we must know that things can get 
a little... caotic. But we shall no fear, if we're always keeping a log journal.
But, actually our code can generate it by using the logging library
"""
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logsLucas.txt')

# logger = logging.getLogger('test_logger')
logger = logging.getLogger(__name__)

logger.info('This is a info message')
logger.warning('This is a warning message')
logger.debug('This is a debug message')
logger.critical('This is a critical message')
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""


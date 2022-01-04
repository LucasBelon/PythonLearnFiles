# file 037Threads.py ----------------------------------------------------------
"""
There are some jobs that can wait to be finished, so we can save time. We need 
to talk about parallelism, and things can get trickier here.
When we can do two things at the same time we are wanting to run two different,
or not, process. When we talk about what is a process in linux we get the idea
that the process is created by a fork of a mother process, yada yada bla bla bla
Basically, there are more then one way to save time on a task, not only with 
that parallel process.
What if our task needs a user input? It will last, in the best cases, two or
three seconds, and the process of our python program will wait that time. But
time is money my friend. We can say to python:
    Hey, what about waiting while you do other tasks?
That's the spirit of threads, we can save that waiting time.
"""
import time

# from threading import Thread
from concurrent.futures import ThreadPoolExecutor
"""
In python we have some libraries with these timey programming, remember that 
there are a lot of programming paradigm, like the event-oriented programming.
If we created a process and it waits forever then it can't be a good program.
And in addition, if we keep creating these never ending processes, then we 
would overflow our machine.
Here's what we're going to do:
    We'll test a program that, while we're waiting the user to input it's name
    it does a lot of calculation. Imagine that we could show a login window
    while we're setting things up in a real program, that really useful.
"""

def ask_user():
    start = time.time()
    user_input = input('Enter Your Name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user: {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started Calculating...')
    [(x ** 2 + 2) for x in range(5000000)]
    print(f'complex_calculation: {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single Tread total time: {time.time() - start}')

# We could use a sintax like the one below, but it would be hard to read, so...
# we done the second way.

'''
thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()
'''
start = time.time()
# This sintax is similar to the "With openfile as file:"
# it will open and close a special condition, a special way, to simplify things.
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two Thread total time: {time.time() - start}')
# file 038Multiprocess.py -----------------------------------------------------
import time
from multiprocessing import Process

"""
When we're using the multiprocess module on a Windows OS it's important that
the actions that it takes are under the if __name__ == '__main__':
It's a way to the system to acknowledge that we're not creating a neverending
recursion that would crash everything. The def's of functions don't need
to be inside that if-statement, only it's call.
Summarising:
    Def's out of 'if', calls inside 'if'.
"""
def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'{user_input}, Good Morning'
    print(greet)
    print('ask_user time: ', time.time() - start)


def complex_calculationn():
    print('Starting Calculation...')
    start = time.time()
    [x ** 2 for x in range(2000000)]
    print(f'complex_calculation time:', time.time() - start)


if __name__ == '__main__':
    '''
    start = time.time()
    ask_user()

    complex_calculationn()
    print(f'Single Thread process time: {time.time() - start}')
    '''
    process1 = Process(target=complex_calculationn)
    process2 = Process(target=complex_calculationn)

    process1.start()
    process2.start()

    start = time.time()
    # ask_user()

    process1.join()
    process2.join()
    print(f'Two Process total time: {time.time() - start}')
"""
As we can see, the multiprocess mess up with the outputs, and thats a expected
situation. The important thing about the 'threads vs. process' is to know when 
to use each one of them
"""
# File 039MultiProcessTest.py -------------------------------------------------
#This is only a test
import process1
import process2
from multiprocessing import Process
if __name__ == '__main__':
    process1 = Process(target=process1.main)
    process2 = Process(target=process2.main)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
# file 040MultiProcessV2.py ---------------------------------------------------
import time
from concurrent.futures import ProcessPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'{user_input}, Good Morning'
    print(greet)
    print('ask_user time: ', time.time() - start)


def complex_calculation():
    print('Starting Calculation...')
    start = time.time()
    [x ** 2 for x in range(2000000)]
    print(f'complex_calculation time:', time.time() - start)


if __name__ == '__main__':
    start = time.time()
    ask_user()
    complex_calculation()
    print(f'Single Thread process time: {time.time() - start}')

    start = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two Process total time: {time.time() - start}')
# file 041SharedStatement.py --------------------------------------------------
"""
An important concept is the data manipulation by two different agents.
Imagine that there are two agents trying to add one to a variable.
Okay, the example is silly, but what if we're accessing a giant database with
many important data, and the minor unexpected change screws up the whole thing.
That's bad right? That's why we need to think carefully about it.
"""
import time
import random

from threading import Thread

counter = 0


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('-----------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
# file 042queued_threads.py ---------------------------------------------------
"""
Right, there's a strategy to put our 'workers' to do stuff with some order, 
we put then in a queue, so when one is doing, the others are waiting.
"""
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()  # Things to be printed out
counter_queue = queue.Queue()  # amounts to which increase counter


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() 
        # This waits until an item is available and them locks the queue
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'The new counter value is {counter}', '---------'))
        counter_queue.task_done()  # this unlocks the queue


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()
# file 043GenNotThreads.py ----------------------------------------------------
"""
Okay, we can put our tasks in a queue, but, what if our task has an easily
known endpoint? Then we can use generators to do it. Generators are powerful.
We can use then instead of threads, 'cause they have this 'wait' behavior.
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1


c1 = countdown(10)
c2 = countdown(20)

print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
# file 044TaskScheduler.py ----------------------------------------------------
"""
We can use a queue of tasks to switch between them, and it's a way to 
make them run in a ordered way. There are a lot of strategies.
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = [countdown(10), countdown(5), countdown(20)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task Finished')


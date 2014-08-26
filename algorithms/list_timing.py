import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

'''
To use timeit you create a Timer object whose parameters are two Python
statements. The first parameter is a Python statement that you want to time;
the second parameter is a statement that will run once to set up the test. By
default timeit will try to run the statement one million times. When its done
it returns the time as a floating point value representing the total number of
seconds. However, since it executes the statement a million times you can read
the result as the number of microseconds to execute the test one time. You can
also pass timeit a named parameter called number that allows you to specify how
many times the test statement is executed. The following session shows how long
it takes to run each of our test functions 1000 times.
'''

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

'''
list.pop() = O(1) because Python keeps track of the end of your list, and can
just run there and remove the item.

list.pop(x) = O(n) because Python then has to move all of the remaining items
over one slot so there aren't gaps during later indexing actions.
'''

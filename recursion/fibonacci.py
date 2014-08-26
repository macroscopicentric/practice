import time

#Naive Fibonacci calculation. Inefficient because it forgets its own progress and so repeats the same calculations at each level. (Ex: Calculates 7 by going 6, 5, 4, 3, 2, 1, then calculates 6 by going 5, 4, 3, 2, 1...)
#There's a good illustration of why this is inefficient here: http://mitpress.mit.edu/sicp/full-text/sicp/book/node16.html
def fib(n):
    start = time.time()
    if n == 0 or n == 1:
        print time.time() - start
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print fib(7)

#Memoized Fibonacci calculation. More efficient because works from the bottom up instead of the top down, so doesn't have to repeat steps or worry about remembering previous calculations.
def mem_fib(n):
    start = time.time()
    a, b = 0, 1
    #How to turn this loop into functional programming?
    for _ in range(n):
        a, b = b, a + b
    print time.time() - start
    return a

print mem_fib(7)
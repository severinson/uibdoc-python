import math

'''
task 1: Create a list of all numbers from 0 to 10 using a loop (or
some other way that does not involve manually writing all 10
numbers). (loops)
'''
print("task 1")
l = list(range(10))
print(l)
print()


'''
task 2: Create a dict mapping the integers 1 through 13 to their
square root. (dict, math)
'''
print("task 2")
d = dict()
for i in range(1, 14):
    d[i] = math.sqrt(i)
print("resulting dict is", d)

# fancy solution (using dict comprehension):
d = {i:math.sqrt(i) for i in range(1, 14)}
print("fancy solution dict is", d)
print()

'''
task 3: Sum all numbers in the list [4, 90, 13, 3, 107] that are
larger than 20. (for loop, if)
'''
print("task 3")
l = [4, 90, 13, 3, 107]
result = 0
for v in l:
    if v > 20:
        result = result + v
print("sum is", result)

# fancy solution (using list comprehension with an if):
result = sum(v for v in l if v > 20)
print("fancy sum is", result)
print()

''' task 4: Crate a list of all integers from 0 to 10. Then, multiply
the elements with odd indices, i.e., 1, 3, 5, ..., in the list by
3. Print the resulting list. (lists, list indexing, loops) '''
print("task 4")
l = list(range(10))
for i in range(10):
    if i % 2 != 0:
        l[i] = l[i] * 3
print("resulting list is", l)

# fancy solution (using map, lambdas):
l = list(range(10))
l = list(map(
    lambda x: x * (1+2*(x % 2 != 0)),
    l,
))
print("with (very) fancy solution", l)
print()

'''
task 5: Write a function that takes a dictionary as its argument and
returns a list of all values in the dictionary. You probably need to
have a look at the manual for dicts:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

(dicts, lists, functions)
'''
print("task 5")
def f(d):
    return list(d.values())
d = dict()
d[1] = 2
d[2] = "foo"
print(f(d))

# one-line function definitions using a lambda expression
# lambdas are the same as the @f() syntax in Matlab.
f = lambda x: list(d.values())
print(f(d))
print()

'''
task 6: Write code that simulates the probability of having heads come
up x times in a row when flipping a coin. The steps could be:

- Write a function that returns a random number 0 or 1 (you need to
import the random module for this), where 0 is heads and 1 is
tails. See this link for info about generating random numbers:
https://docs.python.org/3/library/random.html

- Call this function until tails (1) comes up and store the number of
times you had to run the function. Append this number to a list. Do
this at least a few thousand times to get enough samples.

- Create a dict that maps the length of the sequence of heads to the
- number of times this happened.

'''
import random
print("task 6")

def flip():
    if random.random() < 0.5:
        return 0 # heads
    else:
        return 1 # tails

samples = list()
for i in range(100000):
    count = 0
    outcome = flip()
    while outcome == 0:
        count += 1 # equivalent to count = count + 1
        outcome = flip()
    samples.append(count)

hist = dict()
for v in samples:
    if v not in hist:
        hist[v] = 0
    hist[v] = hist[v] + 1
print(hist)

# slight improvement using defaultdict (a special type of dict that
# gives default values to new keys).
print("task 6 with defaultdict")
import collections
hist = collections.defaultdict(int)
for v in samples:
    hist[v] = hist[v] + 1
print(hist)

# a problem with our previous solution is that it allocates a list of
# length equal to the number of samples. this is rather inefficient
# since we only look at each sample once. the solution is to use a
# generator.
print("task 6 with generators")
def sample(n):
    for _ in range(n):
        count = 0
        outcome = flip()
        while outcome == 0:
            count += 1
            outcome = flip()

        # yield is a special return statement that allows a function
        # to return values several times. the function is paused
        # between each time we request a value from it.
        yield count
    return

hist = collections.defaultdict(int)
# iterating over a generator pulls values out of it until return is
# called in the generator function.
for v in sample(100000):
    hist[v] = hist[v] + 1
print(hist)

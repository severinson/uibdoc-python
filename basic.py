'''This is the first module of the UiBdoc intro to Python for
researchers. It covers the basics of Python. Subsequent modules will
cover more advanced concept and the Python for scientific computing.

I am convinced that the best way to learning programming is to
actually program. Hence, your first task is to write the code below
into the REPL (the interactive Python terminal). Run one segment at a
time to see what it does. Try changing some of the values and code to
see what happens.

I have some more tasks at the bottom of the document. If you already
feel comfortable with all of this you can go straight to the tasks.

'''

# lines that start with a # is a comment
print("Hello, this script introduces the most commonly used features in Python!")
print()

# variables: for storing values and data. unlike in Java variables in
# Python can hold values of any type.
print("--- variables and printing them ---")
name = "Albin"
print("Hello,", name)

first_name = "Albin"
last_name = "Severinson"
full_name = first_name + " " + last_name
print(full_name)

# strings in Python are immutable (cannot be changed) like in
# Java. also like in Java strings are classes with methods that allow
# you to make various changes. see https://docs.python.org/3.7/library/stdtypes.html#string-methods
s0 = 'Captain Jack'
s1 = s0.strip(' Jack')
s2 = s0.replace('Jack', 'Anya')
print(s0)
print(s1)
print(s2)

a = 4
b = 3
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "/", b, "=", a/b)
print(a, "*", b, "=", a*b)

# if statements: for making decisions
print("--- if statements ---")
a = 4
if a < 5:
    print("a is less then 5")

b = 5 # try changing this value
if b < 5:
    print("b is less then 5")
elif b < 10:
    print("b is less than 10 and greater than or equal to 5")
else:
    print("b is 10 or greater")

# loops: for doing things multiple times
print("--- loops ---")
for i in range(10): # in Python we use range(n) to do something n times
    print("FOR: i=", i)

# however, the pythonic way is to loop over collections, not indices
words = ['foo', 'bar', 'foobar'] # this is a list
for word in words:
    print(word)

j = 0
while j < 10:
    print("WHILE j=", j)
    j += 1

# lists: for storing list of anything
print("--- lists ---")
l = [1, 2, 5, 10]
print(l)
l.append("banana") # adding element to a list
print(l)

for v in l: # iterating over the elements of a list
    print("v=", v)

# list indexing: getting the elements of a list
print("--- list indexing ---")
print("first element", l[0])
print("second element", l[1])
print("first 2 elements", l[:2])
print("3rd to 4th elements", l[2:4])
print("last element", l[-1]) # so-called negative indexing

# dictionaries: for associating something with something else
print("--- dictionaries ---")
d = dict()
d["foo"] = 1 # "foo" is called the key and 1 is the value it maps to.
d["bar"] = "cool"
print(d)
print("d[\"foo\"]=", d["foo"])

# tuples: for storing an immutable ordered collection of items
print("--- tuples ---")
t = (1, 2, 'foo')
print(t)
# t[0] = 10 doesn't work!
a, b, c = t # tuple unpacking
print(a, b, c)

# functions: for re-using code
print("--- functions ---")

def f(a, b):
    print("f called with arguments", a, b)
    return a + b

result = f(2, 10)
print("results is", result)

# tuple unpacking allows for multiple return values
def g(a, b, c):
    return (a+b, b+c)

v1, v2 = g(1, 2, 3)
print('g returns two values', v1, v2)

# math: square root and other math operators
print("--- math ---")
import math # math library is a module that has to be imported
print("sqrt(2)=", math.sqrt(2))

# Objects in python
print("--- objects ---")
class Rectangle(object):
    '''Class representing a rectangle.

    '''

    def __init__(self, a, b):
        '''Constructor for the Rectangle object. Called with Rectangle(a,
        b). This is a so-called magic method. self is always given as
        the first argument to object methods and is used to access the
        object variables.

        '''
        self.a = a # corresponding to this in Java
        self.b = b
        return

    def __repr__(self):
        '''Return a string representation of the object. The equivalent of
        toString() in Java.

        '''
        # format is used to create strings containing variable values
        # print('__repr__ function called!')
        return 'Rectangle({}, {})'.format(self.a, self.b)

    def area(self):
        '''Return the area of the rectangle.

        '''
        return self.a * self.b

r = Rectangle(10, 5)
print(r) # automatically calls the __repr__ function
print('the area of', r, 'is', r.area())

'''

If you don't have much prior programming experience I recommend going
to this site and doing the exercises there.
http://codingbat.com/python

If you have some prior programming experience and just want to learn
how to do things in Python I recommend doing the following few
tasks. I recommend creating a new file for each task to keep it from
getting cluttered. Tasks 1-5 can be completed in one line of code if
you want to be fancy.

The concept involved in each task are written in parentheses.

task 1: Create a list of all numbers from 0 to 10 using a loop (or
some other way that does not involve manually writing all 10
numbers). Print this list. You can do it in one line using list
comprehension. (loops)

task 2: Create a dict mapping the integers 1 through 13 to their
square root without writing each entry manually. Print the resulting
dict. You can do it in one line using dict comprehension. (dict, math)

task 3: Sum all numbers in the list [4, 90, 13, 3, 107] that are
larger than 20. Print the result. You can do it in one line using list
comprehension and the sum function or the reduce function. (for loop,
if)

task 4: Multiply the elements with odd indices, i.e., 1, 3, 5, ..., in
the list of all integers 0 to 10 by 3. Print the resulting list. You
can do it in one line using list comprehension. (lists, list indexing,
loops)

task 5: Write a function that takes a dictionary as its argument and
returns a list of all values in the dictionary. You probably need to
have a look at the manual for dicts:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

(dicts, lists, functions)

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
number of times this happened.

Task 7: Create a class Pokemon that stores the name, current hit
points and strength of the Pokemon. The Pokemon class must have the
following methods:

- Constructor (__init__) that takes arguments name, max hit points and
strength.

- Method damage that takes as argument a number and inflicts that
  amount of damage to the Pokemon.

- Method attack that takes another Pokemon object as argument and
  inflicts damage to that Pokemon. The amount of damage should be
  proportional to the strength of the attacking Pokemon. I leave the
  specifics to you.

- Method is_conscicious that returns True if the Pokemon has 1 or more
  hit points and False otherwise.

Now make the Pokemon fight (letting the Pokemon be friends is also
acceptable)!

Task 8: Add unit tests to your Pokemon program. This requires reading
up on how the unittest module works.

Task 9: Expand your Pokemon program by finding creative uses for the
following features (example features in parentheses):

- reading/writing files (create a savefile system that allows you to
  write all stats about a Pokemon to a file on disk and to load those
  back next time you run the program. roll your own or look into the
  picke module.)

- lists/dicts/sets (write a trainer class that has a list of Pokemon
  in his inventory. each Pokemon object may contain a dict mapping
  move names to the different types of attacks it may carry out.)

- modules and packages (make your program into a package containing
  multiple modules)

'''

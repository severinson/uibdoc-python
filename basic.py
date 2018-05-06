'''This is the first module of the UiBdoc intro to Python for
researchers. It covers the basics of Python. Subsequent modules will
cover more advanced concept and the Python for scientific computing.

I am convinced that the best way to learning programming is to
actually program. Hence, your first task is to write the code below
into a new text file. Run your code between each of the sections
(delimited by a #) and look at the output. Try changing some of the
values and code to see what happens.

If you haven't used Python before I recommend you type manually
instead of copying.

The remaining tasks are found the bottom of the document.

'''

# lines that start with a # is a comment
print("Hello, this script introduces the most commonly used features in Python!")
print()

# variables: for storing values and data
print("--- variables and printing them ---")
name = "Albin"
print("Hello,", name)

first_name = "Albin"
last_name = "Severinson"
full_name = first_name + " " + last_name
print(full_name)

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

b = 5
if b < 5:
    print("b is less then 5")
elif b < 10:
    print("b is less than 10 and greater than or equal to 5")
else:
    print("b is 10 or greater")

# loops: for doing things multiple times
print("--- loops ---")
for i in range(10):
    print("FOR: i=", i)

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

# dictionaries: for associating something with something else
print("--- dictionaries ---")
d = dict()
d["foo"] = 1 # "foo" is called the key and 1 is the value it maps to.
d["bar"] = "cool"
print(d)
print("d[\"foo\"]=", d["foo"])

# functions: for re-using code
print("--- functions ---")

def f(a, b):
    print("f called with arguments", a, b)
    return a + b

result = f(2, 10)
print("results is", result)

# math: square root and other math operators
print("--- math ---")
import math # math library has to be imported
print("sqrt(2)=", math.sqrt(2))

'''

These tasks are for you to work on your own. I recommend creating a
new file for each task to keep it from being cluttered. Tasks 1-5 can
be completed in one line of code if you want to be fancy.

The concept involved in each task are written in parentheses.

task 1: Create a list of all numbers from 0 to 10 using a loop (or
some other way that does not involve manually writing all 10
numbers). (loops)

task 2: Create a dict mapping the integers 1 through 13 to their
square root. (dict, math)

task 3: Sum all numbers in the list [4, 90, 13, 3, 107] that are
larger than 20. (for loop, if)

task 4: Multiply the elements with odd indices, i.e., 1, 3, 5, ..., in
the list of all integers 0 to 10 by 3. Print the resulting
list. (lists, list indexing, loops)

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
- number of times this happened.

'''

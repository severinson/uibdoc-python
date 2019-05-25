'''A collection of generally useful functions. Note that this is a
horribly designed module.

'''

def do_useful_work(a, b):
    return a+b

def find_min(iterable):
    '''return the smallest value in iterable'''
    r = 1000
    for v in iterable:
        if v < r:
            r = v
    return r

def find_min(iterable):
    '''return the smallest value in iterable'''
    r = iterable[0]
    for v in iterable:
        if v < r:
            r = v
    return r

def find_min(iterable):
    '''return the smallest value in iterable'''
    r = next(iter(iterable))
    for v in iterable:
        if v < r:
            r = v
    return r

def find_min(iterable):
    '''return the smallest value in iterable'''
    try:
        r = next(iter(iterable))
    except StopIteration: # iterable is empty
        raise ValueError('iterable must not be empty')
    for v in iterable:
        if v < r:
            r = v
    return r

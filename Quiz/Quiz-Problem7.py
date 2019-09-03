# MIT quiz problem 7
#Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. 
#You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.
#Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). 
#The function will return a tuple of two dictionaries: 
#1. a dictionary of the intersect of d1 and d2
#2. a dictionary of the difference of d1 and d2, calculated as follows
#intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
#difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.

def f(a,b):
    return a + b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    # intersection, keys that are common to both d1 and d2.
    inboth = d1.viewkeys () & d2
    
    # symmetric difference, keys in either d1 or d2 but not both.
    outofboth = d1.viewkeys () ^ d2
    
    # apply f on values of the keys that common to both dicts.
    d3 = {k:f(d1[k], d2[k]) for k in inboth}
    d4 = {k:d1[k] for k in outofboth & d1.viewkeys()}
    
    # add key/value pairings from d2 using keys that appear in sym_diff
    d4.update({k:d2[k] for k in outofboth & d2.viewkeys()})
    return d3, d4
        
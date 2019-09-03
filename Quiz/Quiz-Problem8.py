# -*- coding: utf-8 -*-
# MIT quiz problem 8
#Write a Python function called satisfiesF that has the specification below. 
#Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.如果滿足f(s)= true,那就弄出這些s成為新的list
    Returns the length of L after mutation
    """
    # Your function implementation here
    removelist=list()
    for i in range(0, len(L)):
        if f(L[i]) == False:
            removelist.append (L[i])
    if removelist:
        for k in removelist:
            L.remove(k)   
    return len(L)
    

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L
#the code above's output should be
#2
#['a', 'a']


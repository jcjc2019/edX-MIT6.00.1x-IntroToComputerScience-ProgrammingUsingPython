#MIT final exam
#Problem 4- part 1
#This function returns a list of all possible sublists in L of length n without skipping elements in L. 
def getSublists(L, n):
    newlist = []
    for i in range (len(L)-n+1):
        newlist.append(L[i:i+n])
    return newlist
  
#problem 4 part 2
#Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.
def longestRun(L):
    L2 = []
    longest = 0
    for i in range(len(L)+1):
        for k in getSublists(L, i):
            L2.append(k)
    
    for h in L2:
        if sorted(h) == h and len(h) >= longest:
            longest = len(h)
    return longest
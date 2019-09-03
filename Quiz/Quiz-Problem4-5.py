# MIT Quiz problem 4
# find whether a string is a palindrome

def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    if not aString:
        return True
    else:
        return aString[0] == aString[-1] and isPalindrome(aString[1:-1])
        
# MIT quiz problem 5
#Write a Python function that returns the sum of the pairwise products of listA and listB. 
#You should assume that listA and listB have the same length and are two lists of integer numbers. 
#For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for i in range(0, len(listA)):
        sum = listA[i] * listB[i] + sum
    return sum
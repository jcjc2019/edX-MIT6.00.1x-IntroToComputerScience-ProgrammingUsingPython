# MIT Quiz problem 6
#a function to flatten a list. 
#The list contains other lists, strings, or ints. 
#For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0])+flatten(aList[1:])
    return aList[:1]+ flatten(aList[1:])
        
#below is another solution       
def flatten2(aList)
    return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in aList), [] )
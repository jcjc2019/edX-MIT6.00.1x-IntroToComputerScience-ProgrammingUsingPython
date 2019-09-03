#MIT program 3 Python loves fruit

def nfruits(fruits, pattern):

    #reduce one for last fruit
    last = pattern[-1]
    fruits[last] = fruits[last]-1
    for i in pattern[:-1]: #exclude the last fruit
        if i in fruits.keys():  
            #reduce 1 for eaten fruit
            fruits[i] = fruits[i] - 1
        for j in fruits.keys(): 
            if j != i:
                #add 1 for the remaining fruit
                fruits[j] = fruits[j] + 1
    
    return max(fruits.values())

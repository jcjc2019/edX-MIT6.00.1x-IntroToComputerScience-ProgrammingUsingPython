# below is the function to count the number of digits in a number
def ndigits(x):
    # when x is more than 0
    if x > 0:
    #change type to string, count the length of the string
        return len(str(int(x)))
    # when x is less than 0
    elif x < 0:
    #get the absolute value, change type to string, and count the length
        return len(str(abs(x)))
    else:
        return 0


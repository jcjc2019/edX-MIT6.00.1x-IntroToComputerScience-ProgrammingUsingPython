# MIT Week 2 polysum
import math
def polysum (n,s):
    area_1 = 0.25 * n 
    area_2 = s**2 
    area_3 = math.tan (math.pi/n)
    area = area_1 * area_2/area_3
    square_peri = (n * s)**2
    sum = area + square_peri
    return round(sum, 4)

polysum(25, 26)
print "This is a test.", "The sum is", polysum(25,26)
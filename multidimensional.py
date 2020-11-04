from numpy import *

# arr = array([1,2,3,2,5,4]) #in numpy we can skip the type we give while creating an array
# arr1 = array([1,2,3,7,89],int) #we can create in this way as well in case we need to mention type
# print(arr)
# print(arr1)

### Different ways of creatig arrays in numpy
#6 ways as below
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()

# arr = array([1,2,3,4,5],float)
#
# print(arr)
# print(arr.dtype)

# arr = linspace(0,15) #(start, stop, no of parts)
#
# print(arr)


# arr = arange(1,15,5) #(start, stop, step)
#
# print(arr)


# arr = logspace(1,40,5)
#
# print(arr)
# print('%.2f' %arr[4])


# arr = zeros(5)
#
# print(arr)


arr = ones(5,int)

print(arr)
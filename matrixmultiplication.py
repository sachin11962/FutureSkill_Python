from numpy import *

# arr1 = array([
#                 [1,2,3,6,3,1],
#                 [4,5,6,9,8,3]
#
#             ])
#
# print("Converting 2d array into 1d array and copying to new variabl")
# arr2 = arr1.flatten()
#
# print(arr1)
# print(arr1.dtype)#what type of data we are working with
# print(arr1.ndim)#gives the number of dimensions we are working
# print(arr1.shape)#gives number of rows and columns
# print(arr1.size)#gives the size of the entire block
#
# print(arr2)
#
# print("Converting 1d array into 3d array and copying to new variabl")
# arr3 = arr2.reshape(3,4) #rows,columns
#
# print(arr3)
#
# arr4 = arr2.reshape(2,2,3) #one big array which has 2 2D array, which has 2 1D array and which has 3 values
#
# print(arr4)


arr1 = array([
                [1,2,3,6],
                [4,5,6,9]

            ])


# print("converting 2D array into Matrix format")
# m = matrix(arr1)
#
# print(m)

# m1 = matrix('1,2,4;5,4,5;6,7,9')
# print(m1)
#
# print("only diagonal values")
# print(diagonal(m1))
# print(m1.min())


m1 = matrix('1,2,4;5,4,5;6,7,9')
print(m1)
m2 = matrix('1,2,4;5,2,5;2,7,9')
print(m2)

print("Addition of matrix")
print(m1+m2)

print("Multiplicaiton of matrix")
m3 = m1*m2
print(m3)



##################write a code to multiple array
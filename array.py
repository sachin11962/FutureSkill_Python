#Arrays holds similar type of values

#import array as arr
from array import *

#arr.array() #creating an array

vals = array('i', [5,9,-8,4,2])
#vals.reverse()

# print(vals)
# print(vals.buffer_info()) #gives the size of the array in the format: (Address, size)
# print(vals.typecode) #print the type of the code
# #print(vals)

# for i in range(5):
#     print(vals[i])

# for i in range(len(vals)):
#     print(vals[i])

for e in vals:
    print(e)

# i want to create a new array using existing array
newArr = array(vals.typecode, (a for a in vals))
print("New array values")
for z in newArr:
    print(z)

# I want to square the values and copy to new array
newArr1 = array(vals.typecode, (a*a for a in vals))
print("New array values")
for j in newArr1:
    print(j)

print("Printing values in while loop")
i = 0
while i < len(newArr):
    print(newArr[i])
    i+=1

##### work with character

# vals1 = array('u',['a','e','i'])
#
# for x in vals1:
#     print(x)
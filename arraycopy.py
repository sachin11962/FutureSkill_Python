from numpy import *

arr = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])
#
# #add 5 to each element manually
# for i in range(len(arr)):
#     arr[i] = arr[i]+5
#
# print(arr)
#
# #adding directly
# arr = arr + 5
#
# print(arr)

# ### add 2 arrays
# arr3 = arr + arr2
#
# print("Vectorized Operation",arr3)

#
# print(sin(arr))
# print(cos(arr))
# print(log(arr))
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(max(arr))
# print(unique(arr))
# print(sort(arr))
# print(concatenate([arr, arr2]))

# #aliasing
# arr4 = arr #copying array and called as aliasing
# print(arr)
# print(arr4)
#
# print(id(arr))
# print(id(arr4))


# #Create a different array which hold diff address
# arr5 = arr.view() #view is function which will help to create new array at different location
#
# print(id(arr))
# print(id(arr5))
#
# #shallow copy
# arr6 = arr.view()
# arr[1] = 7
# print(arr)
# print(arr6)
# print(id(arr))
# print(id(arr6))

#deep copy
arr7 = arr.copy()
arr[1]= 8
print(arr)
print(arr7)
print(id(arr))
print(id(arr7))
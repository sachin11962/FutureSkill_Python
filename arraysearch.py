##Array values from user in python and search in Array

from array import *


arr = array('i',[]) #creating an empty array

n = int(input("Enter the length of the array ")) #length of the array

#add the elements into the array as per the length

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x) #adding the elements into the array

print(arr)

#search using manually
print("Searching a value from array manually")

val = int(input("Enter the value for search "))

k = 0 #counter variable to keep the index count
for e in arr:
    if e == val:
        print(k)
        break

    k+=1

print("Searching a value from array using function")
val = int(input("Enter the value for search "))
print(arr.index(val))
#
# i = 1 #Initialization
#
# while i <= 5: #Condition
#     print("Telusko")
#     i = i + 1 #Increment/Decrement

# i = 5 #Initialization
# while i >= 1: #Condition
#     print("Telusko Decrement",end="") #Dont go on new line
#     j = 1
#     while j<=4:
#         print("Rocks",end=" ") #Dont go on new line
#         j = j+1
#     i = i - 1 #Increment/Decrement
#     print()


############## FOR Loop
x = ['navin', 65, 2.5]

for i in x:
    print(i)

z = 'NAVIN'

for i in z:
    print(i)

for i in [2, 6, "paul"]:
    print(i)

for i in range(11,21,5): #startingpoint, endingpoint, iteration
    print(i)

for i in range(20,11,-1): #Reverse order
    print(i)

print("Only the value which is not divisible by 5")
for i in range(1,21):
    if i % 5 != 0:
        print(i)
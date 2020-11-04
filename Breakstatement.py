#
# av = 5 #Available candyies in lending machine
#
# x = int(input("How many Candies you want?"))
#
# i = 1
# while i <= x:
#
#     if i > av:
#         print("Out of Stock")
#         break; #Come out the loop
#     print("Candy")
#     i+=1
#
# print("Bye")

# ######## print all values and skip number which are divisble by 3
# for i in range(1, 101):
#     if i%3 == 0 or i%5 == 0:
#         continue
#
#     print(i)
#
# print("Bye")


####### Pass
#Dont print odd numbers
for i in range (1, 101):
    if i%2 !=0:
        pass   #Just pass the block
    else:
        print(i)

print("Bye")
a = 5
b = 6
# """"""
# a = b
# b = a
# print('without using temp variable')
# print(a)
# print(b)
# """"""


# print('using temp variable')
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# a = a+b #11 -- here 11 needs 4 bits to evaluate
# b = a-b #5
# a = a-b #6
# print('without using temp variable - using operator')
# print(a)
# print(b)

# a = a ^ b
# b = a ^ b
# a = a ^ b
# print('with XOR')
# print(a)
# print(b)

print("Before swapping")
print(a)
print(b)
a,b = b,a #This works in one line but not in multiline
#Normally right side will solve first i.e., it solves b,a
#value of b is 6 and value of a is 5. This goes into stack
#then it reverse i.e., ROT_TWO() (Swaps the two top-most stack items)
#value of a comes to b and value of b comes to a
print("After swapping")
print(a)
print(b)
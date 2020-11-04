

a = 10 ##Global variable
print(id(a))

# def something():
#     global a ## if we want variale which is used inside function is global variable then we should use this line
#     #a = 15 ##local variable
#     a = 20 #now this a is referencing to global variable
#     print("in fun",a)
#
# something()
#
# print("outside", a)

def something1():
    #we want to use global and local variable in same function
    #we want local variable 'a' but we also want to change the global variable 'a' value
    a = 9

    x = globals() ['a'] #this globals() functin will give all the global variables
    print(id(x))
    print("in fun",a)

    globals()['a'] = 15 #changing the global variable value without affecting the local variable value

something1()

print("outside", a)
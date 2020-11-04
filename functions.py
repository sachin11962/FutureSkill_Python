

#1. Defining a function
#2. Calling a function

def greet():
    print("Hello")
    print("Good Morning")

# greet()
#
# greet()

def add(x,y):
    c = x+y
    print(c)

greet()
add(4,5)

### Return scenario
def add(x,y):
    c = x+y
    return c

result = add(6,5)
print(result)

### Return two values
def add_sub(x,y):
    a = x+y
    b = x-y
    return a,b

res1, res2 = add_sub(9,5) #when we are returning 2 values in function then we have to accept two values
print(res1, res2)

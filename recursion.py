
import sys
print("Default value", sys.getrecursionlimit())
sys.setrecursionlimit(2000) #setting the limit to 2000
print("After setting the value",sys.getrecursionlimit())

i = 0

def greet():
    global i
    i += 1
    print("Hello",i)
    greet()


greet()
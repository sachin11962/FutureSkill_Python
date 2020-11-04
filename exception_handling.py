
a = 5
b = 2

try:
    print("resource open")
    print(a/b) #critical statement
    k = int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e: # e is an object of an exception
    print("Hey, you cannot divide a number by zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong.. ")

finally:
    print("resource closed")

print("Bye")

##Defining a class
class Computer:

    def config(self):
        print("This is i5, 16gb, 1TB machine")

# x = 9
# print(type(x))
#
# a = '8'
# print(type(a))

com1 = Computer()
# print(type(com1))

com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()
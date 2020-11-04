#
# def add(a,b):
#     c = a + b
#     print(c)
#
#
# add(5,6)

def person(name,age):
    print(name)
    print(age)

person('sachin',28) ##Position arguments  - passing arguments in sequence

person(age=28, name='sachin') ## Keyword arguments

def person1(name,age=18):
    print(name)
    print(age)
person1('sachin') ## If dont pass age then by default age value should be 18
person1('sachin',28) ## if we pass then it will override the default value


#Variable length argument
def sum1(a, *b):  # *b can accept multiple values (b is tuple here)
    print(a)
    print(b)

    c = a #initially c will have the value of a

    #and then we will fetch one one value from b which is tuple and add it to c
    for i in b:
        c = c + i

    print(c)

sum1(5,6,4,54)

def sum2(*b):  # *b can accept multiple values (b is tuple here)
    print(b)

    c = 0 #initially c will have the value 0

    #and then we will fetch one one value from b which is tuple and add it to c
    for i in b:
        c = c + i

    print(c)

sum2(5,6,54,54)
# single * will not accept keyword arugments
# double ** will accept keyword arguments

def person(name, **data):

    print(name)
    print(data)

    for i, j in data.items(): #we have key and value pair
        print(i,j)


person('sachin', age = 28, city = 'Bengaluru', mob = 977879875)
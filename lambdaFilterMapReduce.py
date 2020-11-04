from functools import reduce
# def is_even(n):
#     return n % 2 == 0

nums = [3,2,6,8,4,6,2,9]

#evens = list(filter(is_even,nums)) #assign all the even numbers

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b : a+b,doubles)

print("Using Filter Method",evens)
print("Using Map Method",doubles)
print("Using Reduce Method",sum)
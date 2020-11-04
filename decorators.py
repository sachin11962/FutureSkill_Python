def div(a,b):
    # if a < b:
    #     a,b = b,a
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return inner

div1 = smart_div(div)

div1(4,2)
div1(2,4)
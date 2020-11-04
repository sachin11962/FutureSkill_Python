pos = -1

def search(list,n):
    i = 0

    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return True
    #     i = i+1
    # return False
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

list = [5,4,8,6,9,2]
n = 5

if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")
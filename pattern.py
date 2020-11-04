
for i in range(4):
    for j in range(4):
        print("# ",end="")

    print()

print("Triangle")
for i in range(4):
    for j in range(i+1):
        print("# ",end="")

    print()

print("Reverse Triangle")
for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()
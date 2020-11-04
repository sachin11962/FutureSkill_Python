
class A:

    def __init__(self):
        print("in a init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("in b init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()


#a1 = A() #Constructor

c1 = C()
c1.feature1()
c1.feat()
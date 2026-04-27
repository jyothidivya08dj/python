#inheritence
#single inheritence
class A :
    def one(self):
        print("this is base class")
class B(A):
    def two(self):
        print("This is derived class")
obj=B()
obj.one()
obj.two()

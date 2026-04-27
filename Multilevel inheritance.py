#multilevel inheritance:
class A :
    def one(self):
        print("this is base class")
class B(A):
    def two(self):
        print("This is derived class")
class C(B):
    def three(self):
        print("This is another class")
        
obj=C()
obj.one()
obj.two()
obj.three()

#destructor
class person:
    def __init__(self,name):
        self.name=name
        print("constructor called",self.name)
    def __del__(self):
        print("destructor called",self.name)
p1=person("Hello")
del p1

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

#hybrid inheritance
class animal:
    def sound(self):
        print("animal make sounds")
class mammal(animal):
    def make_sound(self):
        print("Mammals make sound")
class bird(animal):
    def makes_sound(self):
        print("birds do the sounds")
class bat(mammal,bird):
    pass
obj=bat()
obj.make_sound()
obj.sound()
obj.makes_sound()
   
        




#overriding
class mother:
    def parent(self):
        print("this is base class")
class child(mother):
    def parent(self):
        super().parent()
        print("this is child class")
ch=child()
ch.parent()

class animal:
    def sound(self):
        print("animal makes the sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("dog makes sound")
class cat(animal):
    def sound(self):
        print("cat makes sound")
c=dog()
c=cat()
c.sound()

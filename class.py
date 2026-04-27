class dog:
    attr1="puppy"
    attr2="snoopy"
    def display(self):
        print("This is",self.attr1)
        print("This is",self.attr2)
tomy=dog()
print(tomy.attr1)
tomy.display()


#person
class person:
    attr1="Divya"
    attr2=20
    def display(self):
        print("This is",self.attr1)
        print("This is",self.attr2)
p=person()
print(p.attr1)
p.display()

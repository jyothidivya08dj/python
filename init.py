class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
       print("My name is",self.name)
       print("age is",self.age)
s1=student("Hello",15)
s1.display()


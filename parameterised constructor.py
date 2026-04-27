class person:
    def __init__(self,name,age):
       self.name=name;
       self.age=age;
    def display(self):
        print("name is",self.name)
        print("age is:",self.age)
p1=person("madhu",24)
p1.display()

class sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("a+b",self.a+self.b)
        
s=sum(3,4)
s.display()

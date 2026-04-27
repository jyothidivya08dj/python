#car
class car:
    def __init__(self,model,cost,color):
         self.model=model
         self.cost=cost
         self.color=color
    def display(self):
        print("car model is",self.model)
        print("car cost is",self.cost)
        print("car color is",self.color)
c1=car("Thar",10000000,"white")
c1.display()

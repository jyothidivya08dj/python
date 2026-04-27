class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.amount=self.balance+amount
    def withdraw(self,amount):
        self.amount=self.balance-amount
    def display(self):
        print(self.name,"Balance is:",self.balance)
ba=bankaccount("cse",10000)
ba.deposit(1000)
ba.withdraw(500)
ba.display()

class python:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print( "student name is ",self.name,"marks is",self.marks)
c=python("divya",80)
c.display()
#structures
class vehicles:
    def move(self):
        print("vehicles are moves")
class car(vehicles):
    def drive(self):
        print("drive from one place to another")
class bike(vehicles):
   def ride(self):
        print("bike rides")
c=car()
c.drive()
c.move()
b=bike()
b.ride()
b.move()



#structures
class vehicles:
    def move(self):
        print("vehicles are moves")
class car(vehicles):
    def drive(self):
        print("drive from one place to another")
class boat(vehicles):
   def ride(self):
        print("boat sails in river")
v1=car()
v1.car()
v2=boat()
v2.boat()

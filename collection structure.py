#combine structure
class employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("employee's do the work")
class manager(employee):
    def work(self):
        print(self.name,"The manager mananges the team")
class tester(employee):
    def work(self):
        print(self.name,"the tester tets the code")
def employee_details (emp):
    emp.work()
m=manager("girls")
t=tester("boys")
employee_details(m)
employee_details(t)

try:
  marks=25
  result=25/0
  print(result)
except ZeroDivisionError:
    print("A number cannot be divide by zero")
finally:
    print("code was successful")

try:
  list=[1,2,3,4]
  print(list[8])
except IndexError:
     print("out of list")

try:
  f=open("example21","r")
except FileNotFoundError:
    print("file not found")
    
#exception
x=-7
if(x<0):
    raise Exception ("sorry we can't except below zero")

    







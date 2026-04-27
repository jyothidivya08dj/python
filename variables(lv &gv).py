


#global and local
x=100
def display():
    x=10
    print("the value for inside:",x)
display()
print("the value outside :",x)

#change global variable value
y=20
def change():
    y=40
    print(y)
change()

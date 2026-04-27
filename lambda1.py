add=lambda a,b:a+b
print(add (3,5))

square=lambda a:a*a
print(square(3))

cube=lambda n:n**3
print(cube(2))

n=int(input("enter n value"))
result=lambda n:"even" if n%2==0 else "odd"
print(result(n))


maximum=lambda a,b:max(a,b)
print(max(3,4))


n=[1,2,3,5,6]
print(list(map(lambda n:n+5,n)))


a=[1,2,3,4,5]
b=[2,3,4,5,6]
print(list(map(lambda a,b:a*b,a,b)))

a=[1,2,3,4,5]
print(list(filter(lambda a:a%2==0,a)))

a=[1,2,3,4,5]
print(list(filter(lambda a:a%2!=0,a)))

from functools import reduce 
l=[1,2,3,4,5]
print(reduce(lambda x,y:min(x,y),l))

from functools import reduce
a=["hello","world"]
print(reduce(lambda x,y:x+y,a))

a=["hello","world"]
print(lambda x,y:reverse(x,y),a)






    

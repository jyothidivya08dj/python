def greet(name="hello",age=24):
    print(f"my name is {name} and iam {age} years old")    
greet("hello",24)
greet(24,"hello")
n = int(input())

def count_digits(n):
    return len(str(abs(n)))

print(count_digits(n))


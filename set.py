Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====================================== RESTART: C:/Users/jyoth/Downloads/python/fibonacci.py ======================================
Traceback (most recent call last):
  File "C:/Users/jyoth/Downloads/python/fibonacci.py", line 1, in <module>
    n=int(intput("Enter the series"))
NameError: name 'intput' is not defined. Did you mean: 'input'?
a={1,2,3}
b={2,3,5,6}
print("The union is"a.union(b)) 

    
SyntaxError: multiple statements found while compiling a single statement
a={1,2,3}
b={2,3,4,5}
print("The union is",a.union(b))
The union is {1, 2, 3, 4, 5}
The union is {1, 2, 3, 4, 5}
SyntaxError: invalid syntax
print("The intersection is using &",a&b)
The intersection is using & {2, 3}
print("The differnce is using-",a-b)
The differnce is using- {1}
print("The differnce is using -",b-a)
The differnce is using - {4, 5}
print("The symmetric difference is using ^,a^b)
      
SyntaxError: unterminated string literal (detected at line 1)
print("The symmetric differnce is using ^",a^b)
      
The symmetric differnce is using ^ {1, 4, 5}
a={'east','west'}
      
b={'north','south'}
      
print(a)
      
{'west', 'east'}
first set={"east","west"}
      
SyntaxError: invalid syntax
firstset={"east","west","north"}
      
firstset.add('south')
      
print(firstset)
      
{'north', 'west', 'east', 'south'}
firstset.remove('north')
      
print(firstset)
      
{'west', 'east', 'south'}
firstset.remove('thing')
      
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    firstset.remove('thing')
KeyError: 'thing'
firstset.len()
      
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    firstset.len()
AttributeError: 'set' object has no attribute 'len'
firstset.len('west')
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    firstset.len('west')
AttributeError: 'set' object has no attribute 'len'
>>> firstset.len('firstset')
...       
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    firstset.len('firstset')
AttributeError: 'set' object has no attribute 'len'
>>> firstset.pop('west')
...       
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    firstset.pop('west')
TypeError: set.pop() takes no arguments (1 given)
>>> firstset.pop()
...       
'west'
>>> print(firstset)
...       
{'east', 'south'}
>>> firstset.len()
...       
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    firstset.len()
AttributeError: 'set' object has no attribute 'len'
>>> firstset(len('firstset'))
...       
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    firstset(len('firstset'))
TypeError: 'set' object is not callable
>>> print(len(firstset))
...       
2

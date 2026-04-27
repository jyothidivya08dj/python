Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=7
b=5
print(a&b)
5
print(a^b)
2
print(a|b)
7
print(~a)
-8
print(a<<b)
224
print(a>>b)
0
print(a>>2)
1
print(a<<2)
28
a>b
True
a=5
b=8
c=5
print(a is c)
True
print(a is b)
False
print(a in c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(a in c)
TypeError: argument of type 'int' is not iterable
>>> a=[1,2,3,4]
>>> b=[2,3,4,5]
>>> print(1 in a)
True
>>> print(1 in b)
False
>>> print(3 in b)
True
>>> print(6 not in a)
True
>>> print(1 not in a)
False
>>> print(5 in a)
False
>>> a=4
>>> b=6
>>> print(a is 4)
True
>>> print(a is not 6)
True
>>> print(a is 7)
False
>>> print(b is not 6y)
SyntaxError: invalid decimal literal
>>> print( b is not 6)
False
>>> a=8
>>> b=9
>>> c=a
>>> print(a is c)
True
>>> print(b is c)
False

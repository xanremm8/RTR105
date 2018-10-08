Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> a = 35.0
>>> b = 12.50
>>> c = a * b
>>> print(c)
437.5
>>> x=2+3**4/5*6
>>> print(x)
98
>>> iii='hello'+ 'there'
>>> print(iii)
hellothere
>>> iii='hello' + 'there'
>>> print(iii)
hellothere
>>> iii='hello ' + 'there'
>>> print(iii)
hello there
>>> type(iii)
<type 'str'>
>>> type('hello ')
<type 'str'>
>>> type(555)
<type 'int'>
>>> type(-14)
<type 'int'>
>>> type(34832)
<type 'int'>
>>> type(98.6)
<type 'float'>
>>> type(14.0)
<type 'float'>
>>> print(float(111) + 211)
322.0
>>> type(i)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(i)
NameError: name 'i' is not defined
>>> type(iii)\
	   
KeyboardInterrupt
>>> type(iii)
<type 'str'>
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> k=int(f)
>>> print(k)
42
>>> print(12212 / 1213341)
0
>>> print(10 / 2)
5
>>> print (100.00 / 10.00)
10.0
>>> sval = '234'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 123)
357
>>> nam=input('Who are you?')
Who are you?Nas

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Nas' is not defined
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam
= 
input
('Who are you
? ')
 

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    nam
NameError: name 'nam' is not defined
>>> nam=input('Who are you?')
Who are you? print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1
    print('Welcome', nam)
        ^
SyntaxError: invalid syntax
>>> nam=input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam=input('Who are you?') print('Welcome',nam)
SyntaxError: invalid syntax
>>> # comments
>>> a='Enter Hours'
>>> b='Enter Rate'
>>> c=Pay=a*b

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c=Pay=a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> c=a*b

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c=a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> inp= input('Europe floor?')
Europe floor?2
>>> usf=int(inp) + 1
>>> print('US floor', usf)
('US floor', 3)
>>> inp= input('Europe floor?')
Europe floor? 30
>>> print('US floor', usf)
('US floor', 3)
>>> usf=int(inp) + 1
>>> print('US floor', usf)
('US floor', 31)
>>> 

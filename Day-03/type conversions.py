Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=20
>>> float(a)
20.0
>>> str(a)
'20'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> c= 5
>>> c= 5+4j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(5+4j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> str='abcd'
>>> s= 'abcd'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'abcd'
>>> int(str)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'abcd'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'abcd'
>>> list(s)
['a', 'b', 'c', 'd']
>>> tuple(s)
('a', 'b', 'c', 'd')
>>> set(s)
{'b', 'c', 'a', 'd'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(s)
True
>>> l=[1,2,3,4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> str(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    str(l)
TypeError: 'str' object is not callable
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> tuple(5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    tuple(5,6,7,8)
TypeError: tuple expected at most 1 argument, got 4
>>> t=(5,6,7,8)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> str(t)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    str(t)
TypeError: 'str' object is not callable
>>> list(t)
[5, 6, 7, 8]
>>> tuple(t)
(5, 6, 7, 8)
>>> set(t)
{8, 5, 6, 7}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> s={1,3,5,7}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a number, not 'set'
>>> str(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    str(s)
TypeError: 'str' object is not callable
>>> list(s)
[1, 3, 5, 7]
>>> tuple(s)
(1, 3, 5, 7)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> d=[1:2,2:4,3:6]
SyntaxError: invalid syntax
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(d)
NameError: name 'd' is not defined
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(d)
NameError: name 'd' is not defined
>>> str(d)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    str(d)
NameError: name 'd' is not defined
>>> list(d)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list(d)
NameError: name 'd' is not defined
>>> set(d)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    set(d)
NameError: name 'd' is not defined
>>> tuple(d)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tuple(d)
NameError: name 'd' is not defined
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict(d)
NameError: name 'd' is not defined
>>> bool(d)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    bool(d)
NameError: name 'd' is not defined
>>> 
Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count = 10
>>> count
10
>>> a=10
>>> a
10
>>> type(a)
<class 'int'>
>>> price= 99.99
>>> price
99.99
>>> type(price)
<class 'float'>
>>> b=6+4j
>>> b
(6+4j)
>>> type(b)
<class 'complex'>
>>> s=code
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s=code
NameError: name 'code' is not defined
>>> s="code"
>>> s
'code'
>>> type(s)
<class 'str'>
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> l=[1,4,5,8]
>>> l
[1, 4, 5, 8]
>>> type(l)
<class 'list'>
>>> l = [46.56,(1,2)]
>>> type(l)
<class 'list'>
>>> l
[46.56, (1, 2)]
>>> t= ()
>>> t=tuple()
>>> t=(1,2,3,"erty",[1,3,4], {1,2,3}, true, false)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t=(1,2,3,"erty",[1,3,4], {1,2,3}, true, false)
NameError: name 'true' is not defined
>>> t=([1,2,3],"erty",[1,3,4], {1,2,3}, true, false)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t=([1,2,3],"erty",[1,3,4], {1,2,3}, true, false)
NameError: name 'true' is not defined
>>> t=(1,2,3,"erty",[1,3,4], {1,2,3}, True, False)
>>> t
(1, 2, 3, 'erty', [1, 3, 4], {1, 2, 3}, True, False)
>>> type(t)
<class 'tuple'>
>>> s= set()
>>> s={1,2,3,4,"8iytes",25.6,"edgh"}
>>> s
{1, 2, 3, 4, 'edgh', 25.6, '8iytes'}
>>> type(s)
<class 'set'>
>>> s=
SyntaxError: invalid syntax
>>> 


>>> 

>>> 

>>> 

>>> s={1,1,1,1}
>>> s
{1}
>>> s={}
>>> type(s)
<class 'dict'>
>>> s={"name": 'likitha', 'batch'=5, 'course'='PFS'}
SyntaxError: invalid syntax
>>> s={"name": 'likitha', 'batch': 5, 'course'='PFS'}
SyntaxError: invalid syntax
>>> s
{}
>>> status=True
>>> type=(status)
>>> type(status)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    type(status)
TypeError: 'bool' object is not callable
>>> s= False
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    type(s)
TypeError: 'bool' object is not callable
>>> status = None
>>> type(status)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    type(status)
TypeError: 'bool' object is not callable
>>> status = True
>>> s
False
>>> type(status)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    type(status)
TypeError: 'bool' object is not callable
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    type(s)
TypeError: 'bool' object is not callable
>>> s={1,2,3,4,5}
>>> s.remove(3)
>>> s
{1, 2, 4, 5}
>>> s= frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> 
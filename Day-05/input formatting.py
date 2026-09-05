Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #int float str list tuple set dict
>>> x = input()
gduhj
>>> x
'gduhj'
>>> name = input()
likitha
>>> name
'likitha'
>>> name = input(" Enter the name:")
 Enter the name:likitha
>>> name
'likitha'
>>> age = input("Enter the age:")
Enter the age:23
>>> age
'23'
>>> age = int(input("Enter the age:"))
Enter the age:23
>>> age
23
>>> names = input("Enter the names:")
Enter the names:likitha sushma navya
>>> names
'likitha sushma navya'
>>> names.split()
['likitha', 'sushma', 'navya']
>>> names = input("Enter the names:").split()
Enter the names:likitha sushma navya
>>> names
['likitha', 'sushma', 'navya']
>>> names = input("Enter the names:").split()
Enter the names: 1 2 3 4
>>> names
['1', '2', '3', '4']
>>> map(int,names)
<map object at 0x00000268B1212B50>
>>> list(map(int,names))
[1, 2, 3, 4]
>>> values = list(map(int,input().split()))
values
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    values = list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values'
>>> values = list(map(int,input().split()))
1 2 3 4 5 
>>> values
[1, 2, 3, 4, 5]
>>> >>> values = list(map(float,input().split()))
SyntaxError: invalid syntax
>>> values = list(map(float,input().split()))
values
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    values = list(map(float,input().split()))
ValueError: could not convert string to float: 'values'
>>> 1 2 3 4 5
SyntaxError: invalid syntax
>>> values
[1, 2, 3, 4, 5]
>>> names = tuple(input()"Enter the names:").split()
SyntaxError: invalid syntax
>>> names = tuple(input("Enter the names:").split())
Enter the names:likitha sushma navya
>>> names
('likitha', 'sushma', 'navya')
>>> values = tuple(map(float,input().split()))
1 2 3 4 5
>>> values
(1.0, 2.0, 3.0, 4.0, 5.0)
>>> values = set(input().split())
1 2 3 4 5
>>> values
{'5', '1', '2', '4', '3'}
>>> values = set(map(float,input().split()))
5 6 7 8
>>> values
{8.0, 5.0, 6.0, 7.0}
>>> values = set(map(int,input().split()))
5 6 7 8
>>> values
{8, 5, 6, 7}
>>> a,b = [1,2]
>>> a
1
>>> b
2
>>> a,b = (1,2)
>>> a
1
>>> b
2
>>> email,password = input("Enter the email and password:").split()
Enter the email and password:likithamini@gmail.com 1234
>>> email
'likithamini@gmail.com'
>>> password
'1234'
>>> a,b,c = list(map(int,input().split()))
4 5 6
>>> a
4
>>> b
5
>>> c
6
>>> name,marks = input().split()
likitha 60
>>> name
'likitha'
>>> marks
'60'
>>> int(marks)
60
>>> nmae,age = input().split()
name,age = input().split()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    nmae,age = input().split()
ValueError: too many values to unpack (expected 2)
>>> name,age = input().split()
sushma 87
>>> name
'sushma'
>>> age
'87'
>>> int(age)
87
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 
>>> e = eval(input())
2
>>> e
2
>>> e = eval(input())
134.78
>>> e
134.78
>>> e = eval(input())
likitha
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'likitha' is not defined
>>> e = eval(input())
"likitha"
>>> e
'likitha'
>>> e = eval(input())
[1,2,3,4]
>>> e
[1, 2, 3, 4]
>>> e = eval(input())
(5,6,7,8)
>>> e
(5, 6, 7, 8)
>>> e = eval(input())
{1:1,2:2,3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> 
#sys module

import sys

#print(sys.path)
#print(sys.version)
print("start")
sys.exit()
print("end")

#platform module

import platform

print(platform.system())
print(platform.release())
print(platform.processor())

#math module

import math

print(math.pi)
print(math.e)

print(math.sqrt(49))
print(math.pow(3,4))

print(math.ceil(13.0004))
print(math.ceil(13.02))
print(math.ceil(13.546))

print(math.floor(13.0004))
print(math.floor(13.56))
print(math.floor(13.78))

print(math.fabs(-8))
print(math.factorial(6))
print(math.gcd(8,32))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.degrees(30))
print(math.radians(60))

#random module

import random

#random.seed(5)

print(random.radint(1,10))
print(random.radint(100000,999999))
print(random.random())
print(random.uniform(1,5))

l = ['R','P','S']
print(random.choice(l))
print(random.choices(l))

random.shuffle
print(l)

#collections module

from collections import Counter

s = 'python programming'
m = 'this is that that is this is is'.split()
l = [1,1,1,1,2,3,4,5,664,6,6,67,6,67,67,88,8,97,68,86,6]

print(Counter(s))
print(Counter(m))
print(Counter(l))

#default dict

from collections import Counter, defaultdict

s = 'python programming'
m = 'this is that that is this is is'.split()
l = [1,1,1,1,2,3,4,5,664,6,6,67,6,67,67,88,8,97,68,86,6]

d = defaultdict(int)
for i in s:
    d[i]+=1

print(d)   

#deque

from collections import deque

l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()

print(l)

#reverse

from collections import deque

l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()

print(l)

#iter tools

from itertools import combinations,permutations

res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))

print(res1)
print(res2)

#converting into string

from itertools import combinations,permutations

res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])






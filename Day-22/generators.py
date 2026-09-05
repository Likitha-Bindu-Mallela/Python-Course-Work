 #generators - executing one by one using yield keyword


def retrivedata():
    data =['1..100','10..200','201..300','301..400','401..500']
    for i in data:
        yield i

reels = retrivedata()

while True:
    status = input("[s]croll or [q]uit: ")
    if status == 's':
        print(next(reels))
    else:
        break


# even numbers

def even():
    i = 0
    while True:
        i+=2
        yield i

n = 15
res = even()
for i in range(n):
    print(next(res))

#factors of a number

def factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            yield i 

n = 19
res = factors(n)
for i in res:
    print(i)


#prime numbers

def isprime(n):
    for j in range(2,n//2+1):
        if n%j== 0:
            return False
    return True 

def isprime(n):
    for i in range(2,n//2+1):
        if isprime(i):
            yield i

S
res = isprime(n)
for i in res:
    print(i)     


def isprimes(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes(n):
    for i in range(2, n + 1):
        if isprimes(i):
            yield i

n = 15
res = primes(n)

for i in res:
    print(i)


                


    

                 



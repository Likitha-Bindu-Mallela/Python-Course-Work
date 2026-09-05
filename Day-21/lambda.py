#lambda function - shorter logic in a single line

greater = lambda a,b: a if a>b else b

print(greater(17,90))
print(greater(56,35))
print(greater(54,45))
print(greater(49,20))


wish = lambda name: f'Welcome to the course: {name}'

print(wish("Likitha"))
print(wish("Sushma"))
print(wish("Chandu"))

iseven = lambda n: "Even" if n%2==0 else "Odd"

print(iseven(56))
print(iseven(23))
print(iseven(28))


avg = lambda a,b,c : (a+b+c)/3

print(avg(61,24,29))
print(avg(17,19,21))


#email as  input and domain as output

domain = lambda mail: (mail.split('@')[-1]).split('.')[0]

print(domain('likitha@codegnan.com'))
print(domain('likitha@outlook.com'))
print(domain('likitha@yahoo.com'))
print(domain('likitha@gmail.com'))

#price as input price + tax  as output

gst = lambda price: price + price*0.18

print(gst(2000))
print(gst(5000))
print(gst(9000))

#using a function // taking a list of prices - adding gst 
#map function  -  used to update a list

prices = [2437,653,784,878,986,8327,4763]

res = list(map(lambda price: price + price*0.18, prices))

print(res)


#list of names convert into titles

names = ['likitha', 'sushma', 'chandu','pallavi','harsha','dedeepya']

res = list(map(lambda name: name.title(),names))

print(res)



prices = [4637,7467,9747,8749,9744,8457]

res = list(map(lambda price: price - price*0.3, prices))

print(res)

#filter function

prices = [4637,7467,9747,8749,9744,8457]

res = list(filter(lambda price: price >8000, prices))

print(res)

prices = [2346,3458,4560,5678,6782]

res = list(filter(lambda price: price%2==0 , prices))

print(res)


prices = [4637,7467,9747,8749,560,5678]

res = list(filter(lambda price: price%2!=0 , prices))

print(res)

names = ['likitha','chandu','pallavi','dedeepya', 'harsha']

res = list(filter(lambda name: len(name)>5,names))

print(res)

#reduce function - reduce into a single unit

from functools import reduce



products = {'sugar':45,
            'salt':30,
            'eggs':60,
            'cooking oil':90,
            'bread':50
            }

print(dict(sorted(products.items())))

print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(),key= lambda i:i[1])))

print(dict(sorted(products.items(),key= lambda i:i[1],reverse=True)))





 









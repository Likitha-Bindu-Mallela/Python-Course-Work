#list comprehension - executed the code in a single line    updation-iteration-declaration

#printing 1 to 10 numbers

res = [i for i in range(1,11)]
print(res)

#factors a number

n = 12
res = [i for i in range(1,n + 1) if n%i==0]
print(res)

#even numbers

r = [27,746,874,87,98,54]
res = [i if i%2==0 else 0 for i in r]
print(res)

#even numbers - append and odd numbers - 0

r = [[14,56,45],[39,47,32],[76,49,69]]
res = [j for i in r for j in i if j%2==0]
print(res)


#set comprehension -  iterating or adding 

res = {i for i in range(1,11)}
print(res)

#factors a number

n = 12
res = {i for i in range(1,n + 1) if n%i==0}
print(res)

#even numbers

r = {27,746,874,87,98,54}
res = {i if i%2==0 else 0 for i in r}
print(res)

#even numbers - append and odd numbers - 0

r = [[14,56,45],[39,47,32],[76,49,69]]
res = {j for i in r for j in i if j%2==0}
print(res)

#syntax of list comp

#l = [updating for loop]
#l = [updating for loop if cond]
#l = [upd1 if cond else upd2 for loop]
#l = [upd for loop1 for loop2]
#l = [upd for loop1 for loop2 if cond]

l = [int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)


names = [input(f"Enter the name - {i+1}: ") for i in range(5)]
print(names)


#dict comp

names = {input(f"Enter the name - {i+1}: "):int(input("Enter the marks: ")) for i in range(5)}
print(names)

#squares of numbers

result = {i:i*i for i in range(1,11)}
print(result)




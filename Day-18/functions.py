 #function is a reusable block of code designed to perform a specific task.

#user Details
def display(name,email,password):
    print(f'Hello Name',{name})
    print(f'Your email', {email})
    print(f'Password',{password})

display('likitha','likitha@123','likitha@1')    
display('sushma','sushma@123','sushma@1') 
display('chandu','chandu@123','chandu@1') 

#Leap Year
def isleapyear(year):
    if year%400 ==0 or (year%4==0 and year%100!=0):
        print(f"{year}is a  leap year")
    else:
         print(f"{year}is not  leap year")

for year in range(2001,2028):
    isleapyear(year)      


#Sum of Digits
def sumofdigits(n):
    sum =0 
    while(n>0):
        sum += n%10
        n=n//10
    return sum

n = int(input("Enter the number: "))
print(f'sum of {n} digits is {sumofdigits(n)}')

#Product of Digits
def productofdigits(n):
    product = 1
    while(n>0):
        product *=n%10
        n=n//10
    return product

n = int(input("Enter the number: "))
print(f'product of {n} digits is {productofdigits(n)}')  

#Strong Password
def checkpassword(password):
    if len(password) >8:
        check = set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                 check.add('l')
            elif i.isdigit():
                 check.add('d')
            else:
                check.add('s')
        if len(check) ==4:
            return("Strong Password")
        return "Weak Passowrd"
    
password = input("Enter the password: ") 
print(f'Password is {checkpassword(password)}')



#Multiplication Table

def table(n):
    print(f'---------Table - {n}-------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,38):
    table(i)        





           



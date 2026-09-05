#recursion - function calling itself until base condition is satisfied/// how to start ,condition, when to update.

#recursion syntax:

'''def func(argv):
    if base_con:
        return
    func(updating argv)'''

'''func(para)'''

def display(n):
    if n>10:
         return
    print(n)
    display(n+1)
    

display(1)  

def display(n):
    if n>10:
         return
    
    display(n+1)
    print(n)
    

display(1)

#sum of n numbers

def displaysum(n):
     if n==0:
          return 0
     return n+displaysum(n-1)

print(displaysum(10))


#product of n numbers

def productofn(n):
     if n==1:
          return 1
     return n*productofn(n-1)

print(productofn(4)) 


#finding index 

def display(ind):
     if ind == len(s):
          return
     print(s[ind],end='')
     display(ind+1)

s = "Python Programming"
display(0)          


 #reverse of index   

def display(ind):
     if ind == len(s):
          return
     
     display(ind+1)
     print(s[ind],end='')

s = "Python Programming"
display(0) 


#sequence of a string

def display(n):
     if n > len(s):
          return
     print(s[:n])
     display(n+1)

s= "Python Programming"
display(1)  



def display(ind,w):
     if ind > len(s)-w:
          return
     print(s[ind:ind+w])
     display(ind+1,w)

s="Python Programming"
display(0,5)    


def display(n):
     if n==0:
          return
     display(n//10)
     print(n%10)
     
n = 56789
display(n)


#sum of digits

def display(n):
     if n==0:
          return
     print (n %10 + display(n//10))
     
n = 56789
print(display(n))     


#fibonacci series

a=0
b=1

n=10
for n in range(n-1):
     a,b=b,a-b
     print(b)












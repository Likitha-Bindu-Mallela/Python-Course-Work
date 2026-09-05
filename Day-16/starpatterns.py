n = int(input("Enter the size: "))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()    

n = int(input("Enter the size: "))
for i in range(n):
    for sp in range(n-i-1):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end =' ')
    print()           



n = int(input("Enter the size: "))
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()    



n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()            



n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2):
            print('*', end=' ')
        else:
             print(' ', end=' ')   
    print()       


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print('*', end=' ')
        else: 
            print(' ', end=' ')
    print()                 


n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==2 ):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()      


n= int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==2 or i==4):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print() 


n= int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()    


n= int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==4 or j==4):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()      




n= int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or i==n-2):
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print() 


n= int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0): 
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()    


n= int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if (i==j) and (j=n-i-1) and n//2):
            print('*',end=' ')
        else:
            print(' ', end=' ')    
    print()  

    n=7
    for i in range(n):


for i in range(n):
    for j in range(n):
        if (j == 0 or j == n-1 or
            (i == j and i <= n//2) or
            (i+j == n-1 and i <= n//2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= n//2) or (i+j == n-1 and i <= n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
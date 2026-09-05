#scope - local and global variables are present

#global variable - variable can access anywhere // outside 

#local variable - inside the function accessed 

def display(n):
    n=n+10
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)


def display():
    print('Inside:',n)

n=20
display()
print('Outside:',n)

def display():
    n=10
    print('Inside:',n)

display()  

def display():
    global n
    n=n+10
    print('Inside:',n)

n=10
display()
print('Outside:',n)   


def display(n):
    
    n='PFS'
    print('Updated Course:',n)


n = 'PFS'
display(n)
print('Final Course:',n) 



def display():
    n = 'JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated Course:",n)
    update()
    print("Final Course:",n)


display()       

#declaring a built in function 

display()

l= [1,2,3,4,5]
max=20
sum=10
print(sum)


    

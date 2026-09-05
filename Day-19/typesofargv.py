#types - keyword, variable length, positional , default

#positional arg - mapping depends on the position

def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password: {password}')

display('abc','abc@gmail.com', 'abc_123')    
display('abc@gmail.com','abc_123','abc')
display('abc_123','abc','abc@gmail.com')


#keyword arg - depends on the keywords

def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password: {password}')

display(name='abc',email='abc@gmail.com', password='abc_123')    
display(email='abc@gmail.com',password='abc_123',name='abc')
display(password='abc_123',name='abc',email='abc@gmail.com')

#default arg - setting a default value for a  parameter // always should be end of the args

def display(name,email= 'gmail.com',password=' '):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password: {password}')

display('abc','abc@gmail.com', 'abc_123')    
display('abc@gmail.com','abc_123')
display('abc_123')




def display(*names):
    print(names)

display('likitha')
display('likitha', 'chandu')
display('likitha', 'chandu', 'dedeepya')
display('likitha','chandu','dedeepya','pallavi') 

def display(**products):
    print(products)

display(bag=2000)
display(bag=4000,book=20)
display(bag=2500,book= 50,bottle=60)






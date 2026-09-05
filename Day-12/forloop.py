#str list tuple set dict range()
'''
for var in seq:
    print(var)
'''

s = "Codegyan"
for ch in s:
    print(ch)


'''
l = [12,13,17,24,26,2,6,19,20]
for i in l:
    ifi%2==0:
       print(i,"Even")
else:
       print(i,"Odd")


'''

marks = (56,46,37,83,63,92)
for mark in marks:
    if mark>35:
        print(mark,"Pass")
    else:
        print(mark,"Fail")    



followers = {"Likitha", "Navya","Sushma","Chiruhaasa","Pravallika"}
for i in followers:
    print(i)


bus = {'s1':"Available", 's2':"Booked",'s3':"Available",'s4':"Booked",'s5':"Available"}
for seat in bus:
    if bus.get(seat)!= "Available":
        print(seat,bus.get(seat)) 


#range(start,end+1,step) => (0,nodef,1)

for i in range(1,11):
    print(i)


for i in range(2,51,2):
    print(i,end=' ')


for i in range(1,100,2):
    print(i,end=' ')


for i in range(5,51,5):
    print(i,end=' ')


n = int(input("Enter the table no:"))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')    
'''print('1'+ 1)
print(10/0)
l= [24,56]
print(l[10])

k={1:12,2:13}
print(k[3])

try:
    a = int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of a Program")''' 


'''try:
    a = int(input())
    k={1:12,2:13}
    #print(k[14])
    l = [23,456]
    #print(l[10])
    #print(10/0)
    #print('1',1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("Key is not there") 
except IndexError:
    print("Index is out of range")
except ZeroDivisionError:
    print("Can't divide with zero")
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("define the variable")                   
else:
    print("a=",a)
finally:
    print("End of a Program") '''         


'''try:
    a = int(input())
    k={1:12,2:13}
    #print(k[14])
    l = [23,456]
    #print(l[10])
    #print(10/0)
    #print('1',1)
except (ValueError, KeyError, IndexError, ZeroDivisionError, TypeError, NameError) as e:
    print("Error occured:",e)
else:
    print("Print error free program")
    
finally:
    print("End of a Program") 


try:
    a = int(input())
    k={1:12,2:13}
    #print(k[14])
    l = [23,456]
    #print(l[10])
    #print(10/0)
    #print('1',1)
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")    

finally:
    print("End of a Program")'''    


try:
    amount = int(input("Enter the account: "))  
    balance = 4000
    if amount < 0:
     raise Exception("Amount needs should be positive")
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")    

finally:
    print("End of a Program")        




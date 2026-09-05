fa = eval(input("Follows Account: "))
cf = eval(input("Close Friends: "))

if fa:
    if cf:
        print("Story Visisble")
    else:
        print("Not in Close Friends List")

else:
    print("Follow the Account First")            


register = eval(input( "registered: "))

if reg:
    fee = eval(input("Entry Fee: " ))
    if fee:
        print("Tournament Entry Confirmed ")
else:
    print(" Entry fee is pending")
else:
    print("Registration Required")



file = eval(input("File Link is Active: "))
if file:
    permission = eval(input("Granted"))
    if file active:
        print("Active")
    else:
        print("File Opening Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")                
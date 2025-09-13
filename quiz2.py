x = int (input("select a number: "))
y = int (input("select another number: "))
z = input ("which operation do you want to perform. seclect from *, /, + or -: ")

if z == "*":
    print (x * y)
elif z == "/":
    if y == 0:
        print ("Zero cant be the denominator")
    else:
        print (x/y)
elif z=="+":
    print (x+y)
elif z=="-":
    print (x-y)
else:
    print ("enter a valid operator")

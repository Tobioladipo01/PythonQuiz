shoppinglist = []
while True: 
    userinput = input ("do you want to view, add or remove from the current list? or do you want to quit this page? ").lower().strip()
    if userinput == "view":
        print (shoppinglist)
    elif userinput == "add":
        useritems = input ("Add an item to the list:")
        shoppinglist.append(useritems)
        print(shoppinglist)
    elif userinput == "remove":
        userremove = input ("what item do you want to remove? ")
        shoppinglist.remove(userremove)
        print(shoppinglist)
    elif userinput == "quit":
        print ("Thank you for using our software. Hope to see you next time")
        break
    else:
        print("enter a valid prompt")
    
    

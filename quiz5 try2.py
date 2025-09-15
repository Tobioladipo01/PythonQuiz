shoppinglist = []
while True: 
    userinput = input ("do you want to view, add or remove from the current list? or do you want to quit this page? ").lower().strip()
    if userinput == "view":
        print ("shoppinglist: ")
        for x in shoppinglist:
            print(X)
    elif userinput == "add":
        useritems = input ("Add an item to the list:")
        shoppinglist.append(useritems)
        print(f"{useritems} added to the list")
    elif userinput == "remove":
        userremove = input ("what item do you want to remove? ")
        shoppinglist.remove(userremove)
        print(shoppinglist)
    elif userinput == "quit":
        print ("Thank you for using our software. Hope to see you next time")
        break
    else:
        print("enter a valid prompt")
    
    

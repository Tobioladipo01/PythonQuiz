
tasks = []
while True:
    print ("----To do list menu-----")
    print ("1. View Tasks")
    print ("2. Add Tasks")
    print ("3. Remove tasks")
    print ("4. Exit")

    userinput = input ("What would you like to do today? select from the options above: ")
    if userinput == "1":
        if len(tasks) == 0:
           print ("nothing added yet. add a task to the list")
        else:
            print ("--Here are the items on your list--")
            for task in tasks:
                print (task)
           
    elif userinput == "2":
        while True:
            wantto = input ("What tasks will you like to add? type none if you are done ")
            tasks.append(wantto)
            print (f"you have successfully added {wantto} to the list")
            if wantto == "none":
                break
    elif userinput == "3":
        donetasks = input ("What tasks have you completed? ")
        if donetasks in tasks: 
            tasks.remove(donetasks)
            print (f"you have succesfully removed {donetasks}")
        else:
            print("enter a valid task")
    elif userinput == "4":
        break
    else:
        print ("choose a valid option")
    
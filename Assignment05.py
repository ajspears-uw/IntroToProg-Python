# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Amanda Spears,05/11/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Captures the task input
strPriority = "" # Captures the Priority input


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(objFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Item":lstRow[0].strip(), "Priority":lstRow[1].strip()}
    lstTable.append(dicRow)


#objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("\n--- Current items in ToDo List are:")
        for dicRow in lstTable:
            print(dicRow["Item"], ", ", dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str.lower(input("\tEnter the name of your item: "))
        strPriority = str.lower(input("\tEnter the priority of your item: "))
        dicRow = {"Item":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        print("\n--- Current items in ToDo List are:")
        for dicRow in lstTable:
            print(dicRow)
        continue
    # # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItemtoRemove = input("Which task item would you like to remove? ")
        intItemtoRemove = False
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if(strItemtoRemove == str(list(dict(lstTable[intRowNumber]).values())[0])): #create the list of values
                del lstTable[intRowNumber]
                intItemtoRemove = True
            intRowNumber += 1 #end if (and end for loop)
        if(intItemtoRemove == True):
            print("The task was successfully removed.")
        else:
            print("I'm sorry, I was unable to find that task.")
        continue
    # # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Item"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        input("Your data was saved successfully!  Press Enter to return to the main menu.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: no additional code necessary for the break portion.  Just new code after if an inappropriate selection is made.
        break  # and Exit the program
    else:
        print('You have entered an incorrect option. Please choose 1 through 5')

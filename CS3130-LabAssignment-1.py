"""
Timothy Queva
CS3130 Lab1
January 19, 2021

This program reads a CSV file into a unordered map for the purpose of
databasing. User presented with database manipulation options which of
themselves may give a submenu. Submenu functions imported from another
file.
"""

import time
import submenu

#Test case: db ={'5': 'Bob:Barker:Sci','2': 'Sally:Coffin:Research'}
#db.values()

db = {}
opt = 0

#This will import .csv file into in-program database
with open('Test.csv',encoding = "ISO-8859-1") as data:
        for elemnt in data:
            elemnt  = elemnt.strip()    #This by itself strips '\n' from line
            elemnt = elemnt.split(',')
            db[elemnt[0]] = ":".join(elemnt[1:])

#This strips 'schema' from the csv file if it has one
if 'ID' in db:
    del db['ID']

#Interface
print("Welcome to Employee FMS\n")
while opt != 5:
    print("Please select one of the following options:")
    print("    1) Add new employee")
    print("    2) Search for an employee")
    print("    3) Remove an employee from FMS")
    print("    4) Display entire employee FMS")
    print("    5) Exit")
    print() #for ubuntu
    
    #This dals with user input and associated exception handling
    try:
        opt = int(input("Choice #? : "))
        if(opt < 1 or opt > 5):
            print("\nERROR: Please enter a valid option\n")
            time.sleep(2)
            continue
    except ValueError:
        print("\nERROR: Please enter a valid number")
        time.sleep(2)
        continue

    #This will deals with user selected options
    if opt == 1:
        submenu.add(db)
    elif opt == 2:
        submenu.display(db)
    elif opt == 3:
        submenu.rm(db)
    elif opt == 4:
        submenu.displayall(db)

#This code below uploads internal database back into csv file
with open('Test.csv','w',encoding = "ISO-8859-1") as data:
    data.write("ID,FNAME,LNAME,DEPT\n")
    for elemnt in db:
        #Writes the key
        data.write(str(elemnt) + ",")
        
        #transforms second part of tuple into strinig, processes, and writes
        tmp = str(db[elemnt])
        tmp = tmp.split(":")
        tmp = ",".join(tmp)
        data.write(tmp)
        data.write('\n')

print("Thank you. Have a good day!")
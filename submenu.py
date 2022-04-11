"""
Timothy Queva
CS3130 Lab1
January 19, 2021

This file holds the functions necessary for the operation of the submenu
in CS3130 LabAssigment1.py
"""

import time

def add(db):
    again = True
    while again:
        recrd = input("Please enter below employee id, first name, last name, " +
                      "and department in this order separated by one space: ")
        
        #allows exiting if one does not wish to add to database
        if str(recrd) == "exit":
            print("Exiting to main menu...\n")
            time.sleep(1)
            break
        
        #processes input
        recrd = recrd.split(' ')
        
        #psuedo-exception handling for incorrect inputs
        if len(recrd) < 4 or len(recrd) > 4:
            print("Incorrect input: Please enter all details as specified.")
            print() #for ubuntu
            continue
        try:
            int(recrd[0])
        except:
             print("Employee ID is incorrect. Please enter numbers only.")
             continue
        '''
        Some people have unique names which may not be alphanumeric.
        Therefore, no control was implemented for this. Also, a department
        may be numbered or have a number-no control implemented.
        '''
        
        #checks database if record already exists and adds if not
        nfound = True
        for key in db.keys():
            if key == recrd[0]:
                nfound = False
                break
        if nfound:
            db[recrd[0]] = ":".join(recrd[1:])
            print("\nRecord (" + recrd[0] + ":" + db[recrd[0]] + ") added " +
                  "to database")
            print() #for ubuntu
        else:
            print("Sorry: A record already exists for this employee.")
            print() #for ubuntu
        
        #Control for loop/exit to main menu
        while True:
            again = input("Enter another record? (Y/n): ")
            again = again.lower()
            if again == "n":
                print("Exiting to main menu...\n")
                time.sleep(1)
                again = False
                break
            elif again == "y":
                again = True
                break
            else:
                print("Sorry, your response was not recognized.")
                print() #for ubuntu

#Displays database record
def display(db):
    again = True
    while again:
        try:
            #str --> int --> str ensures only # are entered
            found = False
            recrd = int(input("Which employee do you wish to find? ID #: "))
            recrd = str(recrd)
            for key in db.keys():
                if recrd == key:
                    tmp = db[recrd].split(':')
                    print("Employee ID: " + recrd)
                    print("First name : " + tmp[0])
                    print("Last name  : " + tmp[1])
                    print("Department : " + tmp[2])
                    print() #for ubuntu
                    found = True
                    break
            if not found:
                print("Sorry, requested employee could not be found in the " +
                      "database.")
        except ValueError:
            print("Please enter employee ID numbers only")
        
        #Control for loop/exit to main menu
        while True:
            again = input("Search another employee? (Y/n): ")
            again = again.lower()
            if again == "n":
                print("Exiting to main menu...\n")
                print() #for ubuntu
                time.sleep(1)
                again = False
                break
            elif again == "y":
                print() #for ubuntu
                again = True
                break
            else:
                print("Sorry, your response was not recognized.")
                print() #for ubuntu

#rm removes a database entry from the database
def rm(db):
    again = True
    while again:
        try:
            found = False
            recrd = input("Which employee do you wish to remove? ID #: ")
            
            #allows exiting if one does not wish to remove record from database
            if recrd == "exit":
                print("Exiting to main menu...\n")
                time.sleep(1)
                break
            
            #checks input to make sure it is an integer
            recrd = int(recrd)
            recrd = str(recrd)
            
            #searches for record. If found, confirm? deletion:abort
            for key in db.keys():
                if recrd == key:
                    print("\nThe following record will be deleted:")
                    tmp = db[recrd].split(':')
                    print("Employee ID: " + recrd)
                    print("First name : " + tmp[0])
                    print("Last name  : " + tmp[1])
                    print("Department : " + tmp[2])
                    print() #for ubuntu
                    
                    #this part confirms deletion
                    while True:
                        response = input("PROCEED? (Y/n): ")
                        response = response.lower()
                        if response == "y":
                            del db[recrd]
                            print("Record has been deleted.")
                            print() #for ubuntu
                            break
                        elif response == "n":
                            print("Deletion operation aborted.")
                            break
                        else:
                            print("Sorry, your response was not recognized")
                    
                    found = True
                    break
            if not found:
                print("Sorry, requested employee could not be found in the " +
                      "database.")
                print() #for ubuntu
            found = False
        except ValueError:
            print("Please enter employee ID numbers only")
            print() #for ubuntu
            continue
        
        #Control for loop/exit to main menu
        while True:
            again = input("Delete another record? (Y/n): ")
            again = again.lower()
            if again == "n":
                print("Exiting to main menu...\n")
                time.sleep(1)
                again = False
                break
            elif again == "y":
                again = True
                break
            else:
                print("Sorry, your response was not recognized.")

#displays all records in database
def displayall(db):
    print("Employee ID     First Name     Last Name     Department")
    for recrd in db:
        tmp = db[recrd].split(':')
        print('{:<16}'.format(recrd) + '{:<15}'.format(tmp[0]) +
              '{:<14}'.format(tmp[1]) + tmp[2])
    print()
    
#Prevents code execution if file run as stand-alone program
if __name__ == "__main__":
    print("Sorry, this code is not meant to be used as a stand-alone " +
          "program. Please import code in order to use it. Thank you.")
    
    '''Test Cases:
    db ={'5': 'Bob:Barker:Sci','2': 'Sally:Coffin:Research'}
    add(db)
    display(db)
    rm(db)
    displayall(db)
    '''
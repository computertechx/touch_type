'''
A typiny tutor/traininy
progran, no install,
 copy, paste and run(CLI)
VERSION 1.0 ALPHA
'''
# REQUIRED IMPORTS
import os
import random

#DECLARE AND ASSIGN VARIABLE
choice = 0
subChoice = 0
menuItems = [["Letter Drill","Sentence Drill","Quit"],["Drill 1","Drill 2","Drill 3","Back"]]


# CORE FUNCTIONS
def clear():
    os.system("clear")

def invalidOption():
    print("Invalid option")
    input("press Enter to continue ")

def menu(items,num):
    print("Please select an option:")
    i=1
    menuLs = items[num]
    for item in menuLs:
        print(" *"+item+" "*(15-len(item))+"[ "+str(i)+" ]")
        i += 1
    selected = input(" Enter choice: ")
    return selected

# MAIN PROGRAN LOOP

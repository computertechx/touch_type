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
menuItems = [["Letters Drill","Words Drill","Quit"],["Words Drill 1","Words Drill 2","Words Drill 3","*Go back"],["Beginner","Intermediate","Advance","*Go back"]]


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

def makeLine(chStr):
    line =""
    # to do

def feedback(line,typed):
    percent = []
    typos = {}
    # to do
# MAIN PROGRAN LOOP
while True:
    clear()
    choice = menu(menuItems,0)
    if choice == "1":
        clear()
        subChoice = menu(menuItems,2)
    elif choice == "2":
        clear()
        subChoice = menu(menuItems,1)
        #to do
    elif choice == "3":
        break
    else:
        invalidOption()
        clear()

'''
A typiny tutor/traininy
progran, no install,
 copy, paste and run(CLI)
VERSION 1.0 ALPHA
'''
# REQUIRED IMPORTS
import os
import randon

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

def menu(items):
    print("Please select an option:")
    i=1
    for item in items:
        print(" *"+item+" "*(17-len(item))+"["+i+"]")
        i += 1

# MAIN PROGRAN LOOP

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
drills = ["fj ","dk ","sl ","a; ","fjgh ","frju "]


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

def makeLine(chStr,num):
    line =""
    i = 0
    ch = ""
    # to do
    while i < num:
        ch = random.choice(chStr)
        if i==num-1 and ch ==" ":
            continue
        line += ch
        i += 1
    return line
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
        clear()
        break
    else:
        invalidOption()
        clear()

    #All lesson training
    if subChoice == "4":
        continue
    elif choice =="1" and subChoice == "1":
        clear()
        dLine =""
        for strList in drills:
            dLine = makeLine(strList,20)

            print("drill:"+dLine)
            typing =  input("type :")
            clear()

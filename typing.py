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
drills = ["fj","dk","sl","a;","fjgh","frju"]
accuracyPerLine=[]
wrongLetters = ""
abc = "abcdef ghijklmnop qrstuvwxyz"
lineWidth = 20

# CORE FUNCTIONS
def clear():
    os.system("clear")
def pauseScr():
    input("press enter to continue...")
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
    percent = 0
    typos = ""
    i = 0
    count = len(typed)
    correct = 0
    if len(line) < len(typed):
        count = len(line)
    while i < count:
        if line[i] == typed[i]:
            correct += 1
        else:
            typos += line[i]
        i += 1
    if correct > 0:
        percent = round((correct/count)*100)
    return percent, typos

def printReport(percentList,strWrongL):
    mistyped = {}
    print("Accuracy percent per line:")
    print(percentList)
    print("\n\nLetters mistyped:")
    for ch in strWrongL:
        if ch in mistyped:
            mistyped[ch] += 1
        else:
            mistyped[ch] = 1
    print(mistyped)
    print()

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
    elif choice == "1" and subChoice == "3":
        dLine = ""
        i = 0
        while i < 9:
            clear()
            dLine = makeLine(abc + abc.upper() + " ",lineWidth)
            print("drill:"+dLine)
            typing = input("type :")
            percent,mistakes = feedback(dLine,typing)
            accuracyPerLine.append(percent)
            wrongLetters += mistakes
            i += 1
        printReport(accuracyPerLine,wrongLetters)
        # to do yes/no mistake drill
        pauseScr()
        accuracyPerLine = []
        wrongLetters = ""
    elif choice == "1":
        clear()
        dLine =""
        for strCh in drills:
            if subChoice == "1":
                dLine = makeLine(strCh + " ",lineWidth)
            elif subChoice == "2":
                dLine = makeLine(strCh + strCh.upper() + " ",lineWidth)
            print("drill:"+dLine)
            typing =  input("type :")
            clear()
            linePercent,mistakes = feedback(dLine,typing)
            accuracyPerLine.append(linePercent)
            wrongLetters += mistakes
        printReport(accuracyPerLine,wrongLetters)
        #to do yes/no mistakes drill
        pauseScr()
        accuracyPerLine =[]
        wrongLetters =""


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
wrongWords = ""
abc = "abcdef ghijklmnop qrstuvwxyz"
lineWidth = 20

# CORE FUNCTIONS
def clear():
    os.system("clear")
def pauseScr():
    input("press Enter to continue")
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
    #  loop and create str
    while i < num:
        ch = random.choice(chStr)
        if i==num-1 and ch ==" ":
            continue
        line += ch
        i += 1
    return line
def wordFeedback(line,typed):
    words = line.split(" ")
    typedWords = typed.split(" ")
    percent = 0
    missedWords =""
    correct = 0
    count = len(words)
    i = 0
    if len(typedWords) < len(words):
        count = len(typedWords)
    while i < count:
        if words[i] == typedWords[i]:
            correct += 1
        else:
            missedWords += words[i] + " "
        i += 1
    if typed == "":
        percent = 0
    elif not correct == 0:
        percent = round((correct/count)*100)
    return percent,missedWords
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
    if not mistyped == {} :
        i = 0
        mistypedF = ""
        for mTyped in mistyped:
            mistypedF += ("[" + str(mTyped) + ":"+ str(mistyped[mTyped]) +"] ")
            i += 1
            if i%4 == 0:
                mistypedF += "\n"
        print(mistypedF + "\n")
    else:
        print("[ no mistyped letters ]\n  return to nain menu")
        pauseScr()

# impure funtion
def mistypedDrill(strCh,num):
    n = 5
    yesNo = "1"
    if yesNo == input("Practice on mistyped letters\n yes:[ 1 ] no:[ 2 ]:"):
        print()
        try:
            n = int(input("How many lines: "))
        except:
            print("Not a valid, will use default(5)")
            n = 5
        for i in range(n):
            clear()
            dLine = makeLine(strCh,num)
            print("drill: "+dLine)
            typing = input("typed: ")
            percent,mistakes = feedback(dLine,typing)
            print(str(percent)+"% accurate")
            pauseScr()
        clear()
        print("Drill completed, return to main menu")
        pauseScr()

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
            print("drill: "+dLine)
            typing = input("typed: ")
            percent,mistakes = feedback(dLine,typing)
            accuracyPerLine.append(percent)
            wrongLetters += mistakes
            i += 1
        printReport(accuracyPerLine,wrongLetters)
        if not wrongLetters == "":
            mistypedDrill(wrongLetters + " ",lineWidth)
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
            print("drill: "+dLine)
            typing =  input("typed: ")
            clear()
            linePercent,mistakes = feedback(dLine,typing)
            accuracyPerLine.append(linePercent)
            wrongLetters += mistakes
        printReport(accuracyPerLine,wrongLetters)
        if not wrongLetters == "":
            mistypedDrill(wrongLetters + " ",lineWidth)
        accuracyPerLine =[]
        wrongLetters =""
    elif choice == "2":
        clear()
        filePath = ""
        if subChoice == "1":
            filePath = "./word_drill_1.txt"
        elif subChoice == "2":
            filePath = "./word_drill_2.txt"
        elif subChoice == "3":
            filePath = "./word_drill_3.txt"
        with open(filePath) as dFile:
            for dLine in dFile.readlines():
                print("drill: " + dLine)
                typing = input("typed: ")
                percent,missedWords = wordFeedback(dLine,typing)
                accuracyPerLine.append(percent)
                wrongWords += missedWords
                print("\n"+str(percent)+"% words matched")
                pauseScr()
                clear()
                #to do implement a wordChk feedback
            print("Drill completed, return to main menu")
            pauseScr()
            dFile.close()


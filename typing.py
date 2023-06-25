'''
A typiny tutor/traininy
progran, no install,
 copy, paste and run(CLI)
VERSION 1.0.0.1
'''
# REQUIRED IMPORTS
import os
import random

#DECLARE AND ASSIGN VARIABLE
choice = 0
subChoice = 0
menuItems = [["Letters Drill","Words Drill","Quit"],["Words Drill 1","Words Drill 2","Words Drill 3","*Go back"],["Beginner","Intermediate","Advance","*Go back"]]
#drills = ["fj","dk","sl","a;","fjgh","frju"]
accuracyPerLine=[]
wrongLetters = ""
wrongWords = ""
abc = "abcdef ghijklmnop qrstuvwxyz"
drills = ["fj","dk","sl","a;","fgjh","ftrjuy","deki","swlo","aq;p","fvbjmn","dxeki,","aq;zp/", abc]
lineWidth = 20
# drill for missing files
missingFiles = ["Files are missing","Using temp alternative","Please download the Three","files included with typing.py","First file is word_drill_1.txt","Second file is word_drill_2.txt","Third file is word_drill_3.txt","Place three files in","Same folder as typing.py","Thanks for using my app"]

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

def makeLine(chStr,num,choiceNum = "1"):
    line =""
    i = 0
    ch = ""
    #  loop and create str
    while i < num:
        ch = random.choice(chStr)
        if i==num-1 and ch ==" ":
            continue
        line += ch
        if choiceNum == "2" and not i == num-1:
            line += " "
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
    if not strWrongL == "":
        for ch in strWrongL:
            if ch in mistyped:
                mistyped[ch] += 1
            else:
                mistyped[ch] = 1
        # format the data
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
def printWordReport(percentList,mtypedWords):
    clear()
    mistypedWords = []
    print("Accuracy percent per line:")
    print(percentList)
    print("Mistyped Words:")
    if not mtypedWords == "":
        mistypedWords = mtypedWords.split(" ")
        mistypedWF  = ""
        i = 0
        for word in mistypedWords:
            mistypedWF += ("[" + word + "] ")
            i += 1
            if i % 4 == 0:
                mistypedWF += "\n"
        print(mistypedWF)
    else:
        print("[no mistyped words]")
        print("Drill completed\n return to main menu")
        pauseScr()
# impure funtion
def mistypedDrill(strCh,num,choiceNum):
    n = 5
    yesNo = "1"
    if yesNo == input("Practice using mistyped values\n yes:[ 1 ] no:[ 2 ]: ") :
        print()
        try:
            n = int(input("How many lines[Enter=5]: "))
        except:
            print("Not a valid, will use default(5)")
            n = 5
        for i in range(n):
            clear()
            if choiceNum == "1":
                dLine = makeLine(strCh,num)
            elif choiceNum == "2":
                words = strCh.split(" ")
                dLine = makeLine(words,4,"2")
            print("drill: "+dLine)
            typing = input("typed: ")
            percent,mistakes = feedback(dLine,typing)
            print(str(percent)+"% accurate")
            pauseScr()
        clear()
        print("[DRILL COMPLETED] \n return to main menu")
        pauseScr()

# MAIN PROGRAN LOOP
while True:
    clear()
    choice = menu(menuItems,0)
    if choice == "1":
        clear()
        subChoice = menu(menuItems,2)
        if not subChoice == "1" or "2" or "3" or "4":
            subChoice = "1"
    elif choice == "2":
        clear()
        subChoice = menu(menuItems,1)
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
            mistypedDrill(wrongLetters + " ",lineWidth,choice)
        accuracyPerLine = []
        wrongLetters = ""
    elif choice == "1" and (subChoice == "1" or subChoice == "2"):
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
            mistypedDrill(wrongLetters + " ",lineWidth,choice)
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
        if filePath == "":
            filePath = random.choice(["./word_drill_1.txt","./word_drill_2.txt","./word_drill_3.txt"])
        if os.path.isfile(filePath):
            with open(filePath) as dFile:
                for dLine in dFile.readlines():
                    dLine = dLine[0:-1]
                    print("drill: " + dLine)
                    typing = input("typed: ")
                    percent,missedWords = wordFeedback(dLine,typing)
                    accuracyPerLine.append(percent)
                    wrongWords += missedWords
                    print("\n"+str(percent)+"% words matched")
                    pauseScr()
                    clear()
                    # close file
                dFile.close()
            # check report feedback
            printWordReport(accuracyPerLine,wrongWords)
            if not wrongWords == "":
                mistypedDrill(wrongWords,0,choice)
            accuracyPerLine = []
            wrongWords = ""
        else:
            for dLine in missingFiles:
                print("drill: "+dLine)
                typing = input("typed: ")
                percent,missedWords =  wordFeedback(dLine,typing)
                accuracyPerLine.append(percent)
                wrongWords += missedWords
                print(str(percent)+"% Accuracy")
                pauseScr()
                clear()
            printWordReport(accuracyPerLine,wrongWords)
            if not wrongWords == "":
                mistypedDrill(wrongWords,0,choice)
                clear()
            else:
                pauseScr()
                clear()
                print("[DRILL COMPLETED]")
            print("Please downlown the required files to run word drills\n")
            print("more options with files, e.g change the content of files = new drills\n\n return to main menu")
            pauseScr()
            accuracyPerLine = []
            wrongWords = ""

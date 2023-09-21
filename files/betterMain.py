import csv
import datetime
import tkinter as tk

fileName = "files/days.csv"

dFont = "Calibri"
entryInput = input("Entry? >> ")


today = datetime.date.today().strftime("%d-%m-%Y")
now = datetime.datetime.now()


class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.mainloop()



def writeEntry(writeType):
    with open(fileName, writeType, encoding="utf-8", newline="") as fileObjW:
        w = csv.writer(fileObjW)
        
        fullEntry = [str(today),str(now.strftime("%H:%M:%S")),entryInput]
        w.writerow(fullEntry)
        
        fileObjW.close()

# reading file
with open(fileName, "r", encoding="utf-8") as fileObjR:
    r = csv.reader(fileObjR)
    entryList = []
    for row in r:
        entryList.append(row)
    
    if not entryList:
        doneToday = False
    else:
        doneToday = str(today) == entryList[-1][0]
    fileObjR.close()

# here compare today w/ most recent entry
if doneToday:
    writeEntry("w")
    print("Replaced.")
else:
    writeEntry("a")
    '''with open(fileName, "w", encoding="utf-8", newline="") as fileObjW:
        w = csv.writer(fileObjW)
        
        fullEntry = [str(today),str(now.strftime("%H:%M:%S")),entryInput]
        w.writerow(fullEntry)
        
        fileObjW.close()'''
    print("Appended.")

viewInput = input("View? >> ")
if viewInput == "Y":
    with open(fileName, "r", encoding="utf-8") as fileObjR2:
        r2 = csv.reader(fileObjR2)
        for row2 in r2:
            print(row2[0] + ",", row2[1] + " : \"" + row2[2] + "\"")
    print()
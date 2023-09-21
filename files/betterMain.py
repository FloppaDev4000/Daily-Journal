import csv
from datetime import datetime
from datetime import date
import tkinter as tk
from tkinter import ttk

fileName = "files/days.csv"

dFont = "Calibri"
dPadx = 20
dPady = 15
entryInput = "yes" #input("Entry? >> ")


today = date.today().strftime("%d-%m-%Y")
now = datetime.now()

class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.title("Main Window")

        # title
        self.mainLabel = tk.Label(self.root, text="Title Here", font=(dFont, 16))
        
        # text entry
        self.entryBox = tk.Text(self.root)
        
        # submit button
        self.entryButton = tk.Button(self.root, text="Submit Entry")
        
        # view past entries button
        self.viewButton = tk.Button(self.root, text="View Past Entries", command=self.viewEntries)
        
        # pack everything
        self.mainLabel.pack(padx=dPadx, pady=dPady)
        self.entryBox.pack(padx=dPadx, pady=dPady)
        self.entryButton.pack(padx=dPadx, pady=dPady)
        self.viewButton.pack(padx=dPadx, pady=dPady)
        self.root.mainloop()
    
    def viewEntries(self):
        entriesWindow = tk.Toplevel(self.root)

        entriesWindow.title("Past Entries")

        entriesWindow.geometry("500x350")

        self.words = tk.Label(entriesWindow,
                              text="text here",
                              anchor="w",
                              justify="left",
                              width=50)
        self.words.pack(padx=dPadx, pady=dPady)




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
    print("Appended.")

viewInput = "Y" #input("View? >> ")
if viewInput == "Y":
    fullData = []
    with open(fileName, "r", encoding="utf-8") as fileObjR2:
        r2 = csv.reader(fileObjR2)
        for row2 in r2:
            entry = row2[0] + ",", row2[1] + " : \"" + row2[2] + "\""
            fullData.append(entry)
    print()

mainWindow()
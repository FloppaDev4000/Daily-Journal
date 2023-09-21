import csv
from datetime import datetime
from datetime import date
import tkinter as tk
from tkinter import ttk

fileName = "files/days.csv"

dFont = "Calibri"
dPadx = 20
dPady = 12
# entryInput = "yes" #input("Entry? >> ")


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

        # warning label
        self.warning = tk.Label(self.root, text="", font=(dFont, 10))
        
        # submit button
        self.entryButton = tk.Button(self.root, text="Submit Entry", command=lambda: self.writeEntry(entryList))
        
        # view past entries button
        self.viewButton = tk.Button(self.root, text="View Past Entries", command=self.viewEntries)
        
        # pack everything
        self.mainLabel.pack(padx=dPadx, pady=dPady)
        self.entryBox.pack(padx=dPadx, pady=dPady)
        self.warning.pack(padx=dPadx, pady=5)
        self.entryButton.pack(padx=dPadx, pady=dPady)
        self.viewButton.pack(padx=dPadx, pady=dPady)
        self.root.mainloop()
    
    # second text box
    def viewEntries(self):
        entriesWindow = tk.Toplevel(self.root)

        entriesWindow.title("Past Entries")

        entriesWindow.geometry("500x350")

        self.words = tk.Text(entriesWindow,
                              width=50)
        
        self.words.pack(padx=dPadx, pady=dPady)
        self.words.insert("1.0", str(formattedEntries))
        self.words.config(state="disabled")
    
    # write to the CSV file
    def writeEntry(self, list_of_entries):
        
        entryInput = self.entryBox.get("1.0", tk.END)

        if entryInput != "\n":
            with open(fileName, "w", encoding="utf-8", newline="") as fileObjW:
                w = csv.writer(fileObjW)
                
                fullEntry = [str(today),str(now.strftime("%H:%M:%S")),entryInput.replace("\n", "")]
                list_of_entries.append(fullEntry)
                for i in list_of_entries:
                    w.writerow(i)
                
                fileObjW.close()
        else:
            self.warning.config(text = "There's nothing in the entry box!")
            print("didnt work")


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

formattedEntries = ""
for i in entryList:
    formattedEntries = formattedEntries + str(i[0]) + ", " + str(i[1]) + " >> " + str(i[2]) + "\n\n"

# here compare today w/ most recent entry
'''
if doneToday:
    writeEntry(entryList)
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
'''
mainWindow()